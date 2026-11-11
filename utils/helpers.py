"""Calculations for the inventory demonstration."""


def calculate_total_stock_value(items: list[dict[str, object]]) -> float:
    """Return the sum of quantity multiplied by unit price."""
    return sum(
        int(item["quantity"]) * float(item["price"])
        for item in items
    )
