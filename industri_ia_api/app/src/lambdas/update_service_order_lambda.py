import json


from helpers.multipart_validator import MultipartValidator
from repositories.service_order_repository import ServiceOrderRepository
from services.audio_transcriber import AudioTranscriber
from services.service_order_complementor import ServiceOrderComplementor
import traceback

class UpdateServiceOrderLambda:
    def __init__(self):
        self.repository = ServiceOrderRepository()

    def handle(self, event):
        try:
            audio_file, error_response = MultipartValidator.validate(event)
            if error_response:
                return error_response

            service_order_id = event.get('pathParameters')['id']
            service_order = self.repository.get_by(service_order_id)

            requested_changes = AudioTranscriber.transcribe(audio_file)
            orders = ServiceOrderComplementor().process_transcription(service_order, requested_changes)

            service_order.orders = orders

            service_order = self.repository.update(service_order)

            return {
                "statusCode": 200,
                "body": json.dumps(service_order.to_dict())
            }

        except Exception as e:
            traceback_str = ''.join(traceback.format_tb(e.__traceback__))
            print(f"Erro durante o processamento: {e}\nTraceback: {traceback_str}")
            return {
                "statusCode": 500,
                "body": json.dumps({"error": str(e)})
            }
