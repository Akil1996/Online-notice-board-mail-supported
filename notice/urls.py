from django.urls import path
from . import views
urlpatterns=[
    path('',views.notice,name="notice"),
    path('noticedetails/',views.notice,name="noticedetails"),
    path('noticepost/',views.noticep,name="noticep"),
]