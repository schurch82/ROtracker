from rest_framework import serializers
from .models import RO, PayPeriod

class ROSerializer(serializers.ModelSerializer):
    class Meta: 
        model = RO
        fields = ('RO_number','user','hours_sold','work_performed','completed_date','pay_period')



class PayPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PayPeriod
        fields = ('name','user','start_date','end_date')


