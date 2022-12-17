from django.shortcuts import render
from django.views.generic.edit import CreateView, FormView
from app.forms import FF,FFM
from app.models import Imgg
from django.http import HttpResponseRedirect
from django.views.generic.base import View
# Create your views here.
"""
def Fileup(request):
    if request.method =='POST':
        form = FF(request.POST, request.FILES)
        if form.is_valid():
            # print('request file ',request.FILES['imagee'])
            print('cdata ',form.cleaned_data)
            print('cdata2 ',form.cleaned_data['img'])
            print('user ',request.user)
            Imgg.objects.create(img = form.cleaned_data['img'], user = request.user)
            return HttpResponseRedirect('/thx')
    else:
        form = FF()
    return render(request,'app/img.html',{'form':form})
"""
def Fileup(request):
    if request.method =='POST':
        form = FFM(request.POST, request.FILES)
        if form.is_valid():
            pic = form.save(commit=False)
            pic.user = request.user
            pic.save()
            # Imgg.objects.create(img = form.cleaned_data['img'], user = request.user)
            # form.save()
            # print('request file ',request.FILES['image'])
            # print('cdata ',form.cleaned_data)
            # print('cdata2 ',form.cleaned_data['img'])
            # Imgg.objects.create(img = request.FILES['image'], user = request.user)
            return HttpResponseRedirect('/thx')
    else:
        form = FFM()
    return render(request,'app/img.html',{'form':form})    

class Fileimg(CreateView):
    model = Imgg
    form_class = FFM
    template_name = 'app/img.html'
    success_url = '/thx'  

class Thx(View):
  def get(self, request, *args, **kwargs):
        return render(request, "app/thx.html")     












"""
class FileFieldFormView(FormView):
    form_class = FileFieldForm
    template_name = 'upload.html'  # Replace with your template.
    success_url = '...'  # Replace with your URL or reverse().

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        if form.is_valid():
            for f in files:
                ...  # Do something with each file.
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
"""
