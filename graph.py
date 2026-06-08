import streamlit as st
from typing import TypedDict
from langgraph.graph import StateGraph, END
from huggingface_hub import InferenceClient
from gtts import gTTS
from PIL import Image, ImageDraw

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
    image_file: str


def generate_story(state):

    length_map = {
        "Short": 150,
        "Medium": 300,
        "Long": 600
    }

    words = length_map[state["length"]]

    if state["language"] == "Hindi":

        prompt = f"""
एक रोचक {state['category']} कहानी लिखिए।

विषय: {state['topic']}

निर्देश:
- लगभग {words} शब्द
- स्पष्ट शुरुआत, संघर्ष और अंत
- पूरी कहानी हिंदी में
"""

    else:

        prompt = f"""
Write a {state['category']} story.

Topic: {state['topic']}

Requirements:
- Approximately {words} words
- Clear beginning, challenge and ending
- Write entirely in English
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
            max_tokens=1200
        )

        story = response.choices[0].message.content

    except Exception as e:

        story = f"Error generating story: {str(e)}"

    return {
        **state,
        "story": story
    }


def generate_cover_image(state):

    width = 1024
    height = 1024

    image = Image.new(
        "RGB",
        (width, height),
        color=(20, 30, 60)
    )

    draw = ImageDraw.Draw(image)

    draw.rectangle(
        [(40, 40), (984, 984)],
        outline=(255, 215, 0),
        width=5
    )

    title = state["topic"]
    category = state["category"]

    draw.text(
        (80, 180),
        title,
        fill="white"
    )

    draw.text(
        (80, 350),
        f"{category} Story",
        fill=(255, 215, 0)
    )

    draw.text(
        (80, 800),
        "The Rising Icons",
        fill="white"
    )

    image_path = "cover.png"

    image.save(image_path)

    return {
        **state,
        "image_file": image_path
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
builder.add_node("generate_cover_image", generate_cover_image)
builder.add_node("generate_audio", generate_audio)

builder.set_entry_point("generate_story")

builder.add_edge("generate_story", "generate_cover_image")
builder.add_edge("generate_cover_image", "generate_audio")
builder.add_edge("generate_audio", END)

graph = builder.compile()


def run_story_narrator(
    topic,
    category,
    length,
    language
):

    return graph.invoke(
        {
            "topic": topic,
            "category": category,
            "length": length,
            "language": language
        }
    )
