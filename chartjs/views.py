from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View
import pandas as pd

#from rest_framework.response import Response

dataa = pd.read_csv('nba2k20-full.csv')
#print(dataa.full_name.tolist())
#print(dataa.rating.tolist())

def Home(request):
    return render(request,'chartjs/home.html')

class IndexView(View):
        def get(self,request, *args,**kwargs):
            return render(request,'chartjs/index.html')


def get_data(request, *args, **kwargs):
    labels = dataa.full_name.tolist()
    
    chartLabel = "Top Rated NBA Players"
    chartdata = dataa.rating.tolist()
    
    data={
        'labels': labels,
        'chartLabel': chartLabel,
        'chartdata': chartdata,
    }

    return JsonResponse(data)