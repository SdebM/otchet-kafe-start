import pathlib  # noqa: D100

from app.services.orders import load_orders, revenue_by_waiter
from app.ui.console import print_report
from app.utils.clock import today_label
from app.utils.formatter import format_kopeks, format_title



def build_report(path: pathlib.Path) -> list[str]:
    """_summary_.

    Args:
        path (Path): _description_

    Returns:
        list[str]: _description_
    """    
    orders = load_orders(path)
    revenue = revenue_by_waiter(orders)
    lines = [format_title(f" Смена {today_label()} ")]
    for waiter, kopeks in revenue.items():
        lines.append(f"{waiter:<20}{format_kopeks(kopeks):>20}")
    lines.append(format_title(f" Итого {format_kopeks(sum(revenue.values()))} "))
    return lines


if __name__ == "__main__":
    print_report(build_report(pathlib.Path("data/smena.csv")))
