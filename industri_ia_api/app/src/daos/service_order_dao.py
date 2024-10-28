import time
import uuid
from typing import List

from boto3.dynamodb.conditions import Key

from models.service_order import ServiceOrder

class ServiceOrderDao:
    TABLE_NAME = 'indServiceOrder'

    def __init__(self, dynamodb_resource):
        self.table = dynamodb_resource.Table(self.TABLE_NAME)

    def create(self, service_order: ServiceOrder):
        item = {
            'id': self._generate_unique_key(),
            'text': service_order.text,
            'orders': service_order.orders
        }

        self.table.put_item(Item=self._remove_empty_attributes(item))
        return ServiceOrder(**item)

    def update(self, service_order: ServiceOrder):
        item = {
            'id': service_order.id,
            'text': service_order.text,
            'orders': service_order.orders
        }

        self.table.put_item(Item=self._remove_empty_attributes(item))
        return ServiceOrder(**item)


    def get_all(self) -> List[ServiceOrder]:
        items = self.table.scan().get('Items', [])
        print(items)
        return [ServiceOrder(**item) for item in items]

    def get_by(self, id):
        response = self.table.get_item(
            Key={
                'id': id,
            }
        )
        item = response.get('Item')
        if item:
            return ServiceOrder(**item)
        return None

    def _generate_unique_key(self) -> str:
        unique_uuid = str(uuid.uuid4())
        return f"{unique_uuid}"

    def _remove_empty_attributes(self, record):
        return {k: v for k, v in record.items() if v is not None}
