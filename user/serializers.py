from rest_framework import serializers
from user.models import Member, ActivityPeriod


    
class ActivityPeriodSeralizer(serializers.ModelSerializer):
    '''
    Class to buid a serializer for ActivityPeriod Class in models.py

    '''

    # returns date in [Month's name-Date-Year Hours(12-hours format):Minutes AM/PM] format
    start_time = serializers.DateTimeField(format= " %B %d %Y %I:%M %p ")
    end_time = serializers.DateTimeField(format= " %B %d %Y %I:%M %p ")
    class Meta:
        model = ActivityPeriod
        fields = ('start_time','end_time')

class MemberSerializer(serializers.ModelSerializer):
    '''
    Class to buid a serializer for Members Class in models.py

    '''
    # activities gives all the member's activities from the ActivityPeriod model
    activities = ActivityPeriodSeralizer(many=True)
    class Meta:
        model = Member
        fields = ('id', 'real_name', 'tz', 'activities')

