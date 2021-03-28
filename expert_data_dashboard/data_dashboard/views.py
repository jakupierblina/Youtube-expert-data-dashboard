import os

from django.shortcuts import render, redirect
from .forms import UploadLinkForm, ColumnsForm, VizualizationForm
import json
from csv import reader
import csv
from collections import Counter
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

    global columns
    columns = []
    for col_name in data.columns:
        columns.append(col_name)
        #print(col_name)

    print('columns', columns) # created the list of array with columns name



def result(request):
    context = {}

    vizualization_form = VizualizationForm()
    context['vizualization_form'] = vizualization_form

    #creating choices based on columns name of the file
    columns_list = []
    for i in columns:
        columns_list.append((i, i))
    #print(columns_list)

    columns_form = ColumnsForm(columns_list)
    context['columns_form'] = columns_form


    if request.GET:
        vizualization_choice = request.GET['vizualization_field']
        columnsname_choice = request.GET['columns_field']
        print('vizualization_choice', vizualization_choice)
        print('columnsname_choice', columnsname_choice)
        dashboard_dict = vizualization(columnsname_choice)
        #print('dashboard_dict',dashboard_dict)


    return render(request, "result.html", context)




# get and return the prepared dictionary data from columns name of visualization
def vizualization(name_input):
    dashboard1 = []

    for x in data[name_input]:
        dashboard1.append(x)

    my_dict = dict(Counter(dashboard1))
    return my_dict