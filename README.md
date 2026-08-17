# Jarvis-AI

A custom Python voice assistant you run locally on your own machine.
Say the wake word, then a command — Jarvis listens, understands, and talks back.

## Features

- 🎙️ Wake-word activation (default: "jarvis")
- 🗣️ Text-to-speech replies (offline, via `pyttsx3`)
- ⏰ Time and date
- 😂 Random jokes
- 📖 Wikipedia summaries
- 🌦️ Live weather (via OpenWeatherMap)
- 🌐 Open websites (YouTube, Google, GitHub, Gmail, Stack Overflow)
- 🔍 Google search by voice
- 🖥️ Open local apps (Notepad/Calculator) and report system info
- 🧩 Simple command table — add your own commands in a few lines

## Project structure

```
Jarvis-AI/
├── main.py              # Entry point — run this to start Jarvis
├── jarvis/
│   ├── __init__.py
│   ├── assistant.py      # Wake-word loop + command dispatch
│   ├── commands.py        # All command implementations
│   ├── config.py          # Settings, loaded from .env
│   └── speech.py           # Speech-to-text / text-to-speech
├── requirements.txt
├── .env.example
├── .gitignore
└── LICENSE
```

## Setup

1. **Clone your repo** (after uploading, see below) or download this folder.

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate      # Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

   > **Note on PyAudio:** `pyaudio` sometimes fails to install directly via pip.
   > - Windows: `pip install pipwin && pipwin install pyaudio`
   > - macOS: `brew install portaudio` then `pip install pyaudio`
   > - Linux: `sudo apt install portaudio19-dev python3-pyaudio` then `pip install pyaudio`

4. **Configure your settings:**
   ```bash
   cp .env.example .env
   ```
   Then open `.env` and optionally add a free [OpenWeatherMap API key](https://openweathermap.org/api) to enable the weather command. `.env` is git-ignored, so your key never gets committed.

5. **Run Jarvis:**
   ```bash
   python main.py
   ```

## Usage

Once running, Jarvis says it's online. Say the wake word, wait for "Yes?", then say your command:

- "Jarvis" → "what time is it"
- "Jarvis" → "tell me a joke"
- "Jarvis" → "search wikipedia for black holes"
- "Jarvis" → "what's the weather in Tokyo"
- "Jarvis" → "open youtube"
- "Jarvis" → "search google for python tutorials"
- "Jarvis" → "exit"

To skip the wake word entirely (faster for testing on a laptop mic), set `REQUIRE_WAKE_WORD=false` in your `.env`.

## Adding a new command

1. Write a function in `jarvis/commands.py` that takes `text: str` and calls `speak(...)`.
2. Register it in the `COMMANDS` list in `jarvis/assistant.py` with the trigger keyword(s):
   ```python
   (("your keyword",), commands.your_function),
   ```

## Roadmap ideas

- Swap Google's speech API for offline recognition (e.g. Vosk or Whisper)
- Add a GUI (Tkinter or PyQt) as an alternative to the terminal
- Smart home integrations
- Custom wake-word model (Porcupine/Snowboy) instead of keyword matching

## License

MIT — see [LICENSE](LICENSE).
