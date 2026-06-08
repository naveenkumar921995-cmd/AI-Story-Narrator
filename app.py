import streamlit as st
import huggingface_hub

st.write("Hugging Face Hub Version:")
st.write(huggingface_hub.__version__)
from graph import run_story_narrator

st.set_page_config(
    page_title="AI Story Narrator V2",
    page_icon="🎙️",
    layout="wide"
)

if "history" not in st.session_state:
    st.session_state.history = []

st.title("🎙️ AI Story Narrator V2")
st.caption("Create stories and listen to AI narration")

with st.sidebar:

    st.header("⚙️ Story Settings")

    category = st.selectbox(
        "Story Category",
        [
            "Entrepreneur",
            "Motivational",
            "Adventure",
            "Fantasy",
            "Sci-Fi",
            "Historical",
            "Kids Story"
        ]
    )

    length = st.selectbox(
        "Story Length",
        [
            "Short",
            "Medium",
            "Long"
        ]
    )

    language = st.selectbox(
        "Narration Language",
        [
            "English",
            "Hindi"
        ]
    )

    st.divider()

    st.header("📚 Story History")

    if len(st.session_state.history) == 0:
        st.write("No stories generated yet")

    for item in reversed(st.session_state.history[-5:]):
        st.write("• " + item)

topic = st.text_input(
    "Enter Story Topic",
    placeholder="A boy who started a billion-dollar company"
)

generate = st.button("Generate Story & Audio")

if generate:

    if topic:

        with st.spinner("Generating..."):

            result = run_story_narrator(
                topic,
                category,
                length,
                language
            )

        st.session_state.history.append(topic)

        st.success("Story generated successfully")

        st.subheader("📖 Generated Story")

        st.write(result["story"])

        with open(result["audio_file"], "rb") as audio_file:

            audio_bytes = audio_file.read()

        st.subheader("🎧 Audio Narration")

        st.audio(
            audio_bytes,
            format="audio/mp3"
        )

        st.download_button(
            label="⬇️ Download Audio",
            data=audio_bytes,
            file_name="story.mp3",
            mime="audio/mpeg"
        )

    else:

        st.warning("Please enter a story topic.")
