from django.db import models

class Member(models.Model):
    ''' 
    Model to save instances of members
    '''

    id = models.CharField(primary_key= True, max_length= 20)
    real_name = models.CharField(max_length= 100)
    tz = models.CharField(max_length = 64)

    def __str__(self):
        return self.real_name


class ActivityPeriod(models.Model):
    '''
    Model to save activities of Member

    '''

    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    #foreign key, references to 'id' field of Member table
    id_member = models.ForeignKey(Member, related_name= 'activities', on_delete = models.CASCADE)

    


