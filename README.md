# 🖐 Arabic Sign Language Bidirectional Translator

A **bidirectional translator for Arabic Sign Language**, converting **text/speech → sign** and **sign → speech** in real-time using your webcam.

---

## ✨ Features

### 1️⃣ Text/Speech → Sign
- Type a word or sentence manually or **use your voice**.  
- Displays **animated GIFs** for words in Arabic.  
- Supported words include: `"mom"`, `"Alhamdulillah"`, `"angry"`, `"house"`, `"how are you"`, and more.  
- GIFs are fetched **directly from online URLs**.  

---

### 2️⃣ Sign → Speech
- Real-time hand sign recognition via **webcam**.  
- Supports three model types:
  - **Numbers** (0–10)
  - **Arabic letters**
  - **Words**
- Uses **MediaPipe Hands** for hand tracking.  
- Recognizes repeated signs and **speaks them aloud in Arabic**.  
- Displays **shaped Arabic text** on screen using `arabic_reshaper` + `python-bidi`.  

---

### 3️⃣ Controls
- Start/stop the camera 🎥  
- Enable/disable speech 🔊  
- Toggle between right/left hand ✋  
- Clear recognized text 🧹  

---

## 🛠 Dependencies

Python 3.8+ and the following libraries:

```bash
pip install customtkinter pillow requests SpeechRecognition opencv-python mediapipe numpy arabic-reshaper python-bidi gTTS pygame
```

---
## 🚀 How to Use
Run the program:
python main.py
Text/Speech → Sign
Go to "Text → Sign" tab.
Type a word and click "Show GIF", or click "Click to Record" to use speech input.
The corresponding GIF will appear.
Sign → Speech
Go to "Sign → Speech" tab.
Select Numbers, Letters, or Words.
The webcam will detect your hand signs.
Recognized signs are:
Spoken aloud in Arabic
Displayed as text
Use the Clear Text button to reset.
Toggle hand using Use Left/Right Hand button.

---

## 💡 Notes
Audio is cached in audio_cache/ for faster playback.
Left-hand recognition mirrors coordinates for accuracy.
Minimum interval prevents repeated audio output.
Internet is required to display GIFs.
