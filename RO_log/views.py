from urllib import response
from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.dates import TodayArchiveView
from django.db.models import Sum,Q
import datetime
from .models import RO,PayPeriod
from . import forms
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from django.contrib import messages



# Create your views here

class CustomLoginView(LoginView):
    template_name = 'RO_log/login.html'
    fields = "__all__"
    # redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('RO_log:archive_day')

class SignUp(CreateView):
    template_name = 'RO_log/signup.html'
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('RO_log:archive_day')



class ROList(ListView):
    model = RO
    template_name = 'RO_log/RO_list.html'
    # paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = RO.objects.filter(user=self.request.user).filter(
        Q(RO_number__icontains=query)|Q(pay_period__name__icontains=query))
        return object_list



class ROCreate(LoginRequiredMixin,CreateView):
    model = RO
    fields = ['RO_number','hours_sold','work_performed','completed_date']

    def form_valid(self,form):
        form.instance.user = self.request.user
        form_date = form.instance.completed_date
        form.instance.pay_period = PayPeriod.objects.filter(start_date__lte=form_date,end_date__gte=form_date).get()
        
        return super().form_valid(form)
    



class ROUpdate(LoginRequiredMixin,UpdateView):
    model = RO
    fields = ['RO_number','user','hours_sold','work_performed','completed_date']

    def form_valid(self,form):
        form.instance.user = self.request.user
        form_date = form.instance.completed_date
        form.instance.pay_period = PayPeriod.objects.filter(start_date__lte=form_date,end_date__gte=form_date).get()
        return super().form_valid(form)


class RODelete(LoginRequiredMixin,DeleteView):
    model = RO
    success_url = reverse_lazy('RO_log:archive_day')

class ROTodayArchiveView(LoginRequiredMixin,TodayArchiveView):
    queryset = RO.objects.all()
    date_field = "completed_date"
    allow_empty = True
    context_object_name = 'daily_ros'

    def get_context_data(self, **kwargs):
        context=super(ROTodayArchiveView,self).get_context_data(**kwargs)
        context['daily_ros']=context['daily_ros'].filter(user=self.request.user)
        context['daily_total']=context['daily_ros'].filter(user=self.request.user).aggregate(Sum('hours_sold'))['hours_sold__sum']
        context['monthly_hours']=RO.monthly_objects.filter(user=self.request.user).aggregate(Sum('hours_sold'))['hours_sold__sum']
        return context

class PayPeriodList(LoginRequiredMixin,ListView):
    Model = PayPeriod
    queryset=PayPeriod.objects.all()
    context_object_name = 'payperiods'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['payperiods']=context['payperiods'].filter(user=self.request.user)
        return context

class PayPeriodCreate(LoginRequiredMixin,CreateView):
    model = PayPeriod
    fields = ['name','start_date','end_date']

    def form_valid(self,form):
        form.instance.user = self.request.user
        
        return super().form_valid(form)

class PayPeriodUpdate(LoginRequiredMixin,UpdateView):
    model = PayPeriod
    fields = ['name','start_date','end_date']

class PayPeriodDelete(LoginRequiredMixin,DeleteView):
    model = PayPeriod
    success_url = reverse_lazy('RO_log:PayPeriod_list')



class DashboardView(LoginRequiredMixin,ListView):
    template_name = 'RO_log/dashboard.html'
    queryset = PayPeriod.objects.all()
    context_object_name = 'payperiods'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['payperiodhours']=context['payperiods'].filter(user=self.request.user).annotate(Sum('ro__hours_sold'))
        return context


# RO.objects.values('pay_period__name').order_by('pay_period__name').annotate(
# Sum('hours_sold')
#
