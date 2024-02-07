from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required,user_passes_test
from .models import *
from .filters import MemberFilter
from django.http import HttpResponse
import csv
from datetime import datetime, date
# Create your views here.


def login_user(request):
    if request.method == "POST":
        user = authenticate(email=request.POST.get('email'), password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            mail_subject = 'LOGIN NOIFICATION'
            message = render_to_string(
                'email_template/login_email.html',
                {
                    'name':user.first_name,
                },
            )
            email = EmailMessage(mail_subject, message, to=[request.POST.get('email')])
            email.content_subtype = "html"
            email.send(fail_silently=False)
            return redirect('admin-dashboard')
        else:
            messages.error(request, 'Invalid Email or Password')
            return redirect('admin-login')


    return render(request, "login.html")


@login_required(login_url='admin-login')
def dashboard(request):
    attend_2024=Attendance.objects.filter(date__year=2024).count()
    count_2024=Member.objects.filter(date__year=2024).count()
    question_count_2023=Question.objects.filter(date__year=2023).count()
    count_2023=Member.objects.filter(date__year=2023).count()
    question_count_2024=Question.objects.filter(date__year=2024).count()
    return render(request, "dashboard.html", {"count_2023":count_2023,'count_2024':count_2024,'attend_2024':attend_2024,
                    "question_count_2023":question_count_2023,'question_count_2024':question_count_2024})



@login_required(login_url='admin-login')
def member(request):
    mem=Member.objects.all()
    department=Department.objects.all()
    myFilter=MemberFilter(request.GET, queryset=mem)
    mem=myFilter.qs
    count = len(mem)
    p=Paginator(mem, 40)
    page_num = request.GET.get('page',1)
    try:
        page = p.page(page_num)
    except PageNotAnInteger:
        page = p.page(1)
    except EmptyPage:
        page = p.page(p.num_pages)
    
    return render(request, "member.html",  {"mem":page,"department":department,'count':count})

@login_required(login_url='admin-login')
def filter_results_download(request):
    mem=Member.objects.all()
    myFilter=MemberFilter(request.GET, queryset=mem)
    mem=myFilter.qs
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename ="Register Member Report.csv"'
    
    csv_writer = csv.writer(response)
    header_row = [field_name.verbose_name for field_name in Member._meta.fields]
    csv_writer.writerow(header_row)
    
    for mem in mem:
        data_row = [str(getattr(mem, field_name.name)) for field_name in Member._meta.fields]
        csv_writer.writerow(data_row)
    return response


@login_required(login_url='admin-login')
def all_results_download(request):
    mem=Member.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename ="All Register Member Report.csv"'
    
    csv_writer = csv.writer(response)
    header_row = [field_name.verbose_name for field_name in Member._meta.fields]
    csv_writer.writerow(header_row)
    
    for mem in mem:
        data_row = [str(getattr(mem, field_name.name)) for field_name in Member._meta.fields]
        csv_writer.writerow(data_row)
    return response



@login_required(login_url='admin-login')
def question1(request):
    que=Question.objects.all()
    count=que.count()
    return render(request, "question1.html",  {"que":que,"count":count})


@login_required(login_url='admin-login')
def admin_attendance(request):
    attend=Attendance.objects.all()
    myFilter=AttendanceFilter(request.GET, queryset=attend)
    attend=myFilter.qs
    count = len(attend)
    p=Paginator(attend, 40)
    page_num = request.GET.get('page',1)
    try:
        page = p.page(page_num)
    except PageNotAnInteger:
        page = p.page(1)
    except EmptyPage:
        page = p.page(p.num_pages)
    return render(request, "attendance.html",  {"attend":page,"count":count})



def export_student(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Student.csv"'

    writer = csv.writer(response)
    writer.writerow(['first Name', 'Last Name', 'Email', 'UserID','Profile ID', 'Created Date', 'Updated Date'])
    attend=Attendance.objects.all()
    myFilter=AttendanceFilter(request.GET, queryset=attend)
    attend=myFilter.qs
    for attend in attend:
        writer.writerow([stu.first_name, stu.last_name, stu.email,stu.userid,stu.profile_ID,stu.created_at,stu.updated_at])

    return response



def question(request):
    if request.method=='POST':
        name = request.POST['name']
        email1 = request.POST['email']
        subject = request.POST['subject']
        question = request.POST['question']


        Question.objects.create(
            name=name,
            email=email1,
            subject=subject,
            question=question,
        )

        messages.success(request, "Hi " +name+ ", your question has been submitted,  we will contact you")
        return redirect('index')