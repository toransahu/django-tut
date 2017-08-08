from django.contrib import admin
from .models import Question
# Register your models here.

#customize the admin form

class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']
    #This particular change above makes the “Publication date”
    #come before the “Question” field

admin.site.register(Question, QuestionAdmin)
