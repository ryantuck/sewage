from typing import List, Union
from .models import *


class SewageException(Exception):
    """Catch-all exception"""


def clean_amazon_transaction(t: AmazonTransaction) -> CleanTransaction:
    return CleanTransaction(
        transaction_date=t.transaction_date,
        source_description=t.description,
        amount=t.subtotal,
    )


def clean_chase_transaction(t: ChaseTransaction) -> CleanTransaction:
    return CleanTransaction(
        transaction_date=t.occurred_on,
        source_description=t.summary,
        amount=t.amount,
    )


def clean_transaction(
    source: Union[AmazonTransaction, ChaseTransaction]
) -> CleanTransaction:
    if isinstance(source, AmazonTransaction):
        return clean_amazon_transaction(source)
    if isinstance(source, ChaseTransaction):
        return clean_chase_transaction(source)
    raise SewageException(f"Unsupported input type: {type(source)}")


def clean_transactions(sources: List) -> List[CleanTransaction]:
    return [clean_transaction(source) for source in sources]
