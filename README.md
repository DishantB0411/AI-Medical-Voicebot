# 🩺 AI Doctor with Vision and Voice

A multimodal AI application that simulates a doctor-patient interaction using voice and image inputs. This Gradio-powered demo allows users to:
- Speak their symptoms or queries via a microphone.
- Upload an image (e.g., skin lesion, X-ray, etc.).
- Receive a concise and realistic diagnosis-like response from a large multimodal language model.
- Hear the AI doctor's response spoken back via text-to-speech.

---

## 🧠 Features

- 🎤 **Voice Input**: Record patient speech and transcribe it using Whisper (via Groq).
- 🖼️ **Image Analysis**: Accept medical images and analyze them using LLaMA-4-Scout via Groq’s multimodal chat API.
- 🩺 **Doctor's AI Reply**: Return a realistic, non-AI-sounding diagnostic response (differential + remedy suggestions).
- 🔊 **Voice Output**: Use ElevenLabs or gTTS to generate a natural-sounding audio response.
- 💻 **Simple UI**: Built with Gradio for an interactive web interface.

---

## 📁 File Structure

```bash
.
├── app.py                     # Main Gradio interface
├── brain_of_the_doctor.py    # Handles image encoding + AI model query
├── voice_of_patient.py       # Records and transcribes patient voice input
├── voice_of_the_doctor.py    # Converts text response to voice
├── .env                      # Stores API keys
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

## 📦 File Overview

### 1. **`app.py` — Main Application Script**

The heart of the app that ties together the voice and image analysis. It handles user inputs, processes them through multiple models, and outputs the result via Gradio.

#### 🧠 Workflow:
1. **Speech-to-Text (STT)**: Captures audio input from the patient and converts it into text using the Groq API (Whisper model).
2. **Image Analysis**: If an image is provided (e.g., medical images), the app analyzes it using the multimodal model (Groq API).
3. **TTS (Text-to-Speech)**: The doctor’s diagnosis is spoken aloud using Google’s TTS (gTTS) or ElevenLabs’ TTS.

#### 🔌 Dependencies:
- `gradio`: For building the web interface.
- `groq`: For handling transcription and image analysis via Groq's API.
- `dotenv`: For managing environment variables.
- `platform` and `subprocess`: For platform-dependent audio playback.
- `pydub`: For audio file conversion.

---

### 2. **`voice_of_patient.py` — Recording and Transcribing Patient's Audio**

This file is responsible for recording the patient's voice input and transcribing it to text. The recorded audio is saved in MP3 format, and transcription is performed using Groq's Whisper model.

#### 🧠 Workflow:
1. **Audio Recording**: The `record_audio` function records the patient's voice input through the microphone. The audio is saved as an MP3 file.
2. **Speech-to-Text**: The `transcribe_with_groq` function sends the recorded audio file to Groq's Whisper STT model for transcription. The transcription is returned as text.

#### 🔌 Dependencies:
- `speech_recognition`: For microphone audio recording.
- `pydub`: For handling audio file conversions.
- `groq`: For transcription via Groq's Whisper model.
- `dotenv`: For managing API keys.

#### ▶️ How to Run:
To use the script, make sure to set up the `.env` file with the `GROQ_API_KEY`. Then:

```bash
python voice_of_patient.py
````

This will trigger the audio recording and transcription process.

---

### 3. **`brain_of_doctor.py` — Image Processing and LLM Interaction**

This file contains functions responsible for processing images (e.g., medical images) and querying the multimodal LLM for a diagnosis. The image is encoded in base64, combined with the text input, and sent to the LLM for analysis.

#### 🧠 Workflow:

1. **Image Encoding**: The `encoded_image` function reads the image file and converts it to a base64-encoded string.
2. **Model Interaction**: The `analyse_img_query` function combines the transcribed text from the patient and the encoded image. The combined query is sent to Groq's multimodal LLM for processing. The model’s response (diagnosis) is returned.

#### 🔌 Dependencies:

* `groq`: For querying the multimodal model.
* `dotenv`: For managing API keys.
* `base64`: For encoding the image into a string.

#### ▶️ How to Run:

Ensure that the `.env` file contains the `GROQ_API_KEY`. Then you can run the functions like this:

```python
encoded_img = encoded_image('path_to_image.jpg')
response = analyse_img_query('Query Text', 'model_name', encoded_img)
print(response)
```

---

### 4. **`voice_of_doctor.py` — Text-to-Speech Conversion for the Doctor**

This file contains functions responsible for converting the AI doctor's textual response into speech. It uses Google’s TTS (gTTS) and ElevenLabs for natural voice generation.

#### 🧠 Workflow:

1. **gTTS (Google Text-to-Speech)**: The `text_to_speech_with_gtts` function converts the text into speech using Google’s TTS service. The audio is saved in MP3 format and converted to WAV for cross-platform playback.
2. **ElevenLabs TTS**: The `text_to_speech_elevenlabs` function uses ElevenLabs’ API for more natural-sounding speech. Audio is saved in MP3 format and converted for playback.
3. **Audio Playback**: After generating the speech, the file is played back to the user using the appropriate command for each operating system (macOS, Windows, Linux).

#### 🔌 Dependencies:

* `gTTS`: For Google’s TTS.
* `elevenlabs`: For ElevenLabs TTS API.
* `pydub`: For audio file format conversion.
* `platform`: For system-specific audio playback handling.
* `subprocess`: For executing system commands to play audio.

#### ▶️ How to Run:

To use the TTS functions:

```python
text_to_speech_with_gtts('Hello, how can I assist you?', 'output.mp3')
text_to_speech_elevenlabs('Hello, how can I assist you?', 'output.mp3')
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/ai-doctor-vision-voice.git
cd ai-doctor-vision-voice
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add API keys in a `.env` file

Create a `.env` file in the root directory with the following content:

```env
GROQ_API_KEY=your_groq_api_key
ELABS_API_KEY=your_elevenlabs_api_key
```

> Get your Groq API key at [https://console.groq.com](https://console.groq.com)
> Get your ElevenLabs API key at [https://elevenlabs.io](https://elevenlabs.io)

---

## ▶️ How to Run

```bash
python app.py
```

This will launch a Gradio interface in your browser where you can:

1. Speak your symptoms.
2. Upload an image.
3. Get an AI-generated doctor's response.
4. Hear it spoken back to you.

---

## 🛠️ Technologies Used

* [Python 3.8+](https://www.python.org/)
* [Gradio](https://www.gradio.app/)
* [Groq API (Whisper & LLaMA-4-Scout)](https://console.groq.com/)
* [ElevenLabs TTS](https://www.elevenlabs.io/)
* [gTTS](https://pypi.org/project/gTTS/)
* [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
* [pydub](https://pypi.org/project/pydub/)

---

## 🙏 Acknowledgements

* Groq for blazing-fast LLM and Whisper inference.
* ElevenLabs for realistic voice synthesis.
* The open-source community for enabling rapid prototyping with audio and image tools.

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).

---

## ✨ Future Enhancements (Ideas)

* Add multilingual support (STT + TTS)
* Enable differential diagnosis visualization
* Add follow-up interaction (dialogue history)
* Integrate with medical knowledge bases

---

## 🧪 Disclaimer

> This project is intended **for educational and research purposes only**. It does not provide real medical diagnosis and should **not** be used as a substitute for professional medical advice.

---
