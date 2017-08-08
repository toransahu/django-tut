from django.contrib import admin
from .models import Question, Choice
# Register your models here.

#customize the admin form
"""
#customization #1: re-order fields
class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']
    #This particular change above makes the “Publication date”
    #come before the “Question” field
"""

#customization #2: fieldset concept
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
