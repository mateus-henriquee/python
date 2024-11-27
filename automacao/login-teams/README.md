# Automação de Login no Microsoft Teams com Python 🤖💻🐍

Este projeto automatiza o processo de login no Microsoft Teams utilizando Python e a biblioteca `pyautogui`. O script abre o Google Chrome, navega até a página de login do Teams e preenche automaticamente o usuário e senha, facilitando o acesso ao aplicativo de maneira rápida.

## Pré-requisitos ⚙️

Antes de rodar o projeto, você precisa ter o Python instalado em seu sistema, além da biblioteca `pyautogui`.

1. **Instalar o Python**:
   - Você pode baixar o Python em: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. **Instalar a biblioteca `pyautogui`**:
   - Utilize o seguinte comando para instalar a biblioteca `pyautogui` com o `pip`:
   
     ```bash
     pip install pyautogui
     ```

3. **Certifique-se de ter o Google Chrome instalado** no seu computador, pois o script o utilizará para abrir o Teams.

## Como Executar 🚀

1. **Clone o repositório** ou baixe os arquivos do projeto.
2. **Execute o script Python**. Em um terminal ou prompt de comando, navegue até o diretório onde o arquivo do script está e execute o seguinte comando:

   ```bash
   python main.py
   ```

 ## Como Funciona 🛠️
- **Abrir o Google Chrome**: O script utiliza o pyautogui para pressionar a tecla win (Windows), abrir o Google Chrome e navegar até a URL do Microsoft Teams: https://teams.microsoft.com/v2/.

- **Preencher o login**: Após o carregamento da página, o script preenche automaticamente o email e a senha no formulário de login.

- **Aguardar os tempos de resposta**: Utilizando o comando time.sleep(), o script aguarda alguns segundos para garantir que o Chrome e o Teams carreguem corretamente antes de preencher as informações de login.

## Personalização 🔧
- **Email e Senha**: Substitua os valores "meulogin@gmai.co" e "minhasenha123" no código pelos seus dados de login.

- **Ajuste os tempos de espera**: A função time.sleep() pode ser ajustada conforme necessário, dependendo da velocidade de sua conexão ou do desempenho do computador.

## Possíveis Problemas ⚠️
- **Erros ao iniciar o Google Chrome**: Se o comando para abrir o Google Chrome não funcionar, verifique se o caminho do aplicativo está correto no seu sistema.
  
- **Tempo de espera**: Se o Teams ou o Chrome demorar mais do que o esperado para carregar, ajuste o valor de time.sleep() para garantir que o script não tente preencher os campos de login antes de eles estarem visíveis.
