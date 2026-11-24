from pathlib import Path  # noqa: D100

from app.domain.order import Order
from app.services.importer import read_rows


def load_orders(path: Path) -> list[Order]:  # noqa: D103
    return [
        Order(waiter=row["waiter"], kopeks=int(row["kopeks"]))
        for row in read_rows(path)
    ]


def revenue_by_waiter(orders: list[Order], top: int = 0) -> dict[str, int]:
    """_summary_
    
    Args:
        orders: _description_
        top: _description_. По умолчанию 0.
    
    Raises:
        ValueError: _description_
    
    Returns:
        _description_
    """  # noqa: D415
    if not orders:
        raise ValueError("Список заказов пуст")
    totals: dict[str, int] = {}
    for order in orders:
        totals[order.waiter] = totals.get(order.waiter, 0) + order.kopeks
    ranked = sorted(totals.items(), key=lambda pair: -pair[1])
    if top:
        ranked = ranked[:top]
    return dict(ranked)


def sort_orders_in_place(orders: list[Order]) -> None:  # noqa: D103
    orders.sort(key=lambda order: -order.kopeks)
