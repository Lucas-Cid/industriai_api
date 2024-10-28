import json
import base64
from requests_toolbelt.multipart import decoder
from io import BytesIO

class NamedBytesIO(BytesIO):
    def __init__(self, data, name):
        super().__init__(data)
        self.name = name

class MultipartValidator:
    @staticmethod
    def validate(event):
        if 'body' not in event or event['body'] is None:
            return None, {
                "statusCode": 400,
                "body": json.dumps({"error": "Corpo da requisição ausente."})
            }

        headers = event.get("headers", {})
        content_type = headers.get("Content-Type") or headers.get("content-type")
        if not content_type:
            return None, {
                "statusCode": 400,
                "body": json.dumps({"error": "Cabeçalho 'Content-Type' ausente na requisição."})
            }

        is_base64_encoded = event.get('isBase64Encoded', False)
        body = event['body']
        if is_base64_encoded:
            body = base64.b64decode(body)
        else:
            body = body.encode('utf-8')

        multipart_data = decoder.MultipartDecoder(body, content_type)
        audio_data = None
        for part in multipart_data.parts:
            content_disposition = part.headers.get(b"Content-Disposition", b"").decode()
            if 'name="audio"' in content_disposition:
                audio_data = part.content
                break

        if audio_data is None:
            return None, {
                "statusCode": 400,
                "body": json.dumps({"error": "Campo 'audio' não encontrado no formulário multipart."})
            }

        return NamedBytesIO(audio_data, "audio.ogg"), None
