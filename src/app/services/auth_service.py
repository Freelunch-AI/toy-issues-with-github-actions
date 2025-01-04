"""Authentication service for handling user authentication and token generation."""

from datetime import datetime, timedelta
from jose import JWTError, jwt
from typing import Optional
from app.core.config import settings

class AuthService:
    """Service for handling authentication operations."""

    def authenticate_user(self, username: str, password: str) -> bool:
        """
        Authenticate user with username and password.
        
        Args:
            username: Username to verify
            password: Password to verify
            
        Returns:
            bool: True if credentials are valid, False otherwise
        """
        return (username == settings.ADMIN_USERNAME and 
                password == settings.ADMIN_PASSWORD)

    def create_access_token(self, data: dict, expires_delta: Optional[timedelta] = None):
        """
        Create a new JWT access token.
        
        Args:
            data: Data to encode in the token
            expires_delta: Optional expiration time
            
        Returns:
            str: JWT token
        """
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
        return encoded_jwt