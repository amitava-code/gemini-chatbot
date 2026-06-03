
# 🤖 Gemini Chatbot

A sleek, conversational AI chatbot powered by **Google Gemini 2.5 Flash** and built with **Streamlit** — featuring full multi-turn memory so it actually remembers what you said.

---

## ✨ Features

- 💬 **Multi-turn conversations** — full chat history passed on every request
- ⚡ **Gemini 2.5 Flash** — fast, capable, and cutting-edge
- 🧠 **Session memory** — context is preserved across the entire conversation
- 🖥️ **Clean Streamlit UI** — zero-fuss chat interface, ready out of the box
- 🔐 **Secure API key handling** — via `.env` and `python-dotenv`

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/your-username/gemini-chatbot.git
cd gemini-chatbot
```

### 2. Install dependencies

```bash
pip install streamlit google-genai python-dotenv
```

### 3. Set up your API key

Create a `.env` file in the project root:

```env
GEMINI_API=your_google_gemini_api_key_here
```

> Get your key at [Google AI Studio](https://aistudio.google.com/app/apikey)

### 4. Run the app

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
gemini-chatbot/
├── app.py          # Streamlit web chatbot (main UI app)
├── main.py         # Terminal chatbot (practice CLI version, no Streamlit)
├── .gitignore
└── README.md
```

---

## 🔧 How It Works

Each time the user sends a message, the full conversation history is formatted and passed to the Gemini API — giving the model complete context for a coherent, memory-aware response.

```python
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[f"{m['role']}: {m['content']}" for m in st.session_state.messages]
)
```

---

## ⚠️ Important

Never commit your `.env` file. Add it to `.gitignore`:

```
.env
```

---

## 🛠️ Built With

| Tool | Purpose |
|---|---|
| [Streamlit](https://streamlit.io) | UI framework |
| [Google Gemini](https://deepmind.google/technologies/gemini/) | LLM backend |
| [python-dotenv](https://pypi.org/project/python-dotenv/) | Env management |

---

## 👤 Author

**Amitava Biswas**

- GitHub: [@AmitavaBiswas](https://github.com/amitava-code)

---

