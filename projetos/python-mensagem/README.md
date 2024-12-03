# Notificador de Conclusão de Código 💬

Este Projeto Simples Que Utiliza a Biblioteca **Plyer** Para Exibir Notificações No Sistema Operacional. O Objetivo Desse Projeto é Notificar o Usuário Com Uma Mensagem Ao Finalizar a Execução Do Código.

---

## 🚀 Funcionalidades

- Exibe uma notificação no canto inferior esquerdo da tela.
- Permite personalizar o título, mensagem e duração da notificação.

---

## 🛠️ Requisitos

- **Python 3.x**
- Biblioteca **Plyer**

---

## 📦 Instalação

1. Certifique-se de ter o Python instalado em sua máquina.
2. Instale a biblioteca Plyer utilizando o pip:
   ```bash
   pip install plyer

---

## 🖥️ Uso
1. Código:
```bash
from plyer import notification  # Exibe uma notificação no canto inferior esquerdo

notification.notify(
    title="Aviso",
    message="Código finalizado!",
    timeout=10  # Tempo em segundos para a notificação ficar visível
)

```

2. Execute o script com o comando:

```bash
python projetos\python-mensagem
```

---

## 💡 Personalização: 
### Fique à vontade para personalizar o código como quiser!
- Você pode modificar o título, a mensagem e o tempo de exibição para atender às suas necessidades.

---

## 📚 Recursos adicionais
- Documentação oficial do [Plyer]([https://www.linkedin.com/in/devmateus-henriquee/](https://plyer.readthedocs.io/en/latest/))

---

## 📝 Licença
- Este projeto é livre para uso e modificação. Sinta-se à vontade para ajustar o código e usá-lo como desejar.
