from pydantic import BaseModel
from typing import Optional

class ShiftAllowanceBase(BaseModel):
    emp_id: str
    emp_name: str
    grade: Optional[str] = None
    current_status: Optional[str] = None
    department: Optional[str] = None
    client: Optional[str] = None
    project: Optional[str] = None
    project_code: Optional[str] = None
    account_manager: Optional[str] = None
    practice_lead: Optional[str] = None
    delivery_manager: Optional[str] = None
    duration_month: Optional[str] = None
    payroll_month: Optional[str] = None
    shift_a_days: Optional[int] = 0
    shift_b_days: Optional[int] = 0
    shift_c_days: Optional[int] = 0
    prime_days: Optional[int] = 0
    total_shift_types: Optional[int] = 0
    total_days: Optional[int] = 0
    ts_billable_days: Optional[int] = 0
    ts_non_billable_days: Optional[int] = 0
    diff: Optional[int] = 0
    final_total_days: Optional[int] = 0
    billability_status: Optional[str] = None
    practice_remarks: Optional[str] = None
    rmg_comments: Optional[str] = None
    amar_approval: Optional[str] = None
    shift_a_allowance: Optional[float] = 0.0
    shift_b_allowance: Optional[float] = 0.0
    shift_c_allowance: Optional[float] = 0.0
    prime_allowance: Optional[float] = 0.0
    total_days_allowance: Optional[float] = 0.0
    am_email_attempt: Optional[str] = None
    am_approval_status: Optional[str] = None

class ShiftAllowanceCreate(ShiftAllowanceBase):
    pass

class ShiftAllowanceUpdate(BaseModel):
    emp_name: Optional[str] = None
    grade: Optional[str] = None
    current_status: Optional[str] = None
    department: Optional[str] = None
    shift_a_days: Optional[int] = None
    shift_b_days: Optional[int] = None
    shift_c_days: Optional[int] = None
    prime_days: Optional[int] = None
    shift_a_allowance: Optional[float] = None
    shift_b_allowance: Optional[float] = None
    shift_c_allowance: Optional[float] = None
    prime_allowance: Optional[float] = None
    total_days_allowance: Optional[float] = None

class ShiftAllowanceResponse(ShiftAllowanceBase):
    id: int
    class Config:
        from_attributes = True
