# Дробаха Александр, 37_qa_plus — дипломный проект
import requests
import configuration

_session = requests.Session()
_session.headers.update({"Content-Type": "application/json"})


def create_order(body):
    """POST /api/v1/orders — создание заказа."""
    url = configuration.URL_SERVICE + configuration.CREAT_ORDERS
    return _session.post(url, json=body, timeout=30)


def get_order(track_number):
    """GET /api/v1/orders/track?t=<track> — получить заказ по треку."""
    url = f"{configuration.URL_SERVICE}/api/v1/orders/track"
    return _session.get(url, params={"t": track_number}, timeout=30)
