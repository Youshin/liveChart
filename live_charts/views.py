# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import JsonResponse
from live_charts.models import Bar

def sendData(request):
    if request.is_ajax():
        datas = Bar.objects.all()
        #bar = []
        labels = []
        datasets = []
        for data in datas:
            labels.append(data.label)
            datasets.append(data.data)
        bar = dict(labels=labels, datasets=datasets)
        return JsonResponse({'bar':bar})
    else:
        return JsonResponse({'data': None})

def index(request):
    return render(request, 'barChart.html')