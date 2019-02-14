
# 선생님이 메일 보내주신 것, 복사 , 붙여넣기 하였음.
# Create your views here.


from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.views.generic.list import ListView
from polls.models import Question, Choice
from django.utils import timezone

def index(request):

    latest_question_list = Question.objects.all().order_by('-pub_date')[:5] # 모든 것을 가져와서, 역순으로 published date 5개 가져와라.

    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context) # render = html5로 번역해서 보내라.

class IndexView(ListView): #Listview를 상속받음.
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id) # Question이라는 테이블에서 Id가 있으면, 가져오고. 없으면 404
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id) # 404는 데이터가 없으면 보여주는 메시지입니다.
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
