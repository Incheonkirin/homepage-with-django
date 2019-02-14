# Register your models here.
#선생님이 보내주신 메일 복사_붙여넣기
#관리자 페이지 ( 질문 입력 )
from django.contrib import admin
from .models import Question, Choice
class ChoiceInline(admin.TabularInline): #테이블로 보이게 하라
    model = Choice
    extra = 3
class QuestionAdmin(admin.ModelAdmin):  #관리자페이지(질문입력)
    fieldsets = [
        ('Question Statement', {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]  # 질문 - 선택 연결
    list_display = ('question_text', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['question_text']
admin.site.register(Question, QuestionAdmin) # 관리자 페이지 등록 절차
admin.site.register(Choice)
