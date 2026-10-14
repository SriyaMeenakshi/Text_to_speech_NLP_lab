import os
import streamlit as st

from tts_engine import generate


st.set_page_config(
    page_title="Text to Speech System",
    page_icon="🎙️"
)

st.title("🎙️ Text-to-Speech System")

st.write(
    "Convert text into natural speech with different voices, "
    "speed and pitch controls."
)

# Available Microsoft Edge voices
voices = {
    "Female - US English": "en-US-AriaNeural",
    "Male - US English": "en-US-GuyNeural",
    "Female - UK English": "en-GB-SoniaNeural",
    "Male - UK English": "en-GB-RyanNeural",
    "Female - Indian English": "en-IN-NeerjaNeural",
    "Male - Indian English": "en-IN-PrabhatNeural",
}

text = st.text_area(
    "Enter your text",
    height=180,
    placeholder="Type your text here..."
)

voice_name = st.selectbox(
    "Choose Voice",
    list(voices.keys())
)

speed = st.slider(
    "Speech Speed",
    min_value=-50,
    max_value=50,
    value=0,
    step=10
)

pitch = st.slider(
    "Pitch",
    min_value=-50,
    max_value=50,
    value=0,
    step=10
)


if st.button("🔊 Generate Speech", use_container_width=True):

    if not text.strip():
        st.warning("Please enter some text.")

    else:

        os.makedirs("outputs", exist_ok=True)

        output_file = "outputs/generated_speech.mp3"

        rate = f"{speed:+d}%"
        pitch_value = f"{pitch:+d}Hz"

        with st.spinner("Generating speech..."):

            generate(
                text=text,
                voice=voices[voice_name],
                rate=rate,
                pitch=pitch_value,
                output_file=output_file
            )

        st.success("Speech generated successfully!")

        audio_file = open(output_file, "rb")
        audio_bytes = audio_file.read()

        st.audio(audio_bytes, format="audio/mp3")

        st.download_button(
            label="⬇️ Download Audio",
            data=audio_bytes,
            file_name="generated_speech.mp3",
            mime="audio/mpeg",
            use_container_width=True
        )