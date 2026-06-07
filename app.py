import streamlit as st
from graph import run_story_narrator

st.set_page_config(
    page_title="AI Story Narrator",
    page_icon="🎙️",
    layout="centered"
)

st.title("🎙️ AI Story Narrator")
st.write("Generate AI stories and listen to them as audio.")

topic = st.text_input(
    "Enter a story topic",
    placeholder="A boy who started a billion-dollar company"
)

if st.button("Generate Story & Audio"):

    if topic:

        with st.spinner("Generating story and audio..."):

            result = run_story_narrator(topic)

            st.subheader("Generated Story")
            st.write(result["story"])

            st.subheader("Audio Narration")
            st.audio(result["audio_file"])

            with open(result["audio_file"], "rb") as file:
                st.download_button(
                    "Download Audio",
                    file,
                    file_name="story.wav"
                )

    else:
        st.warning("Please enter a topic.")
