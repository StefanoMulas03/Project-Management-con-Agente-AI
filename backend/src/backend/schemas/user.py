from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr




class UserCreate(BaseModel):
    email: EmailStr



class UserUpdate(BaseModel):
    email: EmailStr | None = None



class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)







