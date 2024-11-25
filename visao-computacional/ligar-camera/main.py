import cv2

# Abrir Câmera
cap = cv2.VideoCapture(0)  # 0 = Camera Padrão

# Verificar Se Ligou A Câmera
if not cap.isOpened():
    print("Não foi possível acessar a câmera")
    exit()

while True:
    # Capturar Frame Por Frame
    ret, frame = cap.read()

    # Verificar Se O Frame Foi Capturado
    if not ret:
        print("Falha ao capturar frame")
        break

    # Mostrar O Frame Na Janela
    cv2.imshow('Camera', frame)

    # Condição Para Ao Clicar 't' Sair
    if cv2.waitKey(1) & 0xFF == ord('t'):
        break

# Liberar A Câmera E Fechar As Janelas
cap.release()
cv2.destroyAllWindows()