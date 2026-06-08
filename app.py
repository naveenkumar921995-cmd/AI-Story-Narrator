import streamlit as st
from graph import run_story_narrator

st.set_page_config(
    page_title="AI Story Narrator V3",
    page_icon="🎙️",
    layout="wide"
)

if "history" not in st.session_state:
    st.session_state.history = []

st.title("🎙️ AI Story Narrator V3")
st.caption("Create stories, cover images and audio narration")

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

    st.header("📚 Recent Stories")

    if len(st.session_state.history) == 0:
        st.write("No stories generated yet")

    else:
        for item in reversed(st.session_state.history[-5:]):
            st.write(f"• {item}")

topic = st.text_input(
    "Enter Story Topic",
    placeholder="A boy who started a billion-dollar company"
)

generate = st.button("🚀 Generate Story & Audio")

if generate:

    if topic:

        with st.spinner("Generating story, cover image and audio..."):

            result = run_story_narrator(
                topic,
                category,
                length,
                language
            )

        st.session_state.history.append(topic)

        st.success("Story generated successfully!")

        # Cover Image
        if result.get("image_file"):

            st.subheader("🖼️ Story Cover")

col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.image(
        result["image_file"],
        width=350
    )

        # Story
        st.subheader("📖 Generated Story")

        st.write(result["story"])

        # Audio
        if result.get("audio_file"):

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

st.divider()

st.caption("Built with ❤️ by The Rising Icons")
