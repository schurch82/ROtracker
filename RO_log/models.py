from django.db import models
from django.urls import reverse
from django.db.models import Sum
from django.utils import timezone
from django.contrib.auth.models import User
import datetime
# Create your models here.


class PayPeriod(models.Model):
    name = models.CharField(max_length=200,unique=True)
    user = models.ForeignKey(User,on_delete = models.CASCADE,null=True)
    start_date = models.DateField()
    end_date = models.DateField()

    def sold_hours(self):
        hours = self.annotate(Sum('ro__hours_sold'))
        return hours

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("RO_log:payperiod-list")

class RODailyManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(completed_date=timezone.now())

class ROMonthlyManager(models.Manager):
    def get_queryset(self):
        field_name = "pay_period"
        obj=super().get_queryset().first()
        field_value = getattr(obj,field_name)
        return super().get_queryset().filter(pay_period=field_value)

class RO(models.Model):
    RO_number = models.IntegerField()
    user = models.ForeignKey(User,on_delete = models.CASCADE,null=True)
    hours_sold = models.DecimalField(max_digits=5,decimal_places=2)
    work_performed = models.CharField(max_length=200)
    completed_date = models.DateField(default=timezone.now())
    pay_period = models.ForeignKey(PayPeriod,on_delete=models.RESTRICT,null=True)

    def __str__(self):
        return self.RO_number

    def get_absolute_url(self):
        return reverse("RO_log:archive_day")


    class Meta:
        ordering = ['-completed_date']

    objects = models.Manager() # The default manager.
    daily_objects = RODailyManager()
    monthly_objects = ROMonthlyManager()
