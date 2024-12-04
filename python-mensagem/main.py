from plyer import notification # Exibe uma notificação no canto inferior esquerdo

notification.notify(
title = "Aviso",
message = "Código finalizado!",
app_icon = "python-mensagem\python.ico",
timeout = 10 # Tempo em segundos para a notificação ficar visível
)