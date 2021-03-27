import os

from django.shortcuts import render, redirect
from .forms import UploadLinkForm, ColumnsForm
import json
from csv import reader
import csv
import pandas as pd
import requests
import urllib.request
from io import StringIO

# Create your views here.
def index(request):
    context = {}
    form = UploadLinkForm()
    context['form'] = form

    if request.POST:
        url = request.POST.get('link_field', False)
        response = urllib.request.urlopen(url)

        # parse the file object
        download(url)
        return redirect(result)
    return render(request, "index.html", context)



def download(url: str):
    global completename
    req = requests.get(url)
    print(req.url)
    # output some object attributes
    filename = req.url[(url).rfind('/') + 1:]

    #save the file in data folder
    folder = 'data'
    completename = os.path.join(folder,filename )
    print(completename) #saving the file in folder name data
    with open(completename, 'wb') as f:
        for chunk in req.iter_content(chunk_size=8191):
            if chunk:
                f.write(chunk)
                os.fsync(f.fileno())
                #f.close()
    readfile(completename)

def readfile(filename):

    global columns, data
    my_file = pd.read_csv(filename, sep='[:;,|_]', engine='python')

    data = pd.DataFrame(data=my_file, index=None)
    print(data)



def result(request):
    context = {}
    context['form'] = ColumnsForm()

    rows = len(data.axes[0])
    columns = len(data.axes[1])


    print('cols', columns)
    print('rows', rows)


    return render(request, "result.html", context)