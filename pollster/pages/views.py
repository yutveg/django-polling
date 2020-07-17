from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(request, *args, **kwargs):
    context = {
        "test": "this is a standard key",
        "test_list": [12, 42, 35, 2, 1]
    }
    return render(request, "pages/home.html", context)