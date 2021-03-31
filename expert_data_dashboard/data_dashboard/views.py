import os

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import UploadFileForm, UploadLinkForm, ColumnsForm, VizualizationForm
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


    if request.POST:
        link_form = UploadLinkForm(request.POST, prefix="link")
        file_form = UploadFileForm(request.POST, prefix="file")
        if link_form.is_valid() or file_form.is_valid():

            url = request.POST.get('link_field', False)
            file = request.POST.get('file', False)

            # if both forms are empty
            if not file and not url:
                messages.warning(request, 'Warning: Input is required. Please chose only ONE of the forms!')
                return redirect(index)

            # if the user choosed both forms
            if file and url:
                messages.warning(request, 'Warning:  Please chose only ONE of the forms!')
                return redirect(index)


            # if user chosed a link
            if not file:
                print('you chosed to upload a link')
                response = urllib.request.urlopen(url)
                # parse the file object
                download(url)
                return redirect(result)

            # if user chosed a file
            elif not url:
                print('you chosed to upload a file')
                return HttpResponse('<html><body>111 </body></html>')


    # starting
    else:
        link_form = UploadLinkForm()
        context['link_form'] = link_form
        file_form = UploadFileForm()
        context['file_form'] = file_form
        return render(request, "index.html", context)



def download(url: str):
    global completename
    req = requests.get(url)
    #print(req.url)
    # output some object attributes
    filename = req.url[(url).rfind('/') + 1:]

    #save the file in data folder
    folder = 'data'
    completename = os.path.join(folder,filename )
   # print(completename) #saving the file in folder name data
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
    #print(data)

    global columns
    columns = []
    for col_name in data.columns:
        columns.append(col_name)
        #print(col_name)

    #print('columns', columns) # created the list of array with columns name



def result(request):
    context = {}

    # create the ChartJs Choice field
    vizualization_form = VizualizationForm()
    # pass the form in html
    vizualization_default = 'bar'
    context['vizualization_default'] = vizualization_default
    context['vizualization_form'] = vizualization_form


    # creating choices based on columns name of the file
    columns_list = []
    for i in columns:
        columns_list.append((i, i))
    # columns_list = ( ('x1','x1'), ('x2','x2)) ....

    columns_form = ColumnsForm(columns_list)
    context['columns_form'] = columns_form # pass this list of choices in html template

    dashboard_dict = vizualization(columns[0])
    columnsname_choice = columns[0] # prepare the defaulted columns representation
    context['columnsname_choice'] = columnsname_choice

    #print('default', dashboard_dict)
    keys = dashboard_dict.keys()  # {'A121', 'A122', 'A124', 'A123'}
    values = dashboard_dict.values()

    listkeys = []
    listvalues = []

    for x in keys:
        listkeys.append(x)

    for y in values:
        listvalues.append(y)

    #print('---->', listkeys)
    #print('---->', listvalues)
    context['listkeys'] = listkeys
    context['listvalues'] = listvalues


    # if the page is been updated change the attributes
    if request.GET:
        columnsname_choice = request.GET['columns_field']
        #print('columnsname_choice', columnsname_choice)
        context['columnsname_choice'] = columnsname_choice # put this vizualization in the html title

        dashboard_dict = vizualization(columnsname_choice)
        #print('dashboard_dict',dashboard_dict)

        listkeys = []
        listvalues = []

        keys = dashboard_dict.keys()
        values = dashboard_dict.values()
        for x in keys:
            listkeys.append(x)

        for y in values:
            listvalues.append(y)

        #print('---->', listkeys)
        #print('---->', listvalues)
        context['listkeys'] = listkeys
        context['listvalues'] = listvalues


        # choosen visualization style
        vizualization_choice = request.GET['vizualization_field']
        vizualization_default = vizualization_choice
        context['vizualization_default'] = vizualization_default


    return render(request, "result.html", context)




# get and return the prepared dictionary data from columns name of visualization
def vizualization(name_input):
    dashboard1 = []

    for x in data[name_input]:
        dashboard1.append(x)

    my_dict = dict(Counter(dashboard1))
    return my_dict