# Compose

A small Flask app that drafts blog posts on any topic. You type a topic,
pick an angle and a voice as chips, and it returns a Markdown draft shown
in a clean glass-card UI with a gradient backdrop.

## Project structure

```
roadmap_AI/
├── templates/
│   └── index.html      # UI (notebook: prompt page + draft page)
├── .env                # GROQ_API_KEY lives here (not committed)
├── .gitignore
├── app.py              # Flask routes + Groq call
├── README.md
└── requirements.txt
```

## Tech stack

- **Backend:** Python, Flask
- **AI/LLM:** Groq API
- **Frontend:** HTML, CSS, JavaScript
- **Environment management:** python-dotenv

## Setup

1. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate      # Windows: venv\Scripts\activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Add your Groq API key to `.env`:

   ```
   GROQ_API_KEY=your_actual_key_here
   ```

   Get a key at https://console.groq.com/keys.

4. Run the app:

   ```bash
   python app.py
   ```

5. Open http://127.0.0.1:5000 in your browser.

## How it works

- `GET /` renders `templates/index.html`.
- `POST /generate` accepts JSON `{ topic, angle, tone }`, builds a prompt,
  calls the Groq chat completions API (`llama-3.3-70b-versatile` by
  default), and returns `{ draft, word_count }` as Markdown.
- The frontend renders that Markdown as a styled article inside a glass
  card, with a voice tag, a live word count, and **Copy text** /
  **Download .md** actions.

## Notes

- Swap `MODEL` in `app.py` for any other model available on your Groq
  account.
- Drafts are capped at 1000 tokens (roughly 600–750 words) — a solid first
  draft, not a finished long-form post. Raise `max_tokens` in `app.py` if you
  want longer output.
