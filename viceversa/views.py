from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
    # return HttpResponse('Hello!')

def reverse(request):
    user_text = request.GET['usertext']
    reversed_user_text = user_text[::-1]
    words = user_text.split()
    words_count = len(words)
    return render(request, 'reverse.html', {'user_text': user_text, 'reversed_user_text': reversed_user_text, 'words_count': words_count})