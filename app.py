import requests
from flask import Flask, render_template, url_for
from flask import request as req

app = Flask(__name__)
@app.route("/", methods=["GET","POST"])
def index():
    return render_template("index.html")

@app.route('/summarize', methods=["GET", "POST"])
def summarize():
    if req.method == "POST":
        API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
        headers = {"Authorization": "Bearer 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"}

        data = req.form["data"]
        maxL = int(req.form["maxL"])

        minL = 70
        # maxL = 100 
        def query(payload): 
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()
            
        output = query({
            "inputs": data,
            "parameters": {
                "min_length":minL, 
                "max_length":maxL
            }
        })[0]

        return render_template("index.html", result=output["summary_text"])

    else:
        return render_template("index.html")

@app.route("/home")
def home():
    return "Welcome to Home 🏡 "


if __name__ == '__main__':
   app.debug = True
   app.run()
