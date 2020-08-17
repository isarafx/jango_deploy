from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


# Create your views here.
def show_text(request):

    obj = Post.objects.all()

    # return HttpResponse("Hello, my first Django")
    return render(request, "myblog/home.html", {'context': obj})


def show_single_post(request, id):

    obj = Post.objects.get(id=id)

    return render(request, "myblog/post-details.html", {'single_post': obj})
