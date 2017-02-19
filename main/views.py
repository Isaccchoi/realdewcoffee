from django.shortcuts import render
from .forms import PostForm

# Create your views here.
def home(request):
    title = "안녕하세요"

    ctx = {
        "title": title
    }

    return render(request, 'home.html', ctx)

def location(request):
    ctx = {
        'title': "RealDew Coffee 오시는길",
        'form': PostForm
    }
    return render(request, 'main/location.html', ctx)
