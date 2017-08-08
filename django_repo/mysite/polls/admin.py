from django.contrib import admin
from .models import Question, Choice
# Register your models here.

#customize the admin form
"""
##customization #1: re-order fields
class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']
    #This particular change above makes the “Publication date”
    #come before the “Question” field

admin.site.register(Question)
"""

##customization #2: fieldset concept
"""
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
"""

##customization #3: Inline Choice addition

#class ChoiceInline(admin.StackedInline): #display choices in stack format
class ChoiceInline(admin.TabularInline): #display choices in tabular format
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    #implementing list_display to display individual fields
    #also added was_published_recently()
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    

admin.site.register(Question, QuestionAdmin)
