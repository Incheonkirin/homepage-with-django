"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(), name='home'),
    path('polls/', include('polls.urls', namespace='polls')), #polls 밑에 무엇인가를 찾으면, polls로 가라
    path('sungjuk/', include('sungjuk.urls', namespace='sungjuk')),
    path('chart/', views.Pandas_Graph, name='pandas_graph')

]
#맵핑을 통해서 들어와야 합니다.


# python manage.py makemigrations polls
# python manage.py migrate
# 서버를 기동하겠습니다.
# python manage.py runserver
# 주소가 떨어지고,
# 그대로 브라우져에 써 줍니다.
# 아나콘다에서 ctrl C
#
# pythn manage.py createsuperuser치고,
# 사용자 이름에, admin이라고 치고,
# 이메일 주소 넣어주고
# 패스워드에 에이콘 1234
#
# 만든게 슈퍼유저입니다.
#
# 슈퍼유저를 만든 다음에, 다시 서버를 띄우세요.
# run 서버
#
# 브라우저에 가서, 8000번 다음에 admin이라고 칩니다. /admin/
#
# 아이디하고 패스워드 치면, 관리자 페이지가 만들어집니다.
# Question에 추가를 누릅니다.
#
