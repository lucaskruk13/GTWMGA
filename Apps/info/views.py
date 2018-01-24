from django.shortcuts import render

from .models import ByLaw


# Create your views here.
def bylaws(request):
    laws = ByLaw.objects.first()
    content = laws.bylaws
    return render(request,'info/bylaws.html', {"bylaws": content})
