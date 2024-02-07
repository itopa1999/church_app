from django.urls import path, include
from .import views
from django.contrib.auth.views import LogoutView,LoginView
urlpatterns = [
    path('admin-dashboard', views.dashboard, name="admin-dashboard"),
    path('admin-login', views.login_user, name="admin-login"),
    
    path('admin-member', views.member, name="admin-member"),
    path('admin-question', views.question1, name="admin-question"),
    path('admin-logout', LogoutView.as_view(template_name= "index.html"),name='admin-logout'),
    path('question', views.question, name="question"),
    
    path('filter-results-download', views.filter_results_download, name="filter-results-download"),
    path('filter-attendance-download', views.filter_attendance_download, name="filter-attendance-download"),
    path('all-results-download', views.all_results_download, name="all-results-download"),
    path('all-attendance-download', views.all_attendance_download, name="all-attendance-download"),
    
    path('admin-attendance', views.admin_attendance, name="admin-attendance"),
    
    
]