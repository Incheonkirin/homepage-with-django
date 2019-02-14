from sungjuk import views
from django.urls import path

app_name = 'sungjuk'
urlpatterns = [ #http://127.0.0.1:8000/sungjuk
  path('', views.SungjukList.as_view(), name='sungjuk_list'),
  path('new', views.SungjukCreate.as_view(), name='sungjuk_new'),
  path('edit/(?P<pk>\d+)', views.SungjukUpdate.as_view(), name='sungjuk_edit'),
  path('delete/(?P<pk>\d+)', views.SungjukDelete.as_view(), name='sungjuk_delete'),
]
