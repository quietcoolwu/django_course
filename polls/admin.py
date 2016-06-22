from django.contrib import admin

# Register your models here.

from .models import Question, Choice


# It’d be better if you could add a bunch of Choices directly when you create the Question.
# 3 blank choices by default.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # The first element of each tuple in fieldsets is the title of the fieldset.
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    # Display column-list order.
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # Add filter siderbar - filtering by pub_date
    list_filter = ['pub_date']
    # Add search box - keyword: question_text
    search_fields = ['question_text']


# Tell the admin that Question objects have an admin interface.(QuestionAdmin)
# Often, you’ll want to customize how the admin form looks and works.
# Create a model admin object, then pass it as the second argument
# to admin.site.register() – any time you need to
# change the admin options for an object.

admin.site.register(Question, QuestionAdmin)
