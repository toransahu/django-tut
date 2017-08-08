from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
import datetime
# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        """
        #.1 was giving wrong result for future pub_date questions
        """
        #.1 return self.pub_date>= timezone.now() - datetime.timedelta(days=1)

        """
        correctted by following
        """
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    #improvise: adding attributes to was_published_recently() for admin page
    was_published_recently.admin_order_field = 'pub_date' #will give option to sort questions based on pub_date, by clicking on column header
    was_published_recently.boolean = True #will show true/false icon
    was_published_recently.short_description = 'Published recently?' #will modify column header

class Choice (models.Model):
    question =     models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
