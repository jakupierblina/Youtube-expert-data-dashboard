from django.shortcuts import render, redirect
from .forms import UploadLinkForm, ColumnsForm
import csv
import json
import urllib.request

from io import StringIO

# Create your views here.
def index(request):
    context = {}
    form = UploadLinkForm()
    context['form'] = form
    if request.POST:
        temp = request.POST.get('link_field', False)
        response = urllib.request.urlopen(temp)
        data = json.loads(response.read())
        print(data)
        return redirect(result)
    return render(request, "index.html", context)


def result(request):
    context = {}
    context['form'] = ColumnsForm()
    return render(request, "result.html", context)