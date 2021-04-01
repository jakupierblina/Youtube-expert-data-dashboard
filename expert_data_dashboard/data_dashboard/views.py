import os

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import  UploadLinkForm, ColumnsForm, VizualizationForm
from .models import UploadLinkModel
from django.core.files.storage import FileSystemStorage

from collections import Counter
import pandas as pd
import requests
import urllib.request
from django.conf import settings

from io import StringIO

# Create your views here.
def index(request):
    context = {}


    if request.method == 'POST':

        link_form = UploadLinkForm(request.POST)
        uploaded_file = request.FILES['document']


        if link_form.is_valid() or uploaded_file :

            url = request.POST.get('link_field', False)

            files_name = uploaded_file.name



            # if both forms are empty
            if not files_name and not url:
                messages.warning(request, 'Warning: Input is required. Please chose only ONE of the forms!')
                return redirect(index)

            # if the user chosed both forms
            if files_name and url:
                messages.warning(request, 'Warning:  Please chose only ONE of the forms!')
                return redirect(index)


            # if user chosed a link
            if not files_name:
                print('you chosed to upload a link')
                response = urllib.request.urlopen(url)
                # parse the file object
                download(url)
                return redirect(result)

            # if user chosed a file
            elif not url:
                print('you chosed to upload a file')
                if uploaded_file.name.endswith('.csv'):
                    savefile = FileSystemStorage()

                    name = savefile.save(uploaded_file.name, uploaded_file)  # gets the name of the file
                    print(name)

                    # we need to save the file somewhere in the project, MEDIA
                    # now lets do the savings

                    d = os.getcwd()  # how we get the current dorectory
                    file_directory = d + '\media\\' + name  # saving the file in the media directory
                    print(file_directory)
                    readfile(file_directory)
                    return redirect(result)


                    #return HttpResponse('<html><body>111 </body></html>')
                else:
                    messages.warning(request, 'File was not uploaded. Please use .csv file extension!')
                    return redirect(index)



    # starting
    else:
        link_form = UploadLinkForm()
        context['link_form'] = link_form

        return render(request, "index.html", context)


def readfile(filename):

    #we have to create those in order to be able to access it around
    # use panda to read the file because i can use DATAFRAME to read the file
    #column;culumn2;column
    global rows, columns, data

    my_file = pd.read_csv(filename, sep='[:;,|_]')

    data = pd.DataFrame(data=my_file, index=None)
    print(data)

    rows = len(data.axes[0])
    columns = len(data.axes[1])



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
    for i in data.columns:
        columns_list.append((i, i))
    # columns_list = ( ('x1','x1'), ('x2','x2)) ....

    columns_form = ColumnsForm(columns_list)
    context['columns_form'] = columns_form # pass this list of choices in html template

    dashboard_dict = vizualization(data.columns[0])
    columnsname_choice = data.columns[0] # prepare the defaulted columns representation
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