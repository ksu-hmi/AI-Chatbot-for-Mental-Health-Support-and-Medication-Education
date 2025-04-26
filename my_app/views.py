from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'chatbot.html')

def get_response(request):
    user_input = request.GET.get('message')

    if "anxiety" in user_input.lower():
        return HttpResponse("Try deep breathing or mindfulness exercises. Would you like more tips?")
    elif "ptsd" in user_input.lower():
        return HttpResponse("Grounding techniques can be helpful for PTSD. Would you like a few examples?")
    elif "ocd" in user_input.lower():
        return HttpResponse("It helps to challenge obsessive thoughts. Cognitive-behavioral therapy can be effective.")
    elif "depression" in user_input.lower():
        return HttpResponse("You're not alone. Setting small goals and staying connected to others can help.")
    else:
        return HttpResponse("I'm here to listen. Could you tell me more about how you're feeling?")