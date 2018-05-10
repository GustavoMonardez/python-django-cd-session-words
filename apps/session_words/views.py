from django.shortcuts import render, HttpResponse, redirect
from time import strftime, gmtime
import datetime

def index(request):
    return render(request, "session_words/index.html")

def process(request):
    # capture data
    word = request.POST["word"]
    color = request.POST["color"]
    font = request.POST.getlist('font')
    if len(font):
        font="large"
    else:
        font="normal"
    # time
    time = datetime.datetime.now()    
    time = time.strftime("%I:%M %p, %b %d %Y")
    words = {
        "word": word,
        "color": color,
        "font": font,
        "time": time
    }
    if not "content" in request.session:
        temp = [words]
        request.session["content"] = temp
    else:
        temp = request.session["content"]
        temp.append(words)
        request.session["content"] = temp
    
    return redirect("/session_words")

def clear(request):
    request.session.flush()
    return redirect("/session_words")


