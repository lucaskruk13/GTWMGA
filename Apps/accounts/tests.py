from django.test import TestCase

from .models import MyUser
from Apps.golfer.models import Golfer

class MyUserTestCase(TestCase):
    def setup(self):
        user = MyUser.objects.create(email="test@test.com")
        user.set_password("test123")


    def test_golfer_was_created(self):
        # Test that when a user was created, so was a golfer account

        # Setup the test user
        self.setup()

        # Get the account with the test email
        account = MyUser.objects.get(email="test@test.com")

        # get a golfer with the account id that is the same as the one just created
        golfer = Golfer.objects.get(account=account.id)

        # verify the golfer is not null
        self.assertNotEqual(golfer, None)

        # Verify the profile is not set, and has default data
        self.assertEqual(golfer.__str__(), 'Profile Not Set')
        self.assertEqual(golfer.board_member, 0)


