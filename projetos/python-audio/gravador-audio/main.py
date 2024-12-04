import pyaudio #--Import Da Biblioteca "pyaudio"
import wave #--Import Da Biblioteca "wave"

audio = pyaudio.PyAudio() # Pegar Informações Do Microfone

# Conficurações De Audio
receptor = audio.open (
    input = True,
    format = pyaudio.paInt16,
    channels = 1,
    rate = 4400,
    frames_per_buffer = 1024,
)

frames = []

# Criando Loop Para Criar Audio E Adicionar Frames Na Lista
try:
    print("Gravando... Pressione Ctrl+C para parar.")
    while True:
            bloco = receptor.read(1024)
            frames.append(bloco)
except KeyboardInterrupt:
    print("\n Gravação finalizada confira seu audio na pasta ''audio'' !")
    pass


receptor.start_stream()
receptor.close()
audio.terminate()
arquivo = wave.open("audio/gravacao.mp3", "wb")
arquivo.setnchannels(1)
arquivo.setframerate(4400)
arquivo.setsampwidth(audio.get_sample_size(pyaudio.paInt16))

arquivo.writeframes(b"".join(frames)) # Salvando Arquivo
arquivo.close()