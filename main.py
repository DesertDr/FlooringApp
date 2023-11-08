from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    return render(request, 'index.html', context)


def users(request):
    context = {}
    return render(request, 'users.thml', context)
