from sewage.transforms import *
from sewage.models import *


def amazon_transactions():
    return [
        AmazonTransaction(
            transaction_date=datetime.date(2021, 5, 27),
            description="Oreos",
            subtotal=3.79,
        ),
        AmazonTransaction(
            transaction_date=datetime.date(2021, 5, 27),
            description="Bananas",
            subtotal=0.89,
        ),
        AmazonTransaction(
            transaction_date=datetime.date(2021, 5, 28),
            description="Rubiks Cube",
            subtotal=20.47,
        ),
    ]


def chase_transactions():
    return [
        ChaseTransaction(
            occurred_on=datetime.date(2021, 5, 26),
            summary="GAS SHELL 12356",
            amount=27.62,
        ),
        ChaseTransaction(
            occurred_on=datetime.date(2021, 5, 27),
            summary="POSTMATES CA",
            amount=32.23,
        ),
        ChaseTransaction(
            occurred_on=datetime.date(2021, 5, 28),
            summary="GR MRKTSBP SBX",
            amount=6.12,
        ),
    ]


def get_clean_transactions():
    sources = amazon_transactions() + chase_transactions()
    return clean_transactions(sources)


if __name__ == "__main__":
    txs = get_clean_transactions()
    for tx in txs:
        print(tx)
