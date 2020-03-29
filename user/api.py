from rest_framework import viewsets
from user.models import Member, ActivityPeriod
from user.serializers import MemberSerializer, ActivityPeriodSeralizer

class MembersView(viewsets.ModelViewSet):
    '''
    queryset returns all the members and their activities for a month

    '''

    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class ActivityPeriodView(viewsets.ModelViewSet):
    
    mqueryset = ActivityPeriod.objects.all()   
    serializer_class = ActivityPeriodSeralizer



