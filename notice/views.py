from django.shortcuts import render,redirect
from .models import jobfair
from django.contrib import messages
from django.core.mail import send_mail
from users.models import CustomUser
from django.contrib.auth import get_user_model
# Create your views here.
def notice(request):
    data = jobfair.objects.all()

    context = {
    "jobsfair": data
    }
    return render(request,'notice.html',context)



def noticep(request):
    if (request.method=='POST'):
        ename = request.POST['eventname']
        edate = request.POST['eventdate']
        sperson =request.POST['seminarperson']
        tech=request.POST['technology']
        dept =request.POST['deptment'] 
        plac =request.POST['place']
        User = get_user_model()
        for user in User.objects.all(): 
            if dept == user.department:
                send_mail('Notice','We are conducting '+str(ename)+' on '+str(edate),'akhil.nitroware@gmail.com',[user.email],fail_silently=False)
        s=jobfair(eventname=ename,eventdate=edate,seminarperson=sperson,technology=tech,deptment=dept,place=plac)
        s.save()
        data = jobfair.objects.all()
        for job in data:
            if job.deptment == CustomUser.department:
                messages.success(request,('Event'))
                send_mail('Notice','We have added an ','akhil.nitroware@gmail.com',[str(emails)],fail_silently=False)
        messages.success(request,('Event has posted successfull'))


    return render(request,'noticep.html',{})