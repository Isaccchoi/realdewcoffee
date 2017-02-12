from django.shortcuts import render

# Create your views here.
def home(request):
    title = "안녕하세요"

    ctx = {
        "title": title
    }

    return render(request, 'home.html', ctx)
