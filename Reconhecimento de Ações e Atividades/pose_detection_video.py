import cv2
import mediapipe as mp
import os
import urllib.request
from tqdm import tqdm

MODEL_URL = "https://storage.googleapis.com/mediapipe-models/pose_landmarker/pose_landmarker_lite/float16/latest/pose_landmarker_lite.task"


def ensure_pose_model(model_path):
    if os.path.exists(model_path):
        return model_path

    print("Modelo de pose não encontrado. Baixando...")
    urllib.request.urlretrieve(MODEL_URL, model_path)
    print(f"Modelo salvo em: {model_path}")
    return model_path


def draw_pose(frame, pose_landmarks):
    h, w, _ = frame.shape
    connections = mp.tasks.vision.PoseLandmarksConnections.POSE_LANDMARKS

    # Desenhar conexões
    for conn in connections:
        start = pose_landmarks[conn.start]
        end = pose_landmarks[conn.end]

        x1, y1 = int(start.x * w), int(start.y * h)
        x2, y2 = int(end.x * w), int(end.y * h)

        cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # Desenhar pontos
    for lm in pose_landmarks:
        x, y = int(lm.x * w), int(lm.y * h)
        cv2.circle(frame, (x, y), 3, (0, 0, 255), -1)


def detect_pose(video_path, output_path):
    model_dir = os.path.join(os.path.expanduser("~"), ".mediapipe_models")
    os.makedirs(model_dir, exist_ok=True)
    model_path = ensure_pose_model(os.path.join(model_dir, "pose_landmarker_lite.task"))

    # Inicializar o Pose Landmarker (MediaPipe Tasks API)
    base_options = mp.tasks.BaseOptions(model_asset_path=model_path)
    options = mp.tasks.vision.PoseLandmarkerOptions(
        base_options=base_options,
        running_mode=mp.tasks.vision.RunningMode.VIDEO,
        num_poses=1,
    )
    pose_landmarker = mp.tasks.vision.PoseLandmarker.create_from_options(options)

    # Capturar vídeo do arquivo especificado
    cap = cv2.VideoCapture(video_path)

    # Verificar se o vídeo foi aberto corretamente
    if not cap.isOpened():
        print("Erro ao abrir o vídeo.")
        return

    # Obter propriedades do vídeo
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Definir o codec e criar o objeto VideoWriter
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec para MP4
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    # Loop para processar cada frame do vídeo com barra de progresso
    for frame_idx in tqdm(range(total_frames), desc="Processando vídeo"):
        # Ler um frame do vídeo
        ret, frame = cap.read()

        # Se não conseguiu ler o frame (final do vídeo), sair do loop
        if not ret:
            break

        # Converter o frame para RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Processar o frame para detectar a pose
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
        timestamp_ms = int((frame_idx / fps) * 1000) if fps > 0 else frame_idx * 33
        result = pose_landmarker.detect_for_video(mp_image, timestamp_ms)

        # Desenhar as anotações da pose no frame
        if result.pose_landmarks:
            for pose_landmarks in result.pose_landmarks:
                draw_pose(frame, pose_landmarks)

        # Escrever o frame processado no vídeo de saída
        out.write(frame)

    # Liberar a captura de vídeo e fechar todas as janelas
    cap.release()
    out.release()
    pose_landmarker.close()

# Caminho para o vídeo de entrada e saída
script_dir = os.path.dirname(os.path.abspath(__file__))
input_video_path = os.path.join(script_dir, 'Coração.mp4')  # Nome do vídeo de entrada
output_video_path = os.path.join(script_dir, 'output_video_pose.mp4')  # Nome do vídeo de saída

# Processar o vídeo
detect_pose(input_video_path, output_video_path)
