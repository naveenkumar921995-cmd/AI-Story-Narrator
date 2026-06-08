# 🎙️ AI Story Narrator

An AI-powered storytelling application that generates engaging stories, creates AI-generated cover images, and produces narrated audio from a single topic input.

Built using Streamlit, LangGraph, Hugging Face Inference API, and Google Text-to-Speech (gTTS).

---

## 🚀 Features

### 📖 AI Story Generation

Generate unique stories based on a user-provided topic.

* Entrepreneur Stories
* Motivational Stories
* Adventure Stories
* Fantasy Stories
* Historical Stories
* Kids Stories
* Sci-Fi Stories

### 🌍 Multi-Language Support

Generate stories and narration in:

* English
* Hindi

### 🖼️ AI Cover Image Generation

Automatically creates a professional AI-generated book cover image for every story using Hugging Face image generation models.

### 🎧 Audio Narration

Converts generated stories into realistic audio narration using Google Text-to-Speech (gTTS).

### 📥 Audio Download

Users can download generated narration in MP3 format.

### 📚 Story History

Recently generated stories are stored during the session for quick access.

---

# 🛠️ Tech Stack

## Frontend

### Streamlit

Used for:

* User Interface
* Forms and Inputs
* Story Display
* Image Display
* Audio Player
* Download Buttons
* Session Management

---

## Backend

### Python

Core programming language used for:

* Application logic
* AI workflow orchestration
* Data processing
* File handling

### LangGraph

Used for workflow automation.

Workflow:

Topic Input
↓
Story Generation
↓
AI Cover Image Generation
↓
Audio Narration
↓
Final Output

---

# 🤖 AI Models & Services

## Hugging Face Inference API

Used for:

### Story Generation

Model:

meta-llama/Llama-3.1-8B-Instruct

Capabilities:

* Creative Writing
* Story Generation
* Multi-language Content Generation

---

### Image Generation

Model:

black-forest-labs/FLUX.1-schnell

Capabilities:

* AI Cover Art Creation
* Book Cover Illustration
* High-Quality Image Generation

---

## Google Text-to-Speech (gTTS)

Used for:

* English Narration
* Hindi Narration
* MP3 Audio Generation

---

# 📂 Project Structure

```bash
AI-Story-Narrator/
│
├── app.py
├── graph.py
├── requirements.txt
├── README.md
│
└── generated_files/
```

### app.py

Handles:

* Frontend UI
* User Inputs
* Displaying Stories
* Displaying Images
* Playing Audio
* Download Functionality

### graph.py

Handles:

* LangGraph Workflow
* Story Generation
* AI Cover Image Generation
* Audio Generation

### requirements.txt

Contains project dependencies.

---

# 🔄 Application Workflow

1. User enters a story topic.
2. User selects category.
3. User selects story length.
4. User selects language.
5. AI generates a story.
6. AI creates a cover image.
7. Audio narration is generated.
8. Results are displayed.
9. Audio can be downloaded.

---

# 💡 Skills Demonstrated

### Artificial Intelligence

* Generative AI
* Prompt Engineering
* AI Content Generation
* AI Image Generation

### Python Development

* Python Programming
* API Integration
* File Management
* Error Handling

### AI Frameworks

* LangGraph
* Hugging Face Hub

### Frontend Development

* Streamlit UI
* Interactive Dashboards

### Backend Development

* Workflow Automation
* AI Pipeline Design

### Cloud Deployment

* GitHub
* Streamlit Cloud

---

# 🌐 Deployment

The application is deployed using:

* GitHub Repository
* Streamlit Cloud

---

# Future Improvements

* Multiple Voice Options
* PDF Story Export
* User Authentication
* Story Sharing
* Story Library
* Custom Cover Styles
* Multi-language Expansion
* AI Video Narration

---

# Author

### Naveen Kumar

Founder – The Rising Icons

Building AI-powered applications and digital products focused on storytelling, entrepreneurship, and productivity.

---

⭐ If you found this project useful, please consider giving the repository a star.
