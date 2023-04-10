from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import openai
sentiment = SentimentIntensityAnalyzer()


'''
•(Done) Intent - Greetings, Question/answer, Task Completion, Decision Making Advice
•(Done) Topic - Relationship advice, Philosophy, Career guidance, Health and wellness, ritualistic section
•(Done) Sentiment- Positive, Negative, Neutral
•(Done) Opinion- Positive, Negative, Neutral
'''

openai.api_key = ADD_YOUR_API_KEY(Removed because of security purposes)
#text = input("You: ")

def ask_question(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.3,
        max_tokens=50,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text.strip()

def detectSentiment(text):
    sent = sentiment.polarity_scores(text)
    if sent["compound"] > 0.05:
        return "pos"
    elif sent["compound"] < -0.05:
        return "neg"
    else:
        return "neu"


def detectTopic(text):
    prompt = f"Respond with the topic of the text: {text} from the given list: Relationship advice, Philosophy, Career guidance, Health and wellness, ritualistic section\nResponse:"
    return ask_question(prompt)

def detectIntent(text):
    prompt = f"What is the intent of the text: {text} from the given list: \nGreetings \nQuestion/answer, \nTask Completion, \nDecision Making Advice?\n\nAnswer:"
    return ask_question(prompt)

def detectOpinion(text,prev_message):
    # prev_message=input("Enter Sakha's previous message: ")
    prompt = f"Respond with the opinion (Positive, Negative or Neutral) of the user in the following situation:\nChatbot: {prev_message}\nUser: {text}\n\nResponse: "
    return ask_question(prompt)
