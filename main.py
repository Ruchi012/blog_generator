# # import os

# # from dotenv import load_dotenv
# # from flask import Flask, jsonify, render_template, request
# # from groq import Groq
# # import logging
# # import traceback

# # load_dotenv()

# # # logging
# # logging.basicConfig(level=logging.INFO)
# # logger = logging.getLogger(__name__)

# # app = Flask(__name__)

# # # groq_api_key = os.environ.get("GROQ_API_KEY")
# # # client = Groq(api_key=groq_api_key) if groq_api_key else None

# # API_KEY = os.environ.get("GROQ_API_KEY")
# # if not API_KEY:
# #     logger.error("GROQ_API_KEY not set. Make sure .env exists and load_dotenv() runs from the project root.")
# #     raise ValueError("GROQ_API_KEY environment variable not set")

# # # initialize Groq client
# # try:
# #     client = Groq(api_key=API_KEY)
# #     logger.info("✅ Groq client initialized successfully")
# # except Exception as e:
# #     logger.exception("Failed to initialize Groq client")
# #     client = None

# # # Any current Groq-hosted chat model works here.
# # MODEL = [
# #     "llama-3.1-8b-instant",
# # "llama-3.3-70b-versatile"
# # ]


# # def build_prompt(topic: str, audience: str, tone: str, focus: str) -> str:
# #     return f"""Write a complete, publish-ready blog post about the following AI roadmap.

# # Topic: {topic}
# # This is {focus}.
# # Target reader: {audience}.
# # Tone: {tone}.

# # Requirements:
# # - Start with a single H1 title (# Title) that is specific and not generic.
# # - Open with a short, punchy hook paragraph (2-3 sentences).
# # - Include 3-5 sections with H2 subheadings (## Section) that lay out the roadmap's
# #   phases, priorities, or milestones.
# # - Use plain, concrete language; avoid buzzword soup.
# # - Close with a short "What this means" or takeaway section.
# # - Format the whole thing in Markdown.
# # - Keep it tight and complete within the space you have — do not leave sections
# #   unfinished."""


# # @app.route("/")
# # def index():
# #     return render_template("index.html")

# # @app.route('/test_groq', methods=['GET'])
# # def test_groq():
# #     if not client:
# #         return jsonify({'ok': False, 'error': 'client not initialized'}), 500
# #     try:
# #         model = MODEL[0]
# #         logger.info("Testing Groq with model: %s", model)
# #         resp = client.chat.completions.create(
# #             model=model,
# #             messages=[
# #                 {"role": "system", "content": "You are a helpful assistant."},
# #                 {"role": "user", "content": "Say 'OK' in one word."}
# #             ],
# #             temperature=0.0,
# #             max_tokens=8
# #         )
# #         text = resp.choices[0].message.content
# #         return jsonify({'ok': True, 'model': model, 'response': text})
# #     except Exception as e:
# #         logger.exception("Test request failed")
# #         return jsonify({'ok': False, 'error': str(e), 'traceback': traceback.format_exc()}), 500


# # @app.route("/generate", methods=["POST"])
# # def generate():
# #     if client is None:
# #         return jsonify({"error": "GROQ_API_KEY is not set. Add it to your .env file."}), 500

# #     data = request.get_json(silent=True) or {}
# #     topic = (data.get("topic") or "").strip()
# #     audience = data.get("audience") or "a general tech-curious audience"
# #     tone = data.get("tone") or "confident and visionary"
# #     focus = data.get("focus") or "a product roadmap"

# #     if not topic:
# #         return jsonify({"error": "Add a roadmap topic before drafting."}), 400

# #     prompt = build_prompt(topic, audience, tone, focus)

# #     try:
# #         completion = client.chat.completions.create(
# #             model=MODEL,
# #             messages=[{"role": "user", "content": prompt}],
# #             max_tokens=1000,
# #             temperature=0.7,
# #         )
# #         text = (completion.choices[0].message.content or "").strip()
# #     except Exception as exc:  # surfaced to the UI as a draft failure
# #         return jsonify({"error": str(exc)}), 502

# #     if not text:
# #         return jsonify({"error": "No draft text returned. Try again."}), 502

# #     word_count = len(text.split())
# #     return jsonify({"draft": text, "word_count": word_count})


# # if __name__ == "__main__":
# #     app.run(debug=True)

# import os

# from dotenv import load_dotenv
# from flask import Flask, jsonify, render_template, request
# from groq import Groq

# load_dotenv()

# app = Flask(__name__)

# groq_api_key = os.environ.get("GROQ_API_KEY")
# client = Groq(api_key=groq_api_key) if groq_api_key else None

# # Any current Groq-hosted chat model works here.
# MODEL = "llama-3.3-70b-versatile"


# def build_prompt(topic: str, audience: str, tone: str, focus: str) -> str:
#     return f"""Write a complete, publish-ready blog post about the following AI roadmap.

# Topic: {topic}
# This is {focus}.
# Target reader: {audience}.
# Tone: {tone}.

# Requirements:
# - Start with a single H1 title (# Title) that is specific and not generic.
# - Open with a short, punchy hook paragraph (2-3 sentences).
# - Include 3-5 sections with H2 subheadings (## Section) that lay out the roadmap's
#   phases, priorities, or milestones.
# - Use plain, concrete language; avoid buzzword soup.
# - Close with a short "What this means" or takeaway section.
# - Format the whole thing in Markdown.
# - Keep it tight and complete within the space you have — do not leave sections
#   unfinished."""


# @app.route("/")
# def index():
#     return render_template("index.html")


# @app.route("/generate", methods=["POST"])
# def generate():
#     if client is None:
#         return jsonify({"error": "GROQ_API_KEY is not set. Add it to your .env file."}), 500

#     data = request.get_json(silent=True) or {}
#     topic = (data.get("topic") or "").strip()
#     audience = data.get("audience") or "a general tech-curious audience"
#     tone = data.get("tone") or "confident and visionary"
#     focus = data.get("focus") or "a product roadmap"

#     if not topic:
#         return jsonify({"error": "Add a roadmap topic before drafting."}), 400

#     prompt = build_prompt(topic, audience, tone, focus)

#     try:
#         completion = client.chat.completions.create(
#             model=MODEL,
#             messages=[{"role": "user", "content": prompt}],
#             max_tokens=1000,
#             temperature=0.7,
#         )
#         text = (completion.choices[0].message.content or "").strip()
#     except Exception as exc:  # surfaced to the UI as a draft failure
#         return jsonify({"error": str(exc)}), 502

#     if not text:
#         return jsonify({"error": "No draft text returned. Try again."}), 502

#     word_count = len(text.split())
#     return jsonify({"draft": text, "word_count": word_count})


# if __name__ == "__main__":
#     app.run(debug=True)

import os

from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request
from groq import Groq

load_dotenv()

app = Flask(__name__)

groq_api_key = os.environ.get("GROQ_API_KEY")
client = Groq(api_key=groq_api_key) if groq_api_key else None

# Any current Groq-hosted chat model works here.
MODEL = "llama-3.3-70b-versatile"


def build_prompt(topic: str, tone: str, angle: str) -> str:
    return f"""Write a complete, publish-ready blog post.

Topic: {topic}
Angle: {angle}
Tone: {tone}

Requirements:
- Start with a single H1 title (# Title) that is specific and not generic.
- Open with a short, punchy hook paragraph (2-3 sentences) that earns the read.
- Include 3-5 sections with H2 subheadings (## Section) that develop the idea
  in a clear order.
- Use plain, concrete language and real examples; avoid buzzword soup and
  empty filler sentences.
- Close with a short, satisfying wrap-up — a takeaway, a call to action, or a
  final thought, whichever fits the angle.
- Format the whole thing in Markdown.
- Keep it tight and complete within the space you have — do not leave
  sections unfinished."""


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    if client is None:
        return jsonify({"error": "GROQ_API_KEY is not set. Add it to your .env file."}), 500

    data = request.get_json(silent=True) or {}
    topic = (data.get("topic") or "").strip()
    tone = data.get("tone") or "warm and personal"
    angle = data.get("angle") or "an explainer that unpacks a concept"

    if not topic:
        return jsonify({"error": "Add a topic before drafting."}), 400

    prompt = build_prompt(topic, tone, angle)

    try:
        completion = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000,
            temperature=0.7,
        )
        text = (completion.choices[0].message.content or "").strip()
    except Exception as exc:  # surfaced to the UI as a draft failure
        return jsonify({"error": str(exc)}), 502

    if not text:
        return jsonify({"error": "No draft text returned. Try again."}), 502

    word_count = len(text.split())
    return jsonify({"draft": text, "word_count": word_count})


if __name__ == "__main__":
    app.run(debug=True)
