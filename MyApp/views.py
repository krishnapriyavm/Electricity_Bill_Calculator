from django.shortcuts import render
import json
from django.views.generic import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@method_decorator(csrf_exempt, name = 'dispatch')
class ElectricityBillView(View):
    def post(self, request):
        data = json.loads(request.body)
        units = data.get("units")
        rate = data.get("rate")
        amount = units * rate
        result = {
            "units" : units,
            "rate" : rate,
            "amount" : amount
        }
        return JsonResponse(result)