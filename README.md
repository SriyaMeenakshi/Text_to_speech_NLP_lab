# 🎙️ Text-to-Speech System

A simple, interactive **Text-to-Speech (TTS) web application** built using Python and Streamlit. It converts written text into speech and allows users to select different voices, adjust speech speed and pitch, listen to the generated audio, and download it as an MP3 file.

## ✨ Features

- 📝 **Text Input:** Enter or paste text to convert into speech.
- 🗣️ **Multiple Voices:** Choose from six configured English voices.
- 🌎 **Regional Accents:** Supports US English, UK English, and Indian English voice options.
- ⚡ **Speech Speed Control:** Adjust the speed of the generated speech.
- 🎚️ **Pitch Control:** Customize the pitch of the voice.
- 🔊 **Audio Playback:** Listen to the generated speech directly in the browser.
- 📥 **Download Audio:** Download the generated speech as an MP3 file.
- ✅ **Input Validation:** Displays a warning when the text input is empty.
- 🌐 **Interactive Web Interface:** User-friendly interface developed using Streamlit.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web application interface |
| Edge TTS | Text-to-speech generation |
| asyncio | Asynchronous speech generation |
| HTML5 Audio (via Streamlit) | Audio playback in the browser |

## 🗣️ Available Voices

The application provides the following voice options:

| Voice Option | Voice Identifier |
|---|---|
| Female - US English | `en-US-AriaNeural` |
| Male - US English | `en-US-GuyNeural` |
| Female - UK English | `en-GB-SoniaNeural` |
| Male - UK English | `en-GB-RyanNeural` |
| Female - Indian English | `en-IN-NeerjaNeural` |
| Male - Indian English | `en-IN-PrabhatNeural` |

## 📂 Project Structure

```text
Text-to-Speech-System/
│
├── app.py
├── tts_engine.py
├── text_preprocessing.py
├── requirements.txt
├── README.md
│
└── outputs/
    └── generated_speech.mp3
```

**File descriptions:**

- `app.py` — Creates the Streamlit interface, handles user input, provides voice and audio settings, and displays the generated audio.
- `tts_engine.py` — Handles speech generation using the Edge TTS library.
- `text_preprocessing.py` — Included in the project, but currently duplicates the speech-generation module and is not imported by the main application.
- `requirements.txt` — Lists the Python packages required to run the application.
- `outputs/` — Stores the generated MP3 audio file.

## ⚙️ Installation and Setup

### Prerequisites

Make sure you have the following installed:

- Python 3
- pip (Python package installer)
- A modern web browser
- An active internet connection

**Note:** The application uses an online speech service, so an internet connection is required to generate speech. A dedicated GPU is not required.

### Step 1: Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

Navigate to the project directory:

```bash
cd Text-to-Speech-System
```

Replace `<YOUR_GITHUB_REPOSITORY_URL>` with your actual GitHub repository URL.

### Step 2: Create a Virtual Environment (Recommended)

```bash
python -m venv .venv
```

Activate the environment on Windows:

```bash
.venv\Scripts\activate
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

### Step 3: Install Dependencies

Create a `requirements.txt` file containing:

```text
streamlit
edge-tts
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

### Step 4: Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

Open the local URL displayed in the terminal. By default, Streamlit commonly uses:

```text
http://localhost:8501
```

## 🚀 How to Use

1. Launch the application in your browser.
2. Enter or paste the text you want to convert into speech.
3. Select your preferred voice.
4. Adjust the speech speed using the slider.
5. Adjust the pitch using the pitch slider.
6. Click **Generate Speech**.
7. Wait for the application to generate the audio.
8. Listen to the generated speech using the built-in audio player.
9. Click **Download Audio** to download the MP3 file.

## 🔄 System Workflow

```text
       User Enters Text
              |
              v
       Select Voice
              |
              v
   Adjust Speed and Pitch
              |
              v
      Validate Input
              |
              v
    Edge TTS Speech Service
              |
              v
     Generate MP3 Audio
              |
              v
      Save Generated File
              |
              v
    Play Audio / Download
```

## 💡 Applications

- **Education:** Convert study notes and learning materials into audio.
- **Accessibility:** Help users who prefer listening to written content.
- **Language Learning:** Listen to English text using different regional accents.
- **Content Consumption:** Listen to paragraphs and articles instead of reading them.
- **Voice-enabled Applications:** Serve as a foundation for speech-based interfaces.

## ⚠️ Limitations

- Speech generation requires an active internet connection.
- Voice availability and behavior depend on the external speech service.
- The application currently supports only the configured English voice options.
- Generated audio is saved to a fixed filename, `outputs/generated_speech.mp3`, so a later generation can overwrite the previous file.
- Custom model training and offline speech synthesis are not included.

## 🔮 Future Enhancements

- Add support for more languages and voice options.
- Implement text preprocessing and normalization.
- Support long documents through text chunking.
- Allow users to choose custom output filenames.
- Add improved error handling for network and service failures.
- Provide an offline text-to-speech option.
- Add a history of previously generated audio files.

## 🎓 Project Information

**Project Title:** Text-to-Speech System  
**Domain:** Natural Language Processing (NLP)  
**Project Type:** Web Application  
**Programming Language:** Python  
**Interface Framework:** Streamlit  

Developed as part of a **Natural Language Processing Laboratory project**.

## 📚 References

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Edge TTS GitHub Repository](https://github.com/rany2/edge-tts)
- [Python asyncio Documentation](https://docs.python.org/3/library/asyncio.html)

---

⭐ If you find this project useful, consider giving the repository a star!
