# 💖 Reconhecimento de Ações com MediaPipe

Este diretório tem um pipeline de visão computacional para **detecção de pose** e **contagem de desenhos de coração com os braços** usando **MediaPipe Tasks + OpenCV**.

## 🚀 O que este projeto faz

- Detecta landmarks corporais em vídeo com `PoseLandmarker` (MediaPipe)
- Conta quantas vezes a pessoa faz o gesto de “coração” com os braços
- Salva um vídeo anotado com:
  - esqueleto da pose
  - contador de desenhos de coração

## 📁 Arquivos

- `pose_detection_arm.py` → script principal de contagem de coração
- `pose_detection_video.py` → script de pose sem contagem
- `Coração.mp4` → vídeo de entrada
- `output_video_arm_up.mp4` → saída com contagem de coração
- `output_video_pose.mp4` → saída com pose desenhada
- `pose_landmarker_lite.task` → modelo do MediaPipe (pode ser baixado automaticamente)

## ✅ Pré-requisitos

- Python 3.10+
- Dependências instaladas no ambiente virtual (`.venv`)
- Pacotes principais:
  - `mediapipe`
  - `opencv-python`
  - `tqdm`

Se necessário, na raiz do projeto (`Webcam_CV`):

```bash
pip install -r requirements.txt
```

## ▶️ Como executar

Na raiz do projeto (`Webcam_CV`):

```bash
python "Reconhecimento de Ações e Atividades/pose_detection_arm.py"
```

## 🧠 Como a contagem de coração funciona

O script considera 1 “desenho de coração” quando:

- punho esquerdo cruza para dentro do ombro esquerdo, **e**
- punho direito cruza para dentro do ombro direito

Em termos simples, os dois braços entram numa posição que lembra o gesto de coração.

A contagem só incrementa na **transição** (evita contar vários frames da mesma pose).

## ⚙️ Observações

- O script processa vídeo offline e salva a saída (sem janela `imshow`)
- O modelo `pose_landmarker_lite.task` é buscado automaticamente em:
  - `C:/Users/<seu_usuario>/.mediapipe_models/pose_landmarker_lite.task`
- Se o vídeo não abrir, confira nome/caminho do arquivo de entrada (`Coração.mp4`)

## 🛠️ Dicas rápidas de ajuste

Se quiser deixar a detecção mais rígida ou mais permissiva, ajuste a função `is_heart()` em [pose_detection_arm.py](pose_detection_arm.py).
