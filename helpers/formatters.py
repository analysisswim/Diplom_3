def normalize_order_number(num: str) -> str:
    """Лента может показывать номера с ведущими нулями: '#000123'."""
    num = (num or "").strip().lstrip("#")
    return str(int(num)) if num.isdigit() else num
