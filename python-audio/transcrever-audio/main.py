import whisper #--Importando a Biblioteca "openai-whisper"

# Transcrevendo Audio
modelo = whisper.load_model("base") # Setando Modelo

audio = modelo.transcribe("gravacao.mp3") # Transcrevendo Audio...

print(audio)