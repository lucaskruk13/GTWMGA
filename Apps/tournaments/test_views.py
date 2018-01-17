from django.test import TestCase
from .models import Tournament, Points
from Apps.golfer.models import Golfer
from Apps.accounts.models import MyUser

class TournamentViewTestCases(TestCase):

    def setUp(self):
        user = MyUser.objects.create(email="test@test.com")
        user.set_password("test123")

        tournament = Tournament.objects.create(name="Test Tournament", description="Test Tournament Description", date='2018-01-13')

        Points.objects.create(golfer=Golfer.objects.get(account_id=user.id), tournament=tournament, extra_points=75)

    def test_can_get_to_tournaments(self):
        response = self.client.get('/tournaments/')
        self.assertEqual(response.status_code, 200)

    def test_can_not_get_to_tournament_details_before_tournament_is_created(self):

        response = self.client.get('/tournaments/3/')
        self.assertEqual(response.status_code, 404)

    def test_can_populate_tournament_list(self):

        tournament = Tournament.objects.get(name="Test Tournament")

        response = self.client.get('/tournaments/')
        self.assertContains(response, '<div class="container" id="tournament-container">')
        self.assertTemplateUsed(response, 'tournaments/tournaments.html')

        # Test it contains a row for each element.
        table_data1 = "<td><a href=\'/tournaments/" +  str(tournament.id) + "/\'>Jan. 13, 2018</a></td>"
        table_data2 = '<td>' + tournament.get_course_display() + '</td>'
        table_data3 = '<td>' + tournament.name + '</td>'

        self.assertContains(response, table_data1)
        self.assertContains(response, table_data2)
        self.assertContains(response, table_data3)

        #verify td link works
        tdLink = '/tournaments/' + str(tournament.id) + '/'
        tdLinkResponse = self.client.get(tdLink)
        self.assertEquals(tdLinkResponse.status_code, 200)

    def test_tournamet_is_setup_and_can_get_to_detail_page(self):
        tournament = Tournament.objects.get(name="Test Tournament")

        # make sure it exists
        self.assertNotEqual(tournament, None)

        # Verify we could get to the tournament page
        response = self.client.get('/tournaments/' + str(tournament.id) + '/')
        self.assertEqual(response.status_code, 200)

