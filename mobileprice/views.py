from pydoc import render_doc
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
import joblib

# Create your views here.
def home(request):
    return render(request, 'home.html')

def result(request):
    clf = joblib.load('finalized_model.sav')

    lis = []

    lis.append(request.GET['battery_power'])
    lis.append(request.GET['clock_speed'])
    lis.append(request.GET['fc'])
    lis.append(request.GET['int_memory'])
    lis.append(request.GET['m_dep'])
    lis.append(request.GET['mobile_wt'])
    lis.append(request.GET['n_cores'])
    lis.append(request.GET['pc'])
    lis.append(request.GET['px_height'])
    lis.append(request.GET['px_width'])
    lis.append(request.GET['ram'])
    lis.append(request.GET['sc_h'])
    lis.append(request.GET['sc_w'])
    lis.append(request.GET['talk_time'])

    ans = clf.predict([lis])


    return render(request, 'result.html',{'ans':ans,'lis':lis})
