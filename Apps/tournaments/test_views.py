from django.test import TestCase
from .models import Tournament, Point
from Apps.golfer.models import Golfer
from Apps.accounts.models import MyUser

class TournamentViewTestCases(TestCase):

    def setUp(self):
        user = MyUser.objects.create(email="test@test.com")
        user.set_password("test123")

        tournament = Tournament.objects.create(name="Test Tournament", description="Test Tournament Description", date='2018-01-13')

        golfer = Golfer.objects.get(account=user.id)
        golfer.first_name = "Test"
        golfer.save()



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

    def test_tournament_is_setup_and_can_get_to_detail_page(self):
        tournament = Tournament.objects.get(name="Test Tournament")

        # make sure it exists
        self.assertNotEqual(tournament, None)

        # Verify we could get to the tournament page
        response = self.client.get('/tournaments/' + str(tournament.id) + '/')
        self.assertEqual(response.status_code, 200)

    def test_tournament_is_setup_and_flight_details_do_not_exist(self):

        #get the tournament
        tournament = Tournament.objects.get(name="Test Tournament")

        #get the page
        response = self.client.get('/tournaments/' + str(tournament.id) + '/')
        self.assertEquals(response.status_code, 200)

        #verify there should be no page
        self.assertNotContains(response, "Black Tees")
        self.assertNotContains(response, "Gold Tees")
        self.assertNotContains(response, "Blue Tees")
        self.assertNotContains(response, "White Tees")

    def test_tournament_is_setup_and_flight_details_exist(self):
        # get the tournament
        tournament = Tournament.objects.get(name="Test Tournament")

        golfer = Golfer.objects.get(first_name="Test")


        # Dont Create a black flight in order to test the championship text
        Point.objects.create(golfer=golfer, tournament=tournament, flight_color=1)
        Point.objects.create(golfer=golfer, tournament=tournament, flight_color=2)
        Point.objects.create(golfer=golfer, tournament=tournament, flight_color=3)
        Point.objects.create(golfer=golfer, tournament=tournament, flight_color=2, flight_number=2)

        # get the page
        response = self.client.get('/tournaments/' + str(tournament.id) + '/')
        self.assertEquals(response.status_code, 200)

        # verify there should be result links
        self.assertNotContains(response, "Black Tees")
        self.assertContains(response, "Gold Tees (Championship)")
        self.assertContains(response, "Blue Tees")
        self.assertContains(response, "White Tees")

        # refresh and make sure the championship text is gone
        Point.objects.create(golfer=golfer, tournament=tournament, flight_color=4)
        response = self.client.get('/tournaments/' + str(tournament.id) + '/')
        self.assertNotContains(response, "Gold Tees (Championship)")
        self.assertContains(response, "Gold Tees")


        # Test results links
        whiteResponse = self.client.get("/tournaments/" + str(tournament.id) + "/white_tee_results/")
        blueResponse = self.client.get("/tournaments/" + str(tournament.id) + "/blue_tee_results/")
        goldResponse = self.client.get("/tournaments/" + str(tournament.id) + "/gold_tee_results/")
        blackResponse = self.client.get("/tournaments/" + str(tournament.id) + "/black_tee_results/")


        self.assertEquals(blueResponse.status_code, 200)
        self.assertEquals(goldResponse.status_code, 200)
        self.assertEquals(blackResponse.status_code, 200)
        self.assertEquals(whiteResponse.status_code, 200)



    def test_tournament_is_setup_detail_page_is_setup_with_multiple_tables(self):

        tournament = Tournament.objects.get(name="Test Tournament")
        golfer = Golfer.objects.get(first_name="Test")

        Point.objects.create(golfer=golfer, tournament=tournament, flight_color=2, flight_number=1)
        Point.objects.create(golfer=golfer, tournament=tournament, flight_color=2, flight_number=2)

        response = self.client.get("/tournaments/" + str(tournament.id) + "/blue_tee_results/")

        self.assertContains(response, 'table-hover', count=2)

    def test_tournament_points_table(self):

        for x in range(1, 51):
            email = str(x)+"@"+str(x)+".com"
            user = MyUser.objects.create(email=email)
            golfer = Golfer.objects.get(account_id=user.id)

            Point.objects.create(golfer=golfer, tournament=Tournament.objects.get(name="Test Tournament"), extra_points=x)

        response = self.client.get('/tournaments/point_standings/')

        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'class="cup-qualifier"', count=34) # Verify there are 34 cup qualifiers

        # No test it adds correctly

        tournament = Tournament.objects.create(name="Test Tournament 2", date="2018-02-03")
        firstUser = MyUser.objects.get(email="1@1.com")
        firstGolfer = Golfer.objects.get(account_id=firstUser.id)
        firstGolfer.first_name = "Golfer"
        firstGolfer.last_name = "Test"
        firstGolfer.save()

        Point.objects.create(golfer=firstGolfer, tournament=tournament, extra_points=100)

        response = self.client.get('/tournaments/point_standings/')

        self.assertContains(response, '<td>1st</td>\n                    <td>301</td>\n                    <td>Test, Golfer</td>\n')