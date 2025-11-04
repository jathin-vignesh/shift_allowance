from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from models.models import ShiftAllowance
from db import get_db
from schemas.shift_allowance_schema import ShiftAllowanceCreate, ShiftAllowanceUpdate, ShiftAllowanceResponse
from utils.dependencies import HR_required
router = APIRouter(prefix="/shift")

# CREATE
@router.post("/", response_model=ShiftAllowanceResponse)
def create_shift(data: ShiftAllowanceCreate, db: Session = Depends(get_db),current_user = Depends(HR_required)):
    existing = db.query(ShiftAllowance).filter(ShiftAllowance.emp_id == data.emp_id).first()
    if existing:
        raise HTTPException(status_code=400, detail="Employee ID already exists")
    new_entry = ShiftAllowance(**data.dict())
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)
    return new_entry

# READ ALL
@router.get("/", response_model=List[ShiftAllowanceResponse])
def get_all_shifts(db: Session = Depends(get_db),current_user = Depends(HR_required)):
    return db.query(ShiftAllowance).all()

# READ ONE BY ID
@router.get("/emp/{emp_id}", response_model=ShiftAllowanceResponse)
def get_shift(emp_id: str, db: Session = Depends(get_db),current_user = Depends(HR_required)):
    entry = db.query(ShiftAllowance).filter(ShiftAllowance.emp_id == emp_id).first()
    if not entry:
        raise HTTPException(status_code=404, detail="Record not found")
    return entry

#READ BY EMP ID
@router.get("/{id}", response_model=ShiftAllowanceResponse)
def get_shift(id: int, db: Session = Depends(get_db),current_user = Depends(HR_required)):
    entry = db.query(ShiftAllowance).filter(ShiftAllowance.id == id).first()
    if not entry:
        raise HTTPException(status_code=404, detail="Record not found")
    return entry

# PATCH UPDATE BY ID
@router.patch("/{id}", response_model=ShiftAllowanceResponse)
def update_shift(id: int, data: ShiftAllowanceUpdate, db: Session = Depends(get_db),current_user = Depends(HR_required)):
    entry = db.query(ShiftAllowance).filter(ShiftAllowance.id == id).first()
    if not entry:
        raise HTTPException(status_code=404, detail="Record not found")
    update_data = data.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(entry, field, value)
    db.commit()
    db.refresh(entry)
    return entry

# DELETE BY ID
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_shift_by_id(id: int, db: Session = Depends(get_db),current_user = Depends(HR_required)):
    entry = db.query(ShiftAllowance).filter(ShiftAllowance.id == id).first()
    if not entry:
        raise HTTPException(status_code=404, detail="Record not found")
    db.delete(entry)
    db.commit()
    return

# DELETE BY EMP ID
@router.delete("/emp/{emp_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_shift_by_emp_id(emp_id: str, db: Session = Depends(get_db),current_user = Depends(HR_required)):
    entry = db.query(ShiftAllowance).filter(ShiftAllowance.emp_id == emp_id).first()
    if not entry:
        raise HTTPException(status_code=404, detail="Record not found")
    db.delete(entry)
    db.commit()
    return
