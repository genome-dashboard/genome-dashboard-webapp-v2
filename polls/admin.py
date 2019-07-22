from django.contrib import admin

from .models import Choice, Question

# Define model admin class.
class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]


# Register your models here.
admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)
