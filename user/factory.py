import factory
from factory.django import DjangoModelFactory
from faker import Faker

from user.models import Member, ActivityPeriod

from factory.fuzzy import FuzzyText

class CustomFuzzyText(FuzzyText):
    '''
    class to obtain random string of length for our id field
    '''
    def fuzz(self, *args, **kwargs):
       return super(CustomFuzzyText, self).fuzz(*args, **kwargs).upper()

class MemberFactory(DjangoModelFactory):
    class Meta:
        model = Member
    
    id = CustomFuzzyText(length = 8) # calling CustomFuzzyText which returns random string of length - 8
    real_name = factory.Faker('name')
    tz = factory.Faker('timezone')

class ActivityPeriodFactory(DjangoModelFactory):
    class Meta:
        model = ActivityPeriod

    id_member = factory.SubFactory(MemberFactory) # to maintain one to one realationship between the table
    start_time = factory.Faker('date_time_this_month')
    end_time  = factory.Faker('date_time_this_month')
