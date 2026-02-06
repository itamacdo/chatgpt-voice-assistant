# ChatGPT com Entrada de Texto e Saída em Áudio

## Sobre o Projeto

Este projeto simula uma **interação por voz com o ChatGPT**, priorizando **compatibilidade entre diferentes ambientes**.

Para evitar dependências de microfone ou APIs de reconhecimento de fala, a entrada do usuário é feita por **texto digitado**, representando a etapa de **Speech-to-Text (STT)**.
A resposta gerada pelo ChatGPT é convertida em **áudio**, utilizando o **Google Text-to-Speech (gTTS)**, simulando a etapa de **Text-to-Speech (TTS)**.

---

## Objetivos

* Simular uma aplicação de conversação por voz
* Garantir funcionamento em ambientes sem suporte a microfone
* Facilitar testes e estudos em IA conversacional
* Demonstrar o uso de TTS com respostas do ChatGPT

---

## Como Funciona

1. O usuário digita uma mensagem (simulando Speech-to-Text)
2. O texto é enviado ao ChatGPT
3. O ChatGPT retorna uma resposta em texto
4. A resposta é convertida em áudio com **gTTS**
5. O áudio é reproduzido para o usuário

---

## Tecnologias Utilizadas

* **Python**
* **ChatGPT (OpenAI API)**
* **Google Text-to-Speech (gTTS)**
* Entrada de dados via texto (simulação de STT)

---

## Estrutura do Projeto (Exemplo)

```bash
📁 projeto-chatgpt-tts
├── main.py
├── requirements.txt
├── README.md
└── audio/
    └── resposta.mp3
```

---

## Requisitos

* Python **3.8 ou superior**
* Conexão com a internet

---

## Instalação das Dependências

```bash
pip install gtts
```

---

## Como Executar

```bash
python main.py
```

Após executar:

* Digite sua pergunta no terminal
* O ChatGPT responderá
* A resposta será convertida em áudio automaticamente

---

## Possíveis Melhorias Futuras

* Integração real com Speech-to-Text (Whisper, Google Speech API)
* Interface gráfica (Tkinter, Electron ou Web)
* Suporte a múltiplos idiomas
* Ajuste de voz, velocidade e tom do áudio
* Deploy como aplicação web ou API



Este projeto é de uso **educacional e experimental**.



