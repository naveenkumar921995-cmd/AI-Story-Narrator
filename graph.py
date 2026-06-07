import os
from typing import TypedDict
from langgraph.graph import StateGraph, END
from huggingface_hub import InferenceClient

HF_TOKEN = os.environ["HF_TOKEN"]

client = InferenceClient(
provider="hf-inference",
api_key=HF_TOKEN
)

class StoryState(TypedDict):
topic: str
story: str
audio_file: str

def generate_story(state):
prompt = f"""
Write an engaging short story in 250 words about:
{state['topic']}
"""

```
response = client.chat.completions.create(
    model="Qwen/Qwen3-32B",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

story = response.choices[0].message.content

return {
    **state,
    "story": story
}
```

def generate_audio(state):

```
audio = client.text_to_speech(
    state["story"],
    model="espnet/kan-bayashi_ljspeech_vits"
)

output_file = "story.wav"

with open(output_file, "wb") as f:
    f.write(audio)

return {
    **state,
    "audio_file": output_file
}
```

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
