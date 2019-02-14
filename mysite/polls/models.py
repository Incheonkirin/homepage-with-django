# Create your models here.
# 선생님이 메일로 보내주신 내용 복사/ 붙여넣기 하였음.


# 매일 만드는 것은 question choicetext와, CharField정도입니다.
# 나중에는 간단해 보입니다.

from django.db import models
import datetime
from django.utils import timezone

class Question(models.Model):#데이터 테이블/ 쿼리를 이용해서 만드는 게 아니고, 장고가 가진 .. 걸 이용해서. 어떤 DB던지 다 연결 할 수 있기 때문에.
    question_text = models.CharField(max_length=200) #문자열을 저장하는데 200자 까지.
    pub_date = models.DateTimeField('date published') #만들어 질때의 날짜를 이야기합니다.
    def __str__(self):
        return self.question_text # 문자열을 호출하는데 가면, 자동으로 이거를 뱉음

    def was_published_recently(self): #가장 최근에 저장된 것을 뽑기 위해서.
        now = timezone.now() #날짜를 받고
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
class Choice(models.Model):
    question = models.ForeignKey(#내가 만든 모델이 서버측에 저장, 올라갑니다.
        'Question',  on_delete=models.CASCADE,#위에 퀘스쳔이 지워지면 이것도 같이 지워지도록.
    )
    choice_text = models.CharField(max_length=200) #선택 텍스트를 넣어줌
    votes = models.IntegerField(default=0) #
    def __str__(self):
        return self.choice_text
