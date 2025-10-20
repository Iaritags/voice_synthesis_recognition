# 🗣️ Voice Synthesis & Recognition

Este proyecto implementa un **pipeline completo de procesamiento de voz** en Python:  
convierte texto a audio (**Text-to-Speech**) y audio a texto (**Speech-to-Text**) utilizando librerías locales y de uso libre.  

Funciona sin conexión a internet para la síntesis y con la API gratuita de Google Speech Recognition para la transcripción.  

---

## ✨ Características

- 🔊 **Text → Speech**: usa `pyttsx3` para generar voz a partir de texto.  
- 🧠 **Speech → Text**: usa `SpeechRecognition` para transcribir audios WAV.  
- 🪶 **Normalización de audio**: reescala y limpia WAV con `pydub`.  
- 🖥️ **Interfaz de consola** simple con entrada de texto y opción de grabación.  
- ⚙️ **Compatibilidad con Python 3.13+** (soluciona la falta de `aifc` y `audioop`).  

---

## 🧩 Estructura del proyecto
```
voice_synthesis_recognition/
├─ engines/
│  ├─ speech_synthesizer.py     # Text → Speech
│  └─ speech_recognizer.py      # Speech → Text
├─ services/
│  └─ speech_service.py         # Fachada que unifica síntesis y reconocimiento
├─ utils/
│  └─ audio_utils.py            # Normalización de WAV
├─ main.py                      # Entrada principal (interfaz de consola)
├─ requirements.txt
└─ README.md
```

---

## ⚙️ Instalación

### 1️⃣ Crear y activar entorno virtual
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate
```

### 2️⃣ Instalar dependencias
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 3️⃣ (Windows) Instalar FFmpeg si no está en PATH  
`pydub` lo necesita para leer y exportar audios:
- 🪟 Windows → [Descargar FFmpeg](https://www.gyan.dev/ffmpeg/builds/) y agregar `bin/` al PATH  
- 🐧 Linux → `sudo apt install ffmpeg`  
- 🍎 macOS → `brew install ffmpeg`

---

## 🧠 Uso

```bash
python main.py
```

Ejemplo de interacción:

```
Escribí el texto para convertir a voz: Hola Iara, probando síntesis de voz.
🔊 Reproduciendo y guardando...
✅ Audio: texto.wav normalizado como texto_clean.wav

¿Grabar audio del micrófono y transcribir? (s/n): s
🎙️ Grabando 5 segundos...
📝 Transcripción: hola iara probando síntesis de voz
```

---

## ⚙️ Compatibilidad con Python 3.13+

> **Importante:**  
> `SpeechRecognition 3.10.4` importa `aifc` (y también usa `audioop`),  
> dos módulos de la **librería estándar (stdlib)** que fueron **eliminados a partir de Python 3.13**.  
> Por este motivo, el código original falla en versiones más nuevas del intérprete.  



> ⚠️ Este parche permite usar **WAV → texto** sin problemas.  
> Sin embargo, la captura de micrófono podría no funcionar completamente,  
> ya que `audioop.ratecv` no está implementado en este modo.

Para compatibilidad total (incluido micrófono), se recomienda usar:
- **Python 3.11 o 3.12**

---

## 📦 Dependencias principales
| Librería | Propósito |
|-----------|------------|
| **pyttsx3** | Conversión de texto a voz (offline). |
| **SpeechRecognition** | Reconocimiento de voz (Google Speech API). |
| **pydub** | Manipulación y normalización de audio WAV. |
| **ffmpeg** | Backend requerido por pydub. |

---

## 🧱 Buenas prácticas aplicadas
- Estructura modular por capas (`engines`, `services`, `utils`).  
- Fachada (`SpeechService`) que simplifica el uso de los engines.  
---

## 👩‍💻 Autor
**Iara González Sardi**  
Proyecto académico / práctico — *Procesamiento del Habla*  
📍 Río Grande, Tierra del Fuego – Argentina  
