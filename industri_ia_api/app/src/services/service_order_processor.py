import openai
import os
import json

class ServiceOrderProcessor:
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")
    def process_transcription(self, transcription_text):
        # Define o prompt para o ChatGPT
        prompt = (
            "Extraia as informações a seguir da transcrição fornecida e retorne no formato JSON especificado:\n\n"
            "Transcrição:\n"
            f"\"{transcription_text}\"\n\n"
            "Formato JSON esperado:\n"
            "{\n"
            "    \"orders\": [{\n"
            "        \"machine\": \"nome da maquina\",\n"
            "        \"production_line\": \"linha de produção\",\n"
            "        \"maintenance\": [\n"
            "            {\"procedure\": \"nome do procedimento necessário para manutencao\"}\n"
            "        ]\n"
            "    }]\n"
            "}\n\n"
            "Certifique-se de que o JSON seja válido e inclua todas as informações relevantes. Caso a máquina não seja especificada, escrecer 'Não especificada.' na resposta"
        )

        # Chama a API do OpenAI
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # Use o modelo apropriado
                messages=[
                    {"role": "system", "content": "Você é um assistente que extrai informações de textos e as formata em JSON."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=500,
                temperature=0  # Define a temperatura para 0 para respostas mais determinísticas
            )

            # Extrai a resposta do ChatGPT
            chatgpt_response = response['choices'][0]['message']['content'].strip()

            # Tenta converter a resposta em JSON
            ordem_servico = json.loads(chatgpt_response)

            return ordem_servico

        except Exception as e:
            # Lida com erros, como problemas de parsing
            print(f"Erro ao processar a transcrição: {e}")
            raise e
