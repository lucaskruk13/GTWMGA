from django.db import models
from Apps.accounts.models import MyUser
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Golfer(models.Model):

    board_choices = (
        (0, 'Non Board Member'),
        (1, 'Board Member'),
        (2, 'Treasurer'),
        (3, 'Tournament Chairman'),
        (4, 'Secretary'),
        (5, 'Website Admin'),
        (6, 'Handicap Chairman'),
        (7, 'Vice President'),
        (8, 'President')
    )

    account = models.OneToOneField(MyUser, primary_key=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=40, blank=False, null=True)
    last_name = models.CharField(max_length=60, blank=False, null=True)
    ghin_number = models.CharField(max_length=10, blank=True, null=True)
    handicap = models.DecimalField(blank=True, null=True, decimal_places=1, max_digits=3)
    board_member = models.IntegerField(blank=False, null=False, default=0, choices=board_choices)
    board_member_photo = models.CharField(blank=True, max_length=255, null=True)

    class Meta:
        ordering = ('last_name',)

    @receiver(post_save, sender=MyUser)
    def create_user(sender, instance, created, **kwargs):
        if created:
            Golfer.objects.create(account=instance)

    @receiver(post_save, sender=MyUser)
    def save_user(sender, instance, **kwargs):
        instance.golfer.save()

    def __str__(self):

        returnString= "Profile Not Set"

        if self.last_name:
            returnString = "{lastName}, {firstName}".format(firstName=self.first_name, lastName=self.last_name)

        return returnString