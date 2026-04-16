from datetime import datetime
from typing import Optional, Literal

from pydantic import BaseModel, EmailStr, Field


# -------------------------
# USERS / AUTH
# -------------------------

class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)

class UserOut(BaseModel):
    id: int
    email: EmailStr
    is_active: bool = True

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    sub: Optional[str] = None  # email (subject)


# -------------------------
# TASKS
# -------------------------

Priority = Literal["Low", "Medium", "High"]


class TaskBase(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    category: Optional[str] = Field(default=None, max_length=80)
    due_date: Optional[str] = Field(default=None, max_length=20)  # păstrăm string pt simplu ("2026-01-31")
    priority: Priority = "Medium"
    done: bool = False


class TaskCreate(TaskBase):
    # moștenește tot din TaskBase; aici poți adăuga validări extra dacă vrei
    pass


class TaskUpdate(BaseModel):
    title: Optional[str] = Field(default=None, min_length=1, max_length=200)
    category: Optional[str] = Field(default=None, max_length=80)
    due_date: Optional[str] = Field(default=None, max_length=20)
    priority: Optional[Priority] = None
    done: Optional[bool] = None


class TaskOut(TaskBase):
    id: int
    owner_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
