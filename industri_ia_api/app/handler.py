import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from lambdas.get_service_orders_lambda import GetServiceOrdersLambda
from lambdas.create_service_order_lambda import CreateServiceOrderLambda
from lambdas.update_service_order_lambda import UpdateServiceOrderLambda

lambda_classes = {
    'create_service_order_lambda': CreateServiceOrderLambda,
    'get_service_order_lambda': GetServiceOrdersLambda,
    'update_service_order_lambda': UpdateServiceOrderLambda,
}

for method_name, cls in lambda_classes.items():
    def lambda_function(event, context, cls=cls):
        return cls().handle(event)
    globals()[method_name] = lambda_function
