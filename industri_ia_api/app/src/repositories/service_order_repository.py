import json
from typing import List

from database import dynamodb_client
from models.service_order import ServiceOrder
from daos.service_order_dao import ServiceOrderDao


class ServiceOrderRepository:
    def __init__(self):
        self.dao = ServiceOrderDao(dynamodb_client.instance)

    def create(self, text, orders):
        service_order = ServiceOrder(
            text=text,
            orders=orders
        )
        service_order.validate()
        return self.dao.create(service_order)

    def update(self, service_order):
        return self.dao.update(service_order)

    def get_all(self):
        return self.dao.get_all()

    def get_by(self, id):
        return self.dao.get_by(id)
