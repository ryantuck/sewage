import datetime
from decimal import Decimal
from pydantic import BaseModel


class AmazonTransaction(BaseModel):
    transaction_date: datetime.date
    description: str
    subtotal: Decimal

class ChaseTransaction(BaseModel):
    occurred_on: datetime.date
    summary: str
    amount: Decimal

class CleanTransaction(BaseModel):
    transaction_date: datetime.date
    source_description: str
    amount: Decimal
