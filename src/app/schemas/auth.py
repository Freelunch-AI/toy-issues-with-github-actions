"""Authentication schemas for request and response models."""

from pydantic import BaseModel

class Token(BaseModel):
    """Schema for JWT token response."""
    access_token: str
    token_type: str

class LoginData(BaseModel):
    """Schema for login request data."""
    username: str
    password: str