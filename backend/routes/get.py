from fastapi import APIRouter, Security, Depends
from application.utils import VerifyToken
from sqlalchemy.orm import Session
from data.database import get_db
from data.models.automation import Automation
import logging

router = APIRouter()
auth = VerifyToken()

@router.get("/api/public")
def public():
    """No access token required to access this route"""
    
    logging.info("Hello World")

    result = {
        "status": "success",
        "msg": (
            "Hello from a public endpoint! You don't need to be "
            "authenticated to see this."
        ),
    }
    return result

@router.get("/api/private")
def private(auth_result: str = Security(auth.verify)):
    """A valid access token is required to access this route"""
    return {"text": "Hello World from the protected API"}

@router.get("/v1/api/automations")
def read_automations(db: Session = Depends(get_db)):
    automations = Automation.get_all(db)
    print(automations)
    return {"status": "success", "data": automations}

@router.get("/v1/api/automations/{automation_id}")
def read_automation(automation_id: int, db: Session = Depends(get_db)):
    automation = Automation.get_by_id(db, automation_id)
    if automation:
        return {"status": "success", "data": automation}
    return {"status": "error", "message": "Automation not found"}
