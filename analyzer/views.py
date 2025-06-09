from django.shortcuts import render
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import random

analyzer = SentimentIntensityAnalyzer()

def chat_page(request):
    chat_history = []

    if request.method == "POST":
        user_message = request.POST.get("user_input")
        bot_response = ""
        mood = ""

        if user_message:
            score = analyzer.polarity_scores(user_message)
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

            # Create the chat history for this one turn
            chat_history = [
                {"sender": "user", "message": user_message},
                {"sender": "bot", "message": bot_response, "mood": mood}
            ]

    else:
        # Default message when GET request is made (on first visit)
        chat_history = [
            {"sender": "bot", "message": "Hello! How are you feeling today?"}
        ]

    return render(request, 'analyzer/chat.html', {
        "chat_history": chat_history
    })
