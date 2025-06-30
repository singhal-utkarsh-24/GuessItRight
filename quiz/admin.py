from django.contrib import admin
from .models import Category, Quiz, Question, Choice, UserRank, QuizSubmission

# Register your models here.
admin.site.register(Category)
admin.site.register(Quiz)
admin.site.register(Question)
class ChoiceAdmin(admin.ModelAdmin) :
    list_display = ('question' , 'text' , 'is_correct')

admin.site.register(Choice, ChoiceAdmin)
admin.site.register(UserRank)
admin.site.register(QuizSubmission)
