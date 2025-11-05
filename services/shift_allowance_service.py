from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from models.models import ShiftAllowance
from schemas.shift_allowance_schema import ShiftAllowanceCreate, ShiftAllowanceUpdate


def create_shift(db: Session, data: ShiftAllowanceCreate):
    existing = db.query(ShiftAllowance).filter(ShiftAllowance.emp_id == data.emp_id).first()
    if existing:
        raise HTTPException(status_code=400, detail="Employee ID already exists")
    new_entry = ShiftAllowance(**data.model_dump())
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)
    return new_entry


def get_all_shifts(db: Session):
    return db.query(ShiftAllowance).all()


def get_shift_by_emp_id(db: Session, emp_id: str):
    entry = db.query(ShiftAllowance).filter(ShiftAllowance.emp_id == emp_id).first()
    if not entry:
        raise HTTPException(status_code=404, detail="Record not found")
    return entry


def get_shift_by_id(db: Session, id: int):
    entry = db.query(ShiftAllowance).filter(ShiftAllowance.id == id).first()
    if not entry:
        raise HTTPException(status_code=404, detail="Record not found")
    return entry


def update_shift(db: Session, id: int, data: ShiftAllowanceUpdate):
    entry = db.query(ShiftAllowance).filter(ShiftAllowance.id == id).first()
    if not entry:
        raise HTTPException(status_code=404, detail="Record not found")
    update_data = data.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(entry, field, value)
    db.commit()
    db.refresh(entry)
    return entry


def delete_shift_by_id(db: Session, id: int):
    entry = db.query(ShiftAllowance).filter(ShiftAllowance.id == id).first()
    if not entry:
        raise HTTPException(status_code=404, detail="Record not found")
    db.delete(entry)
    db.commit()


def delete_shift_by_emp_id(db: Session, emp_id: str):
    entry = db.query(ShiftAllowance).filter(ShiftAllowance.emp_id == emp_id).first()
    if not entry:
        raise HTTPException(status_code=404, detail="Record not found")
    db.delete(entry)
    db.commit()
