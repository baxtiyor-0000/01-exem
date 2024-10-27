from django.contrib import admin
from .models import Student, Subject, Exam, Question, Answer, Result


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'group')
    search_fields = ('first_name', 'last_name', 'email', 'group')


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'date')
    list_filter = ('subject',)
    search_fields = ('name', 'subject__name')


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('exam', 'text')
    list_filter = ('exam',)
    search_fields = ('text',)


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'student', 'is_correct')
    search_fields = ('student__first_name', 'student__last_name', 'question__text')


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('student', 'exam', 'score')
    list_filter = ('exam',)
    search_fields = ('student__first_name', 'student__last_name', 'exam__name')
