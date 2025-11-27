# Importing libraries
from flask import Flask, render_template, request
import webbrowser
import google.generativeai as genai
import os
import threading
import time

# Load API key and configure Gemini
my_api_key_gemini = 'AIzaSyB5Qx-ht56m6NwV27DIz8z_jhA5hHri0nI'
genai.configure(api_key=my_api_key_gemini)
model = genai.GenerativeModel('gemini-2.5-flash')

# Initialize Flask app
app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def hello_world():
    if request.method == 'POST':
        try:
            prompt = request.form['prompt']
            response = model.generate_content(prompt)
            return response.text if response.text else "Sorry, Gemini didn't want to answer that!"
        except Exception as e:
            return f"Oops! Error: {e}"
    return render_template('index.html')

# Open the default web browser after a brief delay
def open_browser():
    time.sleep(1)
    webbrowser.open("http://127.0.0.1:5000")

# Start the Flask app
if __name__ == "__main__":
    threading.Thread(target=open_browser).start()
    app.run()


