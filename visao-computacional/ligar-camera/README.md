# Projeto de Acesso à Câmera com Python OpenCV 📸💻🐍

Este projeto utiliza Python e a biblioteca OpenCV para acessar e exibir o feed da câmera do computador. Ele abre a câmera padrão (geralmente a webcam), captura os frames em tempo real e os exibe em uma janela. O usuário pode pressionar a tecla `'t'` para encerrar a aplicação e liberar a câmera.

## Pré-requisitos ⚙️

Antes de rodar o projeto, você precisa ter o Python instalado em seu sistema, além da biblioteca OpenCV.

1. **Instalar o Python**:
   - Você pode baixar o Python em: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. **Instalar a biblioteca OpenCV**:
   - Utilize o seguinte comando para instalar a biblioteca OpenCV com o `pip`:
   
     ```bash
     pip install opencv-python
     ```

## Como Executar 🚀

1. **Clone o repositório** ou baixe os arquivos do projeto.
2. **Execute o script Python**. Em um terminal ou prompt de comando, navegue até o diretório onde o arquivo do script está e execute o seguinte comando:

   ```bash
   python main.py
   ```

O código irá iniciar e abrir uma janela exibindo o feed da câmera. Você pode pressionar a tecla 't' para encerrar o programa.

## Como Funciona 🛠️
- **Abrindo a câmera**: O código utiliza a função cv2.VideoCapture(0) para acessar a câmera padrão do sistema. O índice 0 geralmente se refere à primeira câmera conectada.

- **Captura de frames**: O código captura frames da câmera em tempo real dentro de um laço while, e cada frame é mostrado na janela com a função cv2.imshow().

- **Saída do programa**: O programa continua exibindo a imagem da câmera até que o usuário pressione a tecla 't'. Quando isso acontece, o loop é interrompido e o programa libera a câmera com cap.release() e fecha a janela com cv2.destroyAllWindows().

## Possíveis Problemas ⚠️
- **Câmera não conectada**: Se o código não conseguir acessar a câmera, verifique se a câmera está conectada corretamente ao computador e se não há outros programas utilizando a câmera.

- **Erro ao capturar o frame**: Se o programa falhar ao capturar frames, isso pode indicar um problema de configuração do OpenCV ou da câmera. Verifique se você tem a versão correta do OpenCV instalada e se a câmera está funcionando com outros programas.