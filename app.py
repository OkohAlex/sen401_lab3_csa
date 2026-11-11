"""Display the initial inventory and its total stock valuation."""

from inventory import INVENTORY_ITEMS
from utils.helpers import calculate_total_stock_value


def main() -> None:
    """Print inventory records and the total value of available stock."""
    for item in INVENTORY_ITEMS:
        print(
            f"{item['item_name']}: {item['quantity']} units "
            f"at ${item['price']:.2f}"
        )
    print(f"Total stock value: ${calculate_total_stock_value(INVENTORY_ITEMS):.2f}")


if __name__ == "__main__":
    main()
