class ServiceOrder:
    def __init__(self, id=None, text: str = None, orders = None):
        self.id = id
        self.text = text
        self.orders = orders

    def validate(self):
        error_attributes = []
        if not self.text:
            error_attributes.append('text')

        if not self.orders:
            error_attributes.append('orders')

        if error_attributes:
            raise ValueError(f"{', '.join(error_attributes)} cannot be blank")

    def to_dict(self):
        return {
            'id': self.id,
            'transcription': self.text,
            'orders': self.orders
        }
