# Дробаха Александр, 37_qa_plus — дипломный проект
import configuration
import requests
import data
from datetime import date, timedelta
import copy

# Создание заказа
def create_order(body):
    return requests.post(
        configuration.URL_SERVICE + configuration.CREAT_ORDERS,
        json=body,
        timeout=30
    )

# Получение заказа по номеру трекера
def get_order(track_number):
    get_order_url = f"{configuration.URL_SERVICE}/api/v1/orders/track?t={track_number}"
    response = requests.get(get_order_url, timeout=30)
    return response

# Дробаха Александр, 37_qa_plus — дипломный проект
# Автотест
def test_order_creation_and_retrieval():

    payload = copy.deepcopy(data.order_body)

    payload["deliveryDate"] = (date.today() + timedelta(days=1)).strftime("%Y-%m-%d")

    # 1) создание заказа
    response = create_order(payload)
    assert response.status_code in (201, 202), \
        f"Ожидали 201/202, получили {response.status_code}: {response.text}"

    # 2) сохранение номера трека
    track_number = response.json().get("track")
    assert track_number, f"В ответе нет track: {response.text}"
    print("Заказ создан. Номер трека:", track_number)

    # 3) получение данных заказа по треку
    order_response = get_order(track_number)
    assert order_response.status_code == 200, \
        f"Ошибка: {order_response.status_code}, {order_response.text}"

    order_data = order_response.json()
    print("Данные заказа:")
    print(order_data)