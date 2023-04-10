from flask import Flask, request, jsonify
import json
from sentiment_detection import detectSentiment, ask_question, detectTopic, detectIntent, detectOpinion

app = Flask(__name__)

with open("sakhaE.json", "r", encoding="utf-8") as f:
    dataset = json.load(f)
@app.route('/')
def welcome_page():
    return "Welcome to our sakha model api"

@app.post('/predict')
def home():
    # print(request.is_json)
    # print(request.get_json())
    # print(type(request.get_json()))
    request_json=json.loads(request.get_json())
    # print(type(request_json))
    #user_input = request.get_json().get("userInput")
    #prev_message = request.get_json().get("prevMessage", "")
    user_input=request_json['userInput']
    prev_message=request_json['prevMessage']
    opinion = detectOpinion(user_input,prev_message)
    sentiment = detectSentiment(user_input)
    topic = detectTopic(user_input)
    intent = detectIntent(user_input)
    prev_score = 0
    for i in dataset["sakhaE"]:
        match = 0
        for keyword in i["keywords"]:
            if keyword in user_input:
                match = match + 1
        if sentiment.lower() in i["sentiment"].lower():
            match = match + 1
        if topic.lower() in i["topic"].lower():
            match = match + 1
        if intent.lower() in i["intent"].lower():
            match = match + 1
        if opinion.lower() in i["opinion"].lower():
            match = match + 1

        if match > prev_score:
            prev_score = match
            final_response = i["response"]
    return jsonify({"answer": final_response})

if __name__ == '__main__':
    app.run(debug=True)
