from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from . import token
from typing import Annotated
from .database import get_db
from sqlalchemy.orm import Session
from . import models

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
 
def get_current_user(data: Annotated[str, Depends(oauth2_scheme)], db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    ) 

    # return token.verify_token(data, credentials_exception)
    token_data = token.verify_token(data, credentials_exception)
    if not token_data or not token_data.email:
        raise credentials_exception
    
    user = db.query(models.User).filter(models.User.email == token_data.email).first()
    if not user:
        raise credentials_exception
    
    return user
    