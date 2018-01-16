from django.shortcuts import render

from .models import Golfer

# Create your views here.
def MeetTheBoard(request):
    board_member_list = Golfer.objects.all().filter(board_member__gt=0).order_by('-board_member')
    context = {'board_member_list': board_member_list}
    return render(request,'golfers/MeetTheBoard.html',context)
