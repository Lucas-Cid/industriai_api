import json

from repositories.service_order_repository import ServiceOrderRepository

class GetServiceOrdersLambda:
    def handle(self, event):
        repository = ServiceOrderRepository()
        service_orders = repository.get_all()
        return { 'statusCode': 200, 'body': json.dumps({'serviceOrders': self._parse_content(service_orders)}) }

    def _parse_content(self, items):
        return [item.to_dict() for item in items]
