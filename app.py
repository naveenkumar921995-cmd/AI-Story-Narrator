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

            if result["audio_file"]:

                st.subheader("Audio Narration")

                with open(result["audio_file"], "rb") as audio_file:
                    audio_bytes = audio_file.read()

                st.audio(audio_bytes, format="audio/mp3")

                st.download_button(
                    label="Download Audio",
                    data=audio_bytes,
                    file_name="story.mp3",
                    mime="audio/mpeg"
                )

    else:
        st.warning("Please enter a topic.")
