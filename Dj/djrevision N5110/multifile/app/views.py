from django.shortcuts import render,redirect
from app.models import MultiF

# Create your views here.

from django.views.generic.list import ListView

class HuskyL(ListView):
    template_name = 'app/lst.html'
    model = MultiF
    # queryset = Book.objects.order_by('-id')
    context_object_name = 'bb'



def thx(request):
    return render(request,'app/thx.html')

from django.views.generic.edit import FormView
from .forms import FileFieldForm
from django.urls import reverse_lazy

class FileFieldFormView(FormView):
    form_class = FileFieldForm
    template_name = 'app/multi2.html'  # Replace with your template.
    success_url = reverse_lazy('thx')  # Replace with your URL or reverse().

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        name = request.POST['name']
        files = request.FILES.getlist('file_field')
        if form.is_valid():
            for f in files:
                MultiF.objects.create(name = name, file= f)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)



"""
def multi(request):
    if request.method=='POST':
        name = request.POST['name']
        files = request.FILES.getlist('files')
        for f in files:
            MultiF.objects.create(name = name, file= f)
        return redirect('thx')
    else:
        return render(request,'app/multi.html')

"""            


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

 widgets = {
            'img': forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
        }            
"""    