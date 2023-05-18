import cv2
import dlib

# Carrega o modelo pré-treinado para detecção facial
detector = dlib.get_frontal_face_detector()

# Inicializa a webcam
cap = cv2.VideoCapture(0)

while True:
    # Lê o frame da webcam
    ret, frame = cap.read()
    
    # Converte o frame para escala de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detecta as faces no frame
    faces = detector(gray)
    
    # Itera sobre as faces detectadas
    for face in faces:
        # Obtém as coordenadas da caixa delimitadora da face
        x, y, w, h = face.left(), face.top(), face.width(), face.height()
        
        # Desenha um retângulo ao redor da face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    # Mostra o frame com as faces detectadas
    cv2.imshow('Video', frame)
    
    # Verifica se a tecla 'q' foi pressionada para sair do loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera os recursos utilizados
cap.release()
cv2.destroyAllWindows()