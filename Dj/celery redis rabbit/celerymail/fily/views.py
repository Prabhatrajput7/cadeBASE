from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from docx2pdf import convert
from .task import *
from celery.result import AsyncResult
# Create your views here.

def upload_file(request):
    if request.method == 'POST':
        myfile = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name , myfile)
        # # the fileurl variable now contains the url to the file. This can be used to serve the file when needed
        fileurl = fs.url(filename)
        # print(fileurl)
        convert(f'doctopdf/ + {myfile.name}')
        # data = convert_doc_to_pdf.delay(myfile.name)
        return HttpResponseRedirect('data.task_id')

    return render(request,'fily/file.html')

def check_status(request , task_id):
    #  res is to know task completed or not true or false check template for more
    res = AsyncResult(task_id)
    print(res.ready())
    context = {'task_status': res.ready()}
    return render(request , 'fily/progress.html' , context)    