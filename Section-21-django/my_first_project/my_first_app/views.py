from django.shortcuts import render
from .models import Person


# Create your views here.
def index(request):
    return render(request, "my_first_app/base.html", {"person": Person.objects.all()})


def saludar(request):
    return render(request, "my_first_app/saludar.html")