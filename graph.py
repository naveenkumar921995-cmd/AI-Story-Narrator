import streamlit as st
from typing import TypedDict
from langgraph.graph import StateGraph, END
from huggingface_hub import InferenceClient

HF_TOKEN = st.secrets["HF_TOKEN"]

client = InferenceClient(
    api_key=HF_TOKEN
)


class StoryState(TypedDict):
    topic: str
    story: str
    audio_file: str


def generate_story(state):

    prompt = f"""
Write an engaging short story in about 250 words on:
{state['topic']}
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
            max_tokens=400
        )

        story = response.choices[0].message.content

    except Exception as e:
        story = f"Error from Hugging Face: {str(e)}"

    return {
        **state,
        "story": story
    }


def generate_audio(state):

    return {
        **state,
        "audio_file": ""
    }


builder = StateGraph(StoryState)

builder.add_node("generate_story", generate_story)
builder.add_node("generate_audio", generate_audio)

builder.set_entry_point("generate_story")

builder.add_edge("generate_story", "generate_audio")
builder.add_edge("generate_audio", END)

graph = builder.compile()


def run_story_narrator(topic):

    return graph.invoke(
        {
            "topic": topic
        }
    )
