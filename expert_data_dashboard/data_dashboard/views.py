from django.shortcuts import render, redirect
from .forms import UploadLinkForm, ColumnsForm
import json
from csv import reader
import csv
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
        req = requests.get(url)
        print(req.url)
        # output some object attributes
        filename = req.url[(url).rfind('/')+1:]
        with open(filename, 'wb') as f:
            for chunk in req.iter_content(chunk_size=8191):
                if chunk:
                    f.write(chunk)
        return redirect(result)
    return render(request, "index.html", context)


def result(request):
    context = {}
    context['form'] = ColumnsForm()
    return render(request, "result.html", context)