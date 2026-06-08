import streamlit as st
from graph import run_story_narrator

st.set_page_config(
    page_title="AI Story Narrator",
    page_icon="🎙️",
    layout="wide"
)

if "history" not in st.session_state:
    st.session_state.history = []

st.title("🎙️ AI Story Narrator")
st.caption("The Rising Icons")

with st.sidebar:

    st.header("Story Settings")

    category = st.selectbox(
        "Category",
        [
            "Entrepreneur",
            "Motivational",
            "Adventure",
            "Fantasy",
            "Sci-Fi",
            "Historical",
            "Kids"
        ]
    )

    length = st.selectbox(
        "Length",
        [
            "Short",
            "Medium",
            "Long"
        ]
    )

    language = st.selectbox(
        "Language",
        [
            "English",
            "Hindi"
        ]
    )

    st.divider()

    st.subheader("Recent Stories")

    if st.session_state.history:

        for item in reversed(st.session_state.history[-5:]):
            st.write(f"• {item}")

topic = st.text_input(
    "Enter Story Topic",
    placeholder="Ratan Tata Success Story"
)

if st.button("Generate Story & Audio"):

    if topic:

        with st.spinner(
            "Generating story, AI cover image and audio..."
        ):

            result = run_story_narrator(
                topic,
                category,
                length,
                language
            )

        st.session_state.history.append(topic)

        st.success("Story generated successfully!")

        if result.get("image_file"):

            st.subheader("🖼️ AI Generated Cover")

            st.image(
                result["image_file"],
                use_container_width=True
            )

        st.subheader("📖 Story")

        st.write(result["story"])

        if result.get("audio_file"):

            with open(
                result["audio_file"],
                "rb"
            ) as audio_file:

                audio_bytes = audio_file.read()

            st.subheader("🎧 Narration")

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

        st.warning(
            "Please enter a story topic."
        )

st.divider()

st.caption("Built by The Rising Icons")
