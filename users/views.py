from django.shortcuts import render, redirect
from administrator.forms import MemberForm
from django.contrib import messages
from administrator.models import Member, Department,Attendance
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.db.models import Q
from datetime import datetime, date
# Create your views here.


def index(request):
    form=MemberForm()
    return render(request, 'index.html',{'form':form})


def register_form(request):
    if request.method=="POST":
        form= MemberForm(request.POST)
        if form.is_valid():
            form=form.save(commit=False)
            department=Department.objects.get(id=request.POST.get('departmentID'))
            form.department=department
            form.save()
            if request.POST.get('email'):
                mail_subject = 'REGISTRATION FOR YOUTH POWER EXPLOSION 2024 SUCCESSFULLY'
                message = render_to_string(
                    'email_template/registration_email.html',
                    {
                        'name':request.POST.get('name')
                    },
                )
                email = EmailMessage(mail_subject, message, to=[request.POST.get('email')])
                email.content_subtype = "html"
                email.send(fail_silently=False)
            messages.success(request, "Hi " +str(request.POST.get('name'))+ ", your registration was successful and we have emailed you.")
            return redirect('index')

def Validation(value, request):
    if value.isdigit() and len(value) <=12:
        value1 = value[1:]
    else:
        value1= value
    mem = Member.objects.filter(Q(email__icontains=value1) | Q(phone__icontains=value1)).first()
    if mem is None:
        pass
    else:
        return mem
        
        



def attendance(request):
    if request.method=="POST":
        date1 = datetime(2024, 2, 6).date()
        date2 = datetime(2024, 2, 6).date()
        date3 = datetime(2024, 2, 6).date()
        value= request.POST.get('member')
        if request.POST.get('day') == 'day1':
            if datetime.now().date() == date1:
                mem = Validation(value, request)
                if mem is not None:
                    if Attendance.objects.filter(member__name = mem, day='Day 1').exists():
                        messages.info(request, 'You have already mark your attendance for Day 1.')
                        return redirect('index')
                    else:
                        Attendance.objects.create(
                            member = mem,
                            day='Day 1'
                        )
                        messages.success(request, 'Congratulations you have mark your attendance for Day 1.')
                        return redirect('index')
                else:
                    messages.error(request, 'We cannot find any member that is associate with this ' + str(value) + ', Check for typo error or Register')
                    return redirect('index') 
            else:
                messages.error(request, 'Sorry Attendance for this Day 1 is invalid.')
            
        elif request.POST.get('day') == 'day2':
            if datetime.now().date() == date2:
                mem = Validation(value, request)
                if mem is not None:
                    if Attendance.objects.filter(member__name = mem, day='Day 2').exists():
                        messages.info(request, 'You have already mark your attendance for Day 2.')
                        return redirect('index')
                    else:
                        Attendance.objects.create(
                            member = mem,
                            day='Day 2'
                        )
                        messages.success(request, 'Congratulations you have mark your attendance for Day 2.')
                        return redirect('index')
                else:
                    messages.error(request, 'We cannot find any member that is associate with this ' + str(value) + ', Check for typo error or Register')
                    return redirect('index') 
            else:
                messages.error(request, 'Sorry Attendance for this Day 2 is invalid.')
        else:
            if datetime.now().date() == date3:
                mem = Validation(value, request)
                if mem is not None:
                    if Attendance.objects.filter(member__name = mem, day='Day 3').exists():
                        messages.info(request, 'You have already mark your attendance for Day 3.')
                        return redirect('index')
                    else:
                        Attendance.objects.create(
                            member = mem,
                            day='Day 3'
                        )
                        messages.success(request, 'Congratulations you have mark your attendance for Day 3.')
                        return redirect('index')
                else:
                    messages.error(request, 'We cannot find any member that is associate with this ' + str(value) + ', Check for typo error or Register')
                    return redirect('index') 
            else:
                messages.error(request, 'Sorry Attendance for this Day 3 is invalid.')
        return redirect('index')
    return redirect('index')
