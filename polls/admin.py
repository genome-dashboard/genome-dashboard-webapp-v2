from django.contrib import admin

from .models import Choice, Question


# class ChoiceInline(admin.StackedInline):
#     model = Choice
#     extra = 3

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # ver 1.
    # fields = ['pub_date', 'question_text']

    # ver 2.
    # fieldsets = [
    #     (None,               {'fields': ['question_text']}),
    #     ('Date information', {'fields': ['pub_date']}),
    # ]

    # ver 3.
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]


# Register your models here.
admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)
