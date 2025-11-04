from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from db import Base

class ShiftAllowance(Base):
    __tablename__ = "shift_allowances"

    id = Column(Integer, primary_key=True, index=True)
    emp_id = Column(String, nullable=False, unique=True, index=True)
    emp_name = Column(String, nullable=False)
    grade = Column(String)
    current_status = Column(String)
    department = Column(String)
    client = Column(String)
    project = Column(String)
    project_code = Column(String)
    account_manager = Column(String)
    practice_lead = Column(String)
    delivery_manager = Column(String)
    duration_month = Column(String)
    payroll_month = Column(String)

    shift_a_days = Column(Integer, default=0)
    shift_b_days = Column(Integer, default=0)
    shift_c_days = Column(Integer, default=0)
    prime_days = Column(Integer, default=0)

    total_shift_types = Column(Integer, default=0)
    total_days = Column(Integer, default=0)
    ts_billable_days = Column(Integer, default=0)
    ts_non_billable_days = Column(Integer, default=0)
    diff = Column(Integer, default=0)
    final_total_days = Column(Integer, default=0)
    billability_status = Column(String)
    practice_remarks = Column(String)
    rmg_comments = Column(String)
    amar_approval = Column(String)

    shift_a_allowance = Column(Float, default=0.0)
    shift_b_allowance = Column(Float, default=0.0)
    shift_c_allowance = Column(Float, default=0.0)
    prime_allowance = Column(Float, default=0.0)
    total_days_allowance = Column(Float, default=0.0)

    am_email_attempt = Column(String)
    am_approval_status = Column(String)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    mobile_number = Column(String, nullable=False)
    password = Column(String, nullable=False)  
    role = Column(String, default="HR", nullable=False)  