# 😍 BeautyScope — O Tribunal de Rostos Mais Imparcial da Galáxia

> *"A beleza está nos olhos de quem vê... mas agora está também na distância euclidiana entre encodings de 128 dimensões."*

---

## O que é isso?

Um sistema de **classificação facial em tempo real** que aponta a câmera para o seu rosto e te diz, sem pestanejar, se você é um **Homem lindo** ou um **Homem feio** — baseado em ciência, matemática e um conjunto de fotos que alguém escolheu a dedo.

Não é reconhecimento de pessoa. É reconhecimento de **destino**.

---

## Como a mágica (ou tragédia) acontece

O sistema **não compara você com um indivíduo específico**. Ele compara seu rosto com dois grupos de referência:

| Grupo | Fotos na base | Label exibido |
|---|---|---|
| Lindos | 14 imagens | `Homem lindo` |
| Feios | 7 imagens | `Homem feio` |

Para cada rosto detectado na webcam, o algoritmo calcula a **distância euclidiana** entre seu encoding facial e todos os encodings da base. O grupo mais próximo vence. Sem apelação. Sem recurso. Sem advogado.

```
📷 Webcam captura seu rosto
        ↓
🧠 dlib gera 128 pontos característicos do seu rosto
        ↓
📐 Calcula distância para cada foto da base
        ↓
     🏆 Menor distância vence
        ↓
   😍 "Homem lindo"       😬 "Homem feio"
```

---

## Estrutura da Base de Dados

```
📁 images/
   ├── Homem lindo (1).jpg
   ├── Homem lindo (2).jpg
   ├── ...
   ├── Homem lindo (14).jpg   ← 14 exemplares do padrão de beleza
   ├── Homem feio (1).jpg
   ├── Homem feio (2).jpg
   ├── ...
   └── Homem feio (7).jpg     ← 7 representantes do outro grupo
```

> **Detalhe técnico:** o código usa os **primeiros 11 caracteres** do nome do arquivo como label (`filename[:11]`). `"Homem lindo"` tem exatamente 11 caracteres. `"Homem feio "` tem 11 com espaço. Coincidência? Não.

---

## Instalação

### Pré-requisitos
- Python 3.8+
- Uma webcam (e coragem)
- Paciência para instalar o `dlib`

```bash
pip install -r requirements.txt
```

> **Aviso existencial:** a instalação do `dlib` pode demorar alguns minutos. Use esse tempo para se preparar emocionalmente para o resultado.

---

## Como usar

```bash
python facial_recognition.py
```

Aponte a câmera para o seu rosto e aguarde o veredicto. O sistema exibirá um retângulo vermelho ao redor do seu rosto com o resultado impresso em branco.

Para sair, pressione `q`. O resultado, infelizmente, não some com a janela.

---

## Stack Tecnológica

| Biblioteca | Versão | Papel |
|---|---|---|
| `opencv-python` | 4.13 | Captura de vídeo e renderização do veredicto |
| `face_recognition` | 1.3.0 | API de reconhecimento facial de alto nível |
| `dlib` | 20.0.1 | Geração dos 128 encodings faciais |
| `numpy` | 2.4.4 | Cálculo das distâncias euclidianas |
| `Pillow` | 12.2.0 | Leitura das imagens da base |

---

## Limitações (leia antes de chorar)

- **O resultado é relativo ao dataset** — se a base tiver fotos ruins dos "lindos", o padrão cai junto.
- **Iluminação** afeta os encodings. Com luz ruim, até o Brad Pitt pode perder.
- **Ângulo do rosto** importa — olha direito pra câmera.
- **A base tem 14 lindos e 7 feios** — há duas vezes mais chances de ser classificado como lindo. Aproveite.
- **Não há empate** — o algoritmo sempre escolhe o grupo mais próximo. A neutralidade não existe aqui.

---

## FAQ

**P: O resultado é científico?**  
R: É matemático. Científico já é forçar a barra.

**P: Posso adicionar minhas próprias fotos para "calibrar" o sistema?**  
R: Sim. Coloca na pasta `images/` com o nome começando por `Homem lindo` ou `Homem feio`. O sistema aprende na hora que você rodar de novo.

**P: E se eu for uma mulher?**  
R: O sistema vai classificar assim mesmo. A IA não discrimina gênero — só aparência.

**P: Meu colega foi classificado como "Homem feio". Posso mostrar pra ele?**  
R: Tecnicamente sim. Profissionalmente, avalie o risco.

**P: O sistema erra?**  
R: O sistema calcula. Quem erra é o dataset.

---

## Contribuindo

PRs são bem-vindos. Sugestões de melhoria:

- [ ] Adicionar categoria "Homem médio" para os indecisos
- [ ] Exibir a porcentagem de certeza do veredicto
- [ ] Suporte a múltiplos rostos simultâneos com placar comparativo
- [ ] Histórico de classificações com gráfico de barras (para os masoquistas)

---

## Licença

MIT — use como quiser. Só não nos culpe pelo resultado.

---

*Feito com OpenCV, dlib, face_recognition, numpy e uma total ausência de responsabilidade afetiva.*
