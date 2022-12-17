from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic import CreateView
from app.models import Genre,Language,Book,BookInstance,Author
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.urls import reverse
from django.http import HttpResponseRedirect
from app.forms import Ussr
from django.contrib import messages
# Create your views here.


class HomeCount(LoginRequiredMixin,ListView):
    template_name = 'app/count.html'
    context_object_name = 'ggenre'
    model = Genre

    def get_context_data(self, **kwargs):
        context = super(HomeCount, self).get_context_data(**kwargs)
        context.update({
            'lang': Language.objects.all().count(),
            'bk': Book.objects.all().count(),
            'bi': BookInstance.objects.all().count(),
            'ath': Author.objects.all().count(),
        })
        return context

    def get_queryset(self):
        return Genre.objects.all().count()


class BBK(LoginRequiredMixin,CreateView):
    template_name = 'app/book.html'
    model = Book
    fields = '__all__'
    success_url = reverse_lazy('thx')

class ListBook(ListView):
    template_name = 'app/listbook.html'
    context_object_name = 'bbk'
    # model = Book
    queryset = Book.objects.order_by('id')    

class Book_detail(DetailView):
    template_name = 'app/display.html'
    model = Book

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['bdetail'] = self.object
        context['genres'] = self.object.genre.all()
        context['g'] = 'Genre'
        request = self.request #fetch row from data
        favid = request.session.get('favrev') #4 for termite
        context['favkey'] = favid == str(context['bdetail'].id)
        return context
        
    def post(self, request, *args, **kwargs):
        try:
            if request.POST["delfav"]:
                delbook = request.POST["delfav"]
                del request.session['favrev']
                return HttpResponseRedirect(delbook)
        except:
            print(request.POST["favbook"],type(request.POST["favbook"]))
            favv = request.POST["favbook"]
            request.session['favrev'] = favv
            return HttpResponseRedirect(favv)
            # it takes the entered url and add  fav in str or int section and load the page


def thx(request):
    return render(request,'app/thx.html',{'name':Book.objects.order_by('-id')[0]})

@login_required
def logreq(request):
    return render(request,'app/logreq.html')




class SignUpView(CreateView):
    form_class = Ussr
    # form_class = UserCreationForm 
    success_url = reverse_lazy('login')
    template_name = 'app/signup.html'    
    

class CheckedOutBooksByUserView(LoginRequiredMixin,ListView):
    # List all BookInstances BUT I will filter based off currently logged in user session
    model = BookInstance 
    template_name = 'app/profile.html'
    paginate_by = 5 # 5 book instances per page

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user)     


