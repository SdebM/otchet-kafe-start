def calculate_average(grades: list[int]) -> float:  # noqa: D100, D103
    if not grades:
        raise ValueError("Список оценок пуст")
    return round(sum(grades) / len(grades), 2)


def grade_bounds(grades: list[int]) -> tuple[int, int]:
    """_summary_.
    
    Args:
        grades: _description_
    
    Raises:
        ValueError: _description_
    
    Returns:
        _description_
    """
    if not grades:
        raise ValueError("Список оценок пуст")
    return min(grades), max(grades)
