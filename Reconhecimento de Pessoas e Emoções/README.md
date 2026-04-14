# 😎 Reconhecimento de Pessoas e Emoções

Projeto simples e divertido pra:
- 🧑‍🤝‍🧑 **Reconhecer pessoas** com `face_recognition` (usando fotos em `images/`)
- 😀 **Detectar emoção dominante** com `DeepFace`
- 🎬 **Gerar um vídeo final** com nome + emoção na tela

## 📁 O que tem aqui

- `deepface_v2.py` → script principal
- `Emoções.mp4` → vídeo de entrada
- `output_video_recognize.mp4` → vídeo de saída

## ✅ Antes de rodar

- Python 3.10+ 🐍
- Dependências instaladas
- Pasta `images/` na raiz do projeto (`Webcam_CV/images`) com as fotos das pessoas

> ℹ️ Dica: no script atual, o nome vem do arquivo removendo o último caractere.
> Exemplo: `joao1.jpg` vira `joao`.

## 🛠️ Instalação

Na raiz do projeto (`Webcam_CV`), roda:

```bash
pip install -r requirements.txt
pip install git+https://github.com/ageitgey/face_recognition_models
```

Se aparecer erro com `pkg_resources`, manda esse aqui:

```bash
pip install "setuptools<81"
```

## ▶️ Como executar

Rode a partir da raiz `Webcam_CV` (pra encontrar a pasta `images/` certinho):

```bash
python "Reconhecimento de Pessoas e Emoções/deepface_v2.py"
```

## 🔄 O que o script faz

1. 📸 Carrega as fotos em `images/` e cria os encodings faciais.
2. 🎞️ Lê o vídeo `Emoções.mp4` frame a frame.
3. 😀 Detecta emoções com `DeepFace.analyze(...)`.
4. 🧠 Compara as faces com as pessoas conhecidas.
5. 🏷️ Desenha caixa + emoção + nome no frame.
6. 💾 Salva o resultado em `output_video_recognize.mp4`.

## 💡 Observações rápidas

- ⏳ Pode ficar lento na CPU (análise de emoção em todos os frames).
- 🙈 Se não reconhecer, vai mostrar **Desconhecido**.
- 💡 Pra melhorar resultado: fotos nítidas, boa luz e uma face por imagem.
