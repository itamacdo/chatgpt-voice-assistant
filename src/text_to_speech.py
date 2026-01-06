from gtts import gTTS

def gerar_audio(texto, caminho_saida="audio/output.mp3"):
    tts = gTTS(text=texto, lang="pt")
    tts.save(caminho_saida)
