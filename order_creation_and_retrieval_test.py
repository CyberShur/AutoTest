# Дробаха Александр, 37_qa_plus — дипломный проект
import copy
from datetime import date, timedelta

import data
from sender_stand_request import create_order, get_order


def test_order_creation_and_retrieval():
    # Готовим тело заказа (важно не мутировать исходник)
    payload = copy.deepcopy(data.order_body)
    payload["deliveryDate"] = (
        date.today() + timedelta(days=1)).strftime("%Y-%m-%d")

    # 1) Создать заказ
    response = create_order(payload)
    assert response.status_code in (201, 202), \
        f"Ожидали 201/202, получили {response.status_code}: {response.text}"

    # 2) Сохранить трек
    track_number = response.json().get("track")
    assert track_number, f"В ответе нет track: {response.text}"
    print("Заказ создан. Номер трека:", track_number)

    # 3) Получить заказ по треку
    order_response = get_order(track_number)
    assert order_response.status_code == 200, \
        f"Ошибка: {order_response.status_code}, {order_response.text}"

    print("Данные заказа:")
    print(order_response.json())
