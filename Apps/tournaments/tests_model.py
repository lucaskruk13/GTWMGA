from django.test import TestCase
from .models import Tournament, Points
from Apps.golfer.models import Golfer
from Apps.accounts.models import MyUser
import datetime
# Create your tests here.
class TournamentTestCases(TestCase):

    def setUp(self):

        user = MyUser.objects.create(email="test@test.com")
        user.set_password("test123")

        tournament = Tournament.objects.create(name="Test Tournament", description="Test Tournament Description", date='2018-01-13')

        Points.objects.create(golfer=Golfer.objects.get(account_id=user.id), tournament=tournament, extra_points=75)

    def test_create_points(self):

        points = Points.objects.get(extra_points=75)

        # Verify the participation points are 100
        self.assertEqual(points.extra_points, 75)

    def test_sum_points(self):
        points = Points.objects.get(extra_points=75)

        self.assertEqual(points.calc_points(), (points.participation_points + points.extra_points))


