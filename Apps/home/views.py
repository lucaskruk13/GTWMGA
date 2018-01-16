from django.shortcuts import render
import datetime

from Apps.tournaments.models import Tournament

def index(request):

    tournaments = Tournament.objects.all().order_by("date")
    now = datetime.date.today()

    filteredArray = [tournament for tournament in tournaments if tournament.date > now]

    context = {}

    if filteredArray:
     context = {"tournament": filteredArray[0]}

    return render(request, 'home/index.html', context)

