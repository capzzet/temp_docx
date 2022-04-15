from django.http import HttpResponse
from django.shortcuts import render, redirect
from docxtpl import DocxTemplate
import os
import mimetypes
import pythoncom
from docx2pdf import convert
from pathlib import Path
menu = [{'title': "Главная", 'url_name': 'home'},
        {'title': "Резюме", 'url_name': 'resume'},
        {'title': "О нас", 'url_name': 'about'},
        {'title': "Блог", 'url_name': 'blog'}, ]
def index(request):
    context = {
        'menu':menu
    }
    return render(request, 'resume/html/index.html',context)

def about(request):
    context = {
        'menu': menu
    }
    return render(request, 'resume/html/about.html',context)

def blog(request):
    context = {
        'menu': menu
    }
    return render(request, 'resume/html/blog.html',context)

def resume(request):
    context = {
        'menu': menu,
    }
    if request.method == 'POST':
        pythoncom.CoInitializeEx(0)
        doc = DocxTemplate(rf'{Path(__file__).resolve().parent.parent}/resume/templates_docx/blank-rezume-{request.POST["doc_template"]}.docx')
        context = {'company': request.POST['job_start'], 'doo': request.POST['name'],'photo':request.POST['wage']}
        doc.render(context)
        doc.save('resume.docx')
        in_file = os.path.abspath(rf'{Path(__file__).resolve().parent.parent}\resume.docx')
        out_file = os.path.abspath(rf'{Path(__file__).resolve().parent.parent}\resume.pdf')
        convert(in_file, out_file)
        return redirect('download')
    return render(request, 'resume/html/resume.html',context)

def download(request):
    filename = 'resume.pdf'
    filepath = rf'{Path(__file__).resolve().parent.parent}\resume.pdf'
    with open(filepath, 'r',errors='ignore',encoding='utf-8') as path:
        mime_type, _ = mimetypes.guess_type(filepath)
        response = HttpResponse(path, content_type=mime_type)
        response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response


def custom_page_not_found_view(request, exception):
    return render(request, "resume/errors/404.html", {})

def custom_error_view(request, exception=None):
    return render(request, "resume/errors/500.html", {})

def custom_permission_denied_view(request, exception=None):
    return render(request, "resume/errors/403.html", {})

def custom_bad_request_view(request, exception=None):
    return render(request, "resume/errors/400.html", {})