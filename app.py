from flask import Flask, request, send_file
from gtts import gTTS
import os
import uuid
 
app = Flask(__name__)
 
@app.route("/tts", methods=["POST"])
def tts():
    data = request.get_json()
    text = data.get("text", "")
    lang = data.get("lang", "en")
 
    filename = f"{uuid.uuid4()}.mp3"
    tts = gTTS(text=text, lang=lang)
    tts.save(filename)
 
    return send_file(filename, mimetype="audio/mpeg")