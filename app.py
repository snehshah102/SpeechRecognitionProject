from flask import Flask, render_template, request, redirect
import speech_recognition as sr
app = Flask(_name_)

@app.route("/", methods=["GET, POST"])
def index():
    if request.method == "POST":
        print("FORM DATA RECEIVED")

        if "file" not in request.files
            return redirect(request.url)
        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)
        if file
            recognizer = sr.Recognizer()
            audioFile = sr.AudioFile(file)
            with audioFile as source:
                data = recognizer.record(source)
            text = recognizer.recognize_google(data, Key=None)
            print(text)
    return render_template('index.html', transcript=transcript)
if _name_=="_main_":
    app.run(debug=True, threaded=True)