"""Cashback calculation module."""


def calculate_cashback(purchases: list[float], is_vip: bool = False) -> float:
    """Calculate total cashback for positive purchases."""
    total = 0.0
    rate = 0.05 if is_vip else 0.02

    for amount in purchases:
        if amount > 0:
            total += amount * rate

    return round(total, 2)
