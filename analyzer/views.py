from django.shortcuts import render
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import random

analyzer = SentimentIntensityAnalyzer()

def chat_page(request):
    bot_response = ""
    mood = ""

    if request.method == "POST":
        user_input = request.POST.get("user_input")
        
        if user_input:  # ✅ Only analyze if input is not empty
            score = analyzer.polarity_scores(user_input)
            compound = score['compound']

            if compound >= 0.05:
                mood = "positive"
                responses = [
                    "That's great to hear! 😊",
                    "Keep up the good vibes!",
                    "Glad you're feeling good!"
                ]
            elif compound <= -0.05:
                mood = "negative"
                responses = [
                    "I'm here for you. 💙",
                    "It's okay to feel down sometimes.",
                    "Try taking a break or talking to a friend."
                ]
            else:
                mood = "neutral"
                responses = [
                    "Thanks for sharing!",
                    "Hmm, tell me more.",
                    "Okay, got it!"
                ]

            bot_response = random.choice(responses)

    return render(request, 'analyzer/chat.html', {
        "bot_response": bot_response,
        "mood": mood
    })
