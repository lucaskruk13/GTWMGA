from django.db.models import Count, Sum
from django.shortcuts import render, get_object_or_404

import operator
import math



from .models import Tournament, Points
from Apps.golfer.models import Golfer

goldTeeResults = {}

# Create your views here.
def tournaments(request):
    tournament_list = Tournament.objects.order_by('date')
    context = {'tournament_list': tournament_list}
    return render(request, 'tournaments/tournaments.html', context)

def detail(request, tournament_id):



    tournament = get_object_or_404(Tournament, pk=tournament_id)

    black_flights = get_results(tournament_id, 4)
    gold_flights = get_results(tournament_id, 3)
    blue_flights = get_results(tournament_id, 2)
    white_flights = get_results(tournament_id, 1)

    return render(request, 'tournaments/detail.html', {'tournament': tournament, 'gold_tees':gold_flights, 'black_tees': black_flights, 'blue_tees': blue_flights, 'white_tees': white_flights })

def gold_tee_results(request, tournament_id):

    gold_tees = generate_html(get_results(tournament_id, 3))

    return render(request, 'tournaments/gold_tee_results.html', {"tournament_id":tournament_id, "gold_tees":gold_tees})
def blue_tee_results(request, tournament_id):

    blue_tees = generate_html(get_results(tournament_id, 2))

    return render(request, 'tournaments/blue_tee_results.html', {"tournament_id":tournament_id, "blue_tees":blue_tees})

def black_tee_results(request, tournament_id):
    black_tees = generate_html(get_results(tournament_id, 4))

    return render(request, 'tournaments/black_tee_results.html',
                  {"tournament_id": tournament_id, "black_tees": black_tees})

def white_tee_results(request, tournament_id):
    white_tees = generate_html(get_results(tournament_id, 1))

    return render(request, 'tournaments/white_tee_results.html',
                  {"tournament_id": tournament_id, "white_tees": white_tees})

def point_standings(request):

    points_rankings = {}
    all_golfers = Golfer.objects.all()

    for this_golfer in all_golfers:
        points = Points.objects.all().filter(golfer=this_golfer.account_id, date__year=2018)
        num_tournaments = points.count()

        sum_of_extra_points = points.aggregate(sum_of_points=Sum('extra_points'))

        participation_points = num_tournaments * 100

        if sum_of_extra_points["sum_of_points"] is not None:
            total_points_for_year = sum_of_extra_points["sum_of_points"] + participation_points
            points_rankings[this_golfer] = total_points_for_year


    sorted_points_rankings = sorted(points_rankings.items(), key=operator.itemgetter(1), reverse=True)

    ordinal = lambda n: "%d%s" % (n, "tsnrhtdd"[(n / 10 % 10 != 1) * (n % 10 < 4) * n % 10::4])
    # count for position, account for ties
    position = 1
    current_point_status = 0
    iterator = 0
    rankings = []
    for tup in sorted_points_rankings:
        # Always update the iterator
        iterator += 1

        # if the current_point status and the tup dont match, set to position to the iterator
        if tup[1] != current_point_status:
            position = iterator

        # add to the dictonary with right position
        rankings.append((tup[0], tup[1], ordinal(position)))

        # get the current points status
        current_point_status = tup[1]


    return render(request, 'tournaments/point_standings.html', {"rankings":rankings})

def get_results(tournament_id, tee_color):

    black_flights = {}
    gold_flights = {}
    blue_flights = {}
    white_flights = {}

    rankings = {}

    flight_details = Points.objects.values('flight_number', 'flight_color').annotate(Count('flight_number')).order_by(
        "flight_color")

    # Loop thorugh all the flight detals to determine how many of each flight there are
    for detail in flight_details:
        key_Value = str(detail['flight_color']) + "_" + str(detail['flight_number'])

        this_flight_results = Points.objects.all().filter(tournament=tournament_id, flight_color=int(key_Value[:1]),
                                                          flight_number=int(key_Value[-1:])).order_by("place_finished","-extra_points","gross_or_net",
                                                                                                      "golfer__last_name")

        rankings[key_Value] = this_flight_results

    # set each tee group into their own dictionary
    for key, value in rankings.items():
        if int(key[0]) == 4:
            black_flights[key[2]] = value

        if int(key[0]) == 3:
            gold_flights[key[2]] = value

        if int(key[0]) == 2:
            blue_flights[key[2]] = value

        if int(key[0]) == 1:
            white_flights[key[2]] = value


    if tee_color ==4:
        return black_flights
    elif tee_color ==3:
        return gold_flights
    elif tee_color ==2:
        return blue_flights
    else:
        return white_flights


def generate_html(resultsDict):

    returnHtml = ""

    for key, value in resultsDict.items():
        returnHtml += '<h4 class="text-center"><strong>Flight ' + key + ' </strong></h4>\n'
        returnHtml += '\t\t<table class="table-hover table table-bordered">\n'
        returnHtml += '\t\t\t<thead>\n'
        returnHtml += '\t\t\t\t<tr>\n'
        returnHtml += '\t\t\t\t\t<th scope="col">Place</th>\n'
        returnHtml += '\t\t\t\t\t<th scope="col">Gross</th>\n'
        returnHtml += '\t\t\t\t\t<th scope="col">Name</th>\n'
        returnHtml += '\t\t\t\t\t<th scope="col">Divison</th>\n'
        returnHtml += '\t\t\t\t\t<th scope="col">Points Awarded</th>\n'
        returnHtml += '\t\t\t</tr>\n'
        returnHtml += '\t\t\t</thead>\n'
        returnHtml += '\t\t\t<tbody>\n'

        for golfer in value:
            returnHtml += '\t\t\t\t<tr>\n'
            returnHtml += '\t\t\t\t\t<td>' + str(golfer.get_place_finished_display()) + '</td>\n'
            returnHtml += '\t\t\t\t\t<td>' + str(golfer.get_gross_or_net_display()) + '</td>\n'
            returnHtml += '\t\t\t\t\t<td>' + str(golfer.golfer) + '</td>\n'
            returnHtml += '\t\t\t\t\t<td>' + str(golfer.get_flight_color_display()) + '</td>\n'
            returnHtml += '\t\t\t\t\t<td>' + str(golfer.calc_points()) + '</td>\n'
            returnHtml += '\t\t\t\t<tr>\n'

        returnHtml += '\t\t\t<tbody>\n'
        returnHtml += '\t\t</table>\n'

    return returnHtml
