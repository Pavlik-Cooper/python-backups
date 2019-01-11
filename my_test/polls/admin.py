from django.contrib import admin

# Register your models here.
from .models import Question, Choice

# admin.site.register(Question)
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text','test_field']
    fieldsets = [
        ('Date information', {'fields': ['pub_date']}),
        (None, {'fields': ['question_text']}),
        ('Test fields', {'fields': ['test_field']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)

admin.site.register(Choice)