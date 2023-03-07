from . import views
from django.urls import path

urlpatterns = [

    path('',views.demo,name='demo'),
    path('news/',views.news,name='news')
    # path('about/',views.about,name='adout'),
    # path('contact/',views.contact,name='contact'),
    # path('add/',views.addition,name='addition')
]