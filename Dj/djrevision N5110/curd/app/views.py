from audioop import reverse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView
from app.models import Book,Tag,Author
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.shortcuts import redirect
# Create your views here.

class Bookk(ListView):
    template_name = 'app/list.html'
    model = Book
    # queryset = Book.objects.order_by('-id')
    context_object_name = 'bb'

class Booktails(DetailView):
    template_name = 'app/display.html'
    model = Book

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        # context['tags'] = self.object.tag.all()
        # self.object = Book.objects.get(pk=self.kwargs['pk'])
        context['name'] = self.object.author
        return context

class BookDELETE(DeleteView):
    template_name = 'app/delete.html'
    model = Book  
    success_url ="/book"

class Bookup(UpdateView):
    template_name = 'app/update.html'
    model = Book  
    success_url ="/book" 

    fields = [
        "name",
        'img',
        "rating",
        'author',
        'tag'
    ]

class BCreate(CreateView):
    template_name = 'app/create.html'
    model = Book
    fields = ['name','img','rating','tag']   
    success_url = reverse_lazy('thx')
    # success_url = redirect('thx')
    def post(self, request, *args, **kwargs):
        self.object = None
        return super(BCreate).post(request, *args, **kwargs)
"""
    def post(self, request):
        super(BCreate,self).post(request)
        print(self.request.POST['name'])
        # return redirect('/thx')

    def get_success_url(self):
        return reverse_lazy('thx')
"""        

class Bthx(TemplateView):
    template_name = 'app/thx.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # reviewid = kwargs['username']
        # reviews = Review.objects.get(username =reviewid)
        context["message"] = Book.objects.order_by('-id')[0]
        print(context)
        return context 