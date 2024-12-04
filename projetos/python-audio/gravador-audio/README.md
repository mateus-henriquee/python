# Gravador de Áudio com PyAudio e Wave 🐍🌊

Este script em Python utiliza as bibliotecas `pyaudio` e `wave` para capturar áudio pelo microfone e salvar a gravação em um arquivo. 📁

## 🛠️ Requisitos

Certifique-se de ter as bibliotecas necessárias instaladas antes de executar o script:

- [PyAudio](https://pypi.org/project/PyAudio/)
- [Wave](https://docs.python.org/3/library/wave.html)

### 📦 Instalação do PyAudio

Caso o `pyaudio` não esteja instalado, você pode instalá-lo com o seguinte comando:

```bash
pip install pyaudio
```

> **Nota:** Se ocorrerem erros de instalação no Windows, você pode baixar o instalador apropriado no site [unofficial python binaries](https://www.lfd.uci.edu/~gohlke/pythonlibs/) e instalá-lo manualmente.

---

## 🚀 Funcionamento do Script
1. Configuração do Áudio:

- O script configura o microfone para gravar em formato `paInt16`, com uma taxa de amostragem de 4400 Hz, canal único (mono) e buffer de 1024 frames.


2. Gravação:

- O áudio é capturado em um loop contínuo, adicionando os frames gravados em uma lista (`frames`).
- O loop é encerrado manualmente pelo usuário pressionando `Ctrl+C`.


3. Armazenamento:

- A gravação é salva em um arquivo de áudio no formato `.mp3` na pasta `audio` com o nome `gravacao.mp3`

---

## 🧩 Como Usar

1. Clone ou baixe este repositório.

2. Certifique-se de que a pasta audio exista no mesmo diretório que o script.

3. Execute o script no terminal ou prompt de comando:

```bash
## bash:
python main.py
```

4. O terminal exibirá a seguinte mensagem enquanto captura o áudio:
5. 
```bash
## bash:
Gravando... Pressione Ctrl+C para parar.
```

5. Pressione `Ctrl+C` no terminal para finalizar a gravação.

6. O arquivo será salvo na pasta `audio`.

---

## 🔎 Observações

1. ### Formato do Arquivo:
- Embora o arquivo seja salvo com a extensão `.mp3`, o formato real do áudio é `.wav`. Para evitar confusão, é recomendável usar a extensão `.wav`.

2.  ### Compatibilidade:
- O código utiliza uma taxa de amostragem baixa (4400 Hz) e pode não atender a requisitos de qualidade mais alta.

---

## 📝 Licença 
- Este projeto é livre para uso e modificação. Sinta-se à vontade para ajustar o código e usá-lo como desejar.

---

⭐ **Se você gostou do projeto, não esqueça de dar uma estrela!**

Obrigado por visitar meu perfil! 😊