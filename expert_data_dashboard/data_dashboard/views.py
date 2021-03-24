from django.shortcuts import render,redirect
from .forms import UploadLinkForm,ColumnsForm

# Create your views here.
def index(request):
    context = {}
    form = UploadLinkForm()
    context['form'] = form
    if request.POST:
        temp = request.POST.get('link_field', False)
        print(temp)
        return redirect(result)
    return render(request, "index.html", context)


def result(request):
    context = {}
    context['form'] = ColumnsForm()
    return render(request, "result.html", context)