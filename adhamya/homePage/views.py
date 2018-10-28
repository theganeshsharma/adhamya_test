from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from homePage.forms import formLogin,formFeedback
from .models import Feedback,User


#--home Page--
def index(request):
    return render(request,'homePage/index.html',{'context': ''})

#--feedback form--
def feedback(request):
    forms = formFeedback()
    if(request.method == "POST"):
        feedbackObj = Feedback()
        if forms.is_valid():
            return HttpResponse('Form is invalid')
        else:
            forms = formFeedback(request.POST)
            feedbackObj.Name = request.POST.get('name')
            feedbackObj.EmailID = request.POST.get('email')
            feedbackObj.Comment = request.POST.get('comments')
            feedbackObj.save()
            return render(request, 'homePage/index.html', {'forms': forms})
    else:
        return HttpResponse('Form is invalid')

#--login Page--
def login(request):
    return render(request, 'homePage/login.html', {'context': ''})





