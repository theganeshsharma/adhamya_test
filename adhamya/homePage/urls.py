from . import views
from django.urls import path

app_name='homePage'

urlpatterns = [

    #home-page
    path('',views.index,name='index'),

    #login-page
    path('login/',views.login,name='login'),


    #feedback-form-submit
    path('feedback/',views.feedback,name='feedback'),


]