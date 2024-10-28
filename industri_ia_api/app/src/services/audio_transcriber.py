import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

class AudioTranscriber:
    @staticmethod
    def transcribe(audio_file):
        transcription_result = openai.Audio.transcribe("whisper-1", audio_file)
        return transcription_result.get('text', '')
