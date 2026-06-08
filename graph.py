import streamlit as st
from typing import TypedDict
from langgraph.graph import StateGraph, END
from huggingface_hub import InferenceClient
from gtts import gTTS

HF_TOKEN = st.secrets["HF_TOKEN"]

client = InferenceClient(
    api_key=HF_TOKEN
)


class StoryState(TypedDict):
    topic: str
    category: str
    length: str
    language: str
    story: str
    audio_file: str


def generate_story(state):

    length_map = {
        "Short": 150,
        "Medium": 300,
        "Long": 600
    }

    words = length_map[state["length"]]

    prompt = f"""
Write a {state['category']} story.

Topic: {state['topic']}

Requirements:
- Length: approximately {words} words
- Make it engaging
- Include a clear beginning, challenge, and ending
- Use simple language
"""

    try:

        response = client.chat.completions.create(
            model="meta-llama/Llama-3.1-8B-Instruct",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            max_tokens=1000
        )

        story = response.choices[0].message.content

    except Exception as e:

        story = f"Error generating story: {str(e)}"

    return {
        **state,
        "story": story
    }


def generate_audio(state):

    lang_code = "en"

    if state["language"] == "Hindi":
        lang_code = "hi"

    output_file = "story.mp3"

    tts = gTTS(
        text=state["story"],
        lang=lang_code,
        slow=False
    )

    tts.save(output_file)

    return {
        **state,
        "audio_file": output_file
    }


builder = StateGraph(StoryState)

builder.add_node("generate_story", generate_story)
builder.add_node("generate_audio", generate_audio)

builder.set_entry_point("generate_story")

builder.add_edge("generate_story", "generate_audio")
builder.add_edge("generate_audio", END)

graph = builder.compile()


def run_story_narrator(topic, category, length, language):

    return graph.invoke(
        {
            "topic": topic,
            "category": category,
            "length": length,
            "language": language
        }
    )
