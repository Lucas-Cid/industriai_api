import json

from helpers.multipart_validator import MultipartValidator
from repositories.service_order_repository import ServiceOrderRepository
from services.audio_transcriber import AudioTranscriber
from services.service_order_processor import ServiceOrderProcessor
import traceback

class CreateServiceOrderLambda:
    def __init__(self):
        self.repository = ServiceOrderRepository()

    def handle(self, event):
        try:
            audio_file, error_response = MultipartValidator.validate(event)
            if error_response:
                return error_response

            transcription = AudioTranscriber.transcribe(audio_file)
            orders = ServiceOrderProcessor().process_transcription(transcription_text=transcription).get('orders')

            service_order = self.repository.create(transcription, orders)

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
