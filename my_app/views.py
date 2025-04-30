from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'chatbot.html')

def get_response(request):
    user_input = request.GET.get('message')

    bot_response = "I'm here to listen. Could you tell me more about how you're feeling?"

    if user_input:
        message = user_input.lower()

        if "anxiety" in message:
            bot_response = "Try deep breathing or mindfulness exercises. Would you like more tips?"
        elif "ptsd" in message:
            bot_response = "Grounding techniques can be helpful for PTSD. Would you like a few examples?"
        elif "ocd" in message:
            bot_response = "It helps to challenge obsessive thoughts. Cognitive-behavioral therapy can be effective."
        elif "depression" in message:
            bot_response = "You're not alone. Setting small goals and staying connected to others can help."
        elif "bipolar" in message:
            bot_response = "Managing bipolar disorder often includes mood-stabilizing medication and therapy. Would you like resources?"
        elif "panic attack" in message:
            bot_response = "During a panic attack, try grounding techniques like naming 5 things you can see. Want more tips?"
        elif "medication" in message:
            bot_response = "Medication should always be taken as prescribed. Would you like to learn about common side effects?"
        elif "coping" in message or "self-care" in message:
            bot_response = "Coping strategies include journaling, exercise, and connecting with supportive people."
        elif "yes" in message:
            bot_response = "I'm glad you're interested. I recommend reaching out to a therapist or checking trusted websites like NAMI.org or Mayo Clinic for more resources."
        elif "sad" in message or "feeling down" in message:
            bot_response = "I'm sorry you're feeling sad. It might help to talk to someone you trust or engage in activities you usually enjoy. Would you like more coping tips?"
        elif "zoloft" in message or "sertraline" in message:
            bot_response = "Zoloft (sertraline) is an SSRI often used to treat depression and anxiety. Side effects may include nausea, sleep changes, or dizziness."
        elif "side effects" in message:
            bot_response = "Common side effects of mental health medications include fatigue, nausea, dry mouth, or mood swings. Would you like more info on a specific medication?"
        elif "medication interactions" in message:
            bot_response = "It's important to talk to a pharmacist or provider before mixing medications. Some combinations can cause dangerous effects."
        elif "what does" in message and "do" in message:
            bot_response = "I'm still learning! Please enter the medication name (like Zoloft or Prozac), and I’ll try to help."

    return HttpResponse(bot_response)
