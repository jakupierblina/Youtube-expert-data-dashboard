from django.shortcuts import render, redirect
from .forms import UploadLinkForm, ColumnsForm
import json
from csv import reader
import csv
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

        # parse json object

        # output some object attributes


        return redirect(result)
    return render(request, "index.html", context)


def result(request):
    context = {}
    context['form'] = ColumnsForm()
    return render(request, "result.html", context)