from typing import Dict, List, Optional, Tuple, Union
from datetime import datetime

from pydantic import BaseModel, field_validator
import re

EMAILREGEXP = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,7}\b(?!.{101,})')


class CreateUser(BaseModel):
    name: str
    email: str 
    province: str
    city: str
    major: str

    @field_validator("email", check_fields=False)
    def validate_email(cls, v):
        if not EMAILREGEXP.match(v):
            raise ValueError(
                "Invalid Email"
            )
        return v

class UserResponse(CreateUser):
    id:int
    created_at:datetime
    
    class Config:
        from_attributes = True

class UserResponseList(BaseModel):
    Users: List[UserResponse]