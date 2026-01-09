BASE_URL = "https://stellarburgers.education-services.ru/"
API_BASE_URL = f"{BASE_URL}api"

URL_PARTS = {
    "domain": "stellarburgers",
    "feed": "feed",
    "login": "login",
}

PAGES = {
    "main": BASE_URL,
    "feed": f"{BASE_URL}feed",
    "login": f"{BASE_URL}login",
    "register": f"{BASE_URL}register",
    "profile": f"{BASE_URL}profile",
    "profile_orders": f"{BASE_URL}profile/orders",
}

API_ENDPOINTS = {
    "register": f"{API_BASE_URL}/auth/register",
    "login": f"{API_BASE_URL}/auth/login",
    "user": f"{API_BASE_URL}/auth/user",
    "orders": f"{API_BASE_URL}/orders",
    "orders_all": f"{API_BASE_URL}/orders/all",
    "ingredients": f"{API_BASE_URL}/ingredients",
}
