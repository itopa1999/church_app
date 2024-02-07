import django_filters
from django_filters import DateFilter
from .models import *

class MemberFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    email = django_filters.CharFilter(field_name='email', lookup_expr='icontains')
    state = django_filters.CharFilter(field_name='state', lookup_expr='icontains')
    district = django_filters.CharFilter(field_name='district', lookup_expr='icontains')
    date__lte = django_filters.DateFilter(field_name='date', lookup_expr='lte')
    date__gte = django_filters.DateFilter(field_name='date', lookup_expr='gte')
    class Meta:
        model = Member
        fields = ['gender','name','email','state','department','date__lte','date__gte']


class AttendanceFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='member__name', lookup_expr='icontains')
    email = django_filters.CharFilter(field_name='member__email', lookup_expr='icontains')
    phone = django_filters.CharFilter(field_name='member__phone', lookup_expr='icontains')
    district = django_filters.CharFilter(field_name='member__district', lookup_expr='icontains')
    gender = django_filters.CharFilter(field_name='member__gender')
    department = django_filters.CharFilter(field_name='member__department')
    date__lte = django_filters.DateFilter(field_name='date', lookup_expr='lte')
    date__gte = django_filters.DateFilter(field_name='date', lookup_expr='gte')
    class Meta:
        model = Member
        fields = ['phone','name','email','department','date__lte','date__gte','gender','district']

        