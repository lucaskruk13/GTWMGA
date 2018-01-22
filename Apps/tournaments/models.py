from django.db import models
import datetime
from django.utils.translation import gettext as _

from Apps.golfer.models import Golfer

# Create your models here.
class Tournament(models.Model):

    default_start_time = datetime.time(8,30,0)

    course = (
        ('OAKS', 'The Oaks'),
        ('PT', 'Panther Trail'),
        ('LW', 'Lake Windcrest'),
    )

    players_in_group = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
    )

    name = models.CharField(max_length=50, blank=False)
    description = models.CharField(max_length=1000, blank=False)
    date = models.DateField(blank=False)
    course = models.CharField(max_length=4, choices=course, default='OAKS')
    start_time = models.TimeField(default=default_start_time)
    gold_flight = models.BooleanField(default=True)
    blue_flight = models.BooleanField(default=True)
    white_flight = models.BooleanField(default=True)
    num_players = models.IntegerField(choices=players_in_group, default=1)
    sign_up_link = models.URLField(blank=True, null=True)
    major = models.BooleanField(default=False)
    pairing_party = models.BooleanField(default=False)
    calcutta = models.BooleanField(default=False)


    def __str__(self):
        return self.name


class Point(models.Model):

    flight_color = (
        (1, "White"),
        (2, "Blue"),
        (3, "Gold"),
        (4, "Black"),
    )

    grossOrNet = (
        ('G', "Gross"),
        ('N', "Net"),
    )

    place_finished = (
        (1, "1st"),
        (2, "2nd"),
        (3, "3rd"),
        (4, "4th"),
        (99, "DNP"),
    )

    golfer = models.ForeignKey(Golfer, on_delete=models.CASCADE)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    participation_points = models.IntegerField(default=100)
    extra_points = models.IntegerField(default=0, null=True, blank=True)
    flight_color = models.IntegerField(default=2, choices=flight_color, blank=False, null=False)
    flight_number = models.IntegerField(default=1, blank=False, null=False)
    date = models.DateField(default=datetime.datetime.now)
    place_finished = models.IntegerField(null=True, blank=True, default=99, choices=place_finished)
    gross_or_net = models.CharField(max_length=1, blank=False, null=False, choices=grossOrNet, default='N')


    class Meta:
        ordering = ('golfer',)

    def calc_points(self):
        points = self.participation_points

        if self.tournament.major:
            points += self.extra_points * 2
        else:
            points += self.extra_points

        return points




    def __str__(self):
        tournament_name = Tournament.objects.get(pk=self.tournament_id)
        golfer_name = Golfer.objects.get(pk=self.golfer_id)

        return golfer_name.__str__() + " - " + tournament_name.__str__() + " on " + self.date.__str__()

    def __flight_color__(key):
        if key == 1:
            return "White"
        elif key == 2:
            return "Blue"
        elif key == 3:
            return "Gold"
        else:
            return "Black"








