from src.chatgpt import perguntar_chatgpt
from src.text_to_speech import gerar_audio

print("🤖 ChatGPT Voice Assistant (sem áudio de entrada)")
print("-" * 50)

texto = input("Digite sua pergunta: ")

resposta = perguntar_chatgpt(texto)

print("\nResposta do ChatGPT:")
print(resposta)

gerar_audio(resposta)
print("\n🔊 Áudio gerado em: audio/output.mp3")
