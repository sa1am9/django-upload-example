from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .forms import ReportForm
from .models import Report
from django.http import HttpResponse
import xlsxwriter
import mimetypes


class Home(TemplateView):
    template_name = 'home.html'


def delete_report(request, pk):
    if request.method == 'POST':
        report = Report.objects.get(pk=pk)
        report.delete()
    return redirect('reports_list')

def download_file(request, pk):
    # fill these variables with real values
    file = open('testfile.txt', 'a+')
    report = get_object_or_404(Report, pk=pk)
    file.write(report.name)
    response = HttpResponse(file)

    response['Content-Disposition'] = "attachment; filename=testfile.txt"
    return response


class ReportListView(ListView):
    model = Report
    template_name = 'reports_list.html'
    context_object_name = 'reports_list'


class UploadDataView(CreateView):
    model = Report
    form_class = ReportForm
    success_url = reverse_lazy('reports_list')
    template_name = 'upload_data.html'
