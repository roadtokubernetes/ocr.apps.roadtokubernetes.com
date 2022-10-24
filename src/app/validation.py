from fastapi import Depends, Header, HTTPException

from .settings import Settings, get_settings


def verify_auth(authorization=Header(None), settings: Settings = Depends(get_settings)):
    """
    Authorization: Bearer <token>
    {"authorization": "Bearer <token>"}
    """
    if settings.debug and settings.skip_auth:
        return
    if authorization is None:
        raise HTTPException(detail="Invalid endpoint", status_code=401)
    label, token = authorization.split()
    if token != settings.secret_token:
        raise HTTPException(detail="Invalid endpoint", status_code=401)
