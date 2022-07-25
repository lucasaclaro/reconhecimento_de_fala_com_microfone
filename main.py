# instalar as bibliotecas SpeechRecognition, pipwin e PyAudio
# usar o terminal para instalar pipwin (pip install pipwin) e depois (pipwin install PyAudio)

import speech_recognition as sr

rec = sr.Recognizer()

# listar os microfones conectados aos computador
print(sr.Microphone().list_microphone_names())

# para escolher qual microfone usar, entre parênteses abaixo deve-se colocar o número do índice da lista que o microfone aparece no print acima
# para usar o microfone padrão, é só deixar em branco

with sr.Microphone() as mic:
# reconhecer o ruído para melhorar a captação de áudio
    rec.adjust_for_ambient_noise(mic)
    audio = rec.listen(mic)
    texto = rec.recognize_google(audio, language='pt-BR')
    print(texto)

