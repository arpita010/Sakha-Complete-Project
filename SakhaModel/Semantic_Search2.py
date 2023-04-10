import json
from sentiment_detection import detectSentiment, ask_question, detectTopic, detectIntent, detectOpinion

with open("sakhaE.json", "r", encoding="utf-8") as f:
    dataset = json.load(f)

user_input = input("Enter a message: ")
opinion = detectOpinion(user_input)
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

print(final_response)

        
    