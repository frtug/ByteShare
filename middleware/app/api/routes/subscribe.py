from fastapi import APIRouter
from database.db import DynamoDBManager
from datetime import datetime, timezone
from pydantic import BaseModel

router = APIRouter()

# DynamoDB
subscriber_table_name = "byteshare-subscriber"
subscriber_dynamodb = DynamoDBManager(subscriber_table_name)


class Subscribe(BaseModel):
    email: str


@router.post("/")
def add_subscriber_return_done(body: Subscribe):
    """
    Adds new subscriber to DB.

    Parameters:
    - email: email of the subscriber

    Returns:
    - Done
    """

    subscriber = {
        "email": body.email,
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    subscriber_dynamodb.create_item(subscriber)

    return {"status": "Done"}
