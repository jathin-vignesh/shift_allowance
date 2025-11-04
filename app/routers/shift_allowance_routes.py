from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from db import get_db
from schemas.shift_allowance_schema import ShiftAllowanceCreate, ShiftAllowanceUpdate, ShiftAllowanceResponse
from utils.dependencies import HR_required
from services import shift_allowance_service

router = APIRouter(prefix="/shift")

@router.post("/", response_model=ShiftAllowanceResponse)
def create_shift(
    data: ShiftAllowanceCreate, db: Session = Depends(get_db), current_user=Depends(HR_required)
):
    return shift_allowance_service.create_shift(db, data)


@router.get("/", response_model=List[ShiftAllowanceResponse])
def get_all_shifts(db: Session = Depends(get_db), current_user=Depends(HR_required)):
    return shift_allowance_service.get_all_shifts(db)


@router.get("/emp/{emp_id}", response_model=ShiftAllowanceResponse)
def get_shift_by_emp_id(emp_id: str, db: Session = Depends(get_db), current_user=Depends(HR_required)):
    return shift_allowance_service.get_shift_by_emp_id(db, emp_id)


@router.get("/{id}", response_model=ShiftAllowanceResponse)
def get_shift_by_id(id: int, db: Session = Depends(get_db), current_user=Depends(HR_required)):
    return shift_allowance_service.get_shift_by_id(db, id)


@router.patch("/{id}", response_model=ShiftAllowanceResponse)
def update_shift(id: int, data: ShiftAllowanceUpdate, db: Session = Depends(get_db), current_user=Depends(HR_required)):
    return shift_allowance_service.update_shift(db, id, data)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_shift_by_id(id: int, db: Session = Depends(get_db), current_user=Depends(HR_required)):
    shift_allowance_service.delete_shift_by_id(db, id)
    return


@router.delete("/emp/{emp_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_shift_by_emp_id(emp_id: str, db: Session = Depends(get_db), current_user=Depends(HR_required)):
    shift_allowance_service.delete_shift_by_emp_id(db, emp_id)
    return
