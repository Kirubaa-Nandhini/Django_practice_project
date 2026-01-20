from django.contrib import admin
from .models import Question
from .models import Choice
# Register your models here.
class choiceInline(admin.TabularInline):
    model=Choice
    extra=3
class QuestionAdmin(admin.ModelAdmin):
    fieldsets=[
        ("date_information",{"fields":["pub_date"]}),
        ("Question_information",{"fields":["question_text"],"classes":["collapse"]}),
        ]
    inlines = [choiceInline]
    list_display=["question_text","pub_date","was_published_recently"]
    list_filter=["pub_date"]
    search_fields=["question_text"]
        
admin.site.register(Question, QuestionAdmin)

