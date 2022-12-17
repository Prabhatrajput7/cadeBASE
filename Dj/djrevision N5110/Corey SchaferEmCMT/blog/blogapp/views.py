from .models import Comment
from django.shortcuts import render,get_object_or_404,redirect
from blogapp.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView,DetailView,CreateView,UpdateView,DeleteView)
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormMixin
from .forms import CommentForm,CommentForm2
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.forms import inlineformset_factory
from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied
#  to show one form multiple time
# Create your views here.


class BlogList(LoginRequiredMixin,ListView):
    template_name = 'blogapp/home.html'
    model = Post
    context_object_name = 'r6'
    ordering = ['-date_posted']
    paginate_by = 5
    # def get_queryset(self):
    #     return Post.objects.order_by('-id')

class UserPostListView(LoginRequiredMixin,ListView):
    model = Post
    template_name = 'blogapp/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        # user = get_object_or_404(User, username=self.kwargs.get('username'))
        # return Post.objects.filter(author=user).order_by('-date_posted') 
        return Post.objects.filter(author__username=self.kwargs.get('username')).order_by('-date_posted')    

class BlogDetailView(DetailView,FormMixin):
    model = Post    
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        if 'post/ucomment/' in self.request.path:
            c = Comment.objects.get(id=self.kwargs['pk2'])
            context['form2'] = CommentForm2(initial={'content':c.content})
            context['comm'] = Comment.objects.filter(pst=self.kwargs['pk'],reply=None).exclude(id=c.id)
            print('insideelse',context['comm'])
            return context
        else:
            context['form'] = CommentForm()
        # context['comm'] = Post.objects.get(id=self.kwargs['pk']).comment_set.all().order_by('-pk')
        context['comm'] = Comment.objects.filter(pst=self.kwargs['pk'])
        print('else',context['comm'])
        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if 'post/ucomment/' in self.request.path:
            print('up')
            c = Comment.objects.get(id=self.kwargs['pk2'])
            c.content = request.POST.get('content')
            c.save()
            return HttpResponseRedirect(reverse('blogapp:detail', args=[self.kwargs['pk']])) 
        elif form.is_valid():
            print('down')
            form.instance.content = request.POST.get('content')
            form.instance.reply_id = request.POST.get('cid')
            form.instance.cby = self.request.user
            form.instance.pst = Post.objects.get(pk = self.kwargs['pk'])
            form.save()
            return HttpResponseRedirect(reverse('blogapp:detail', args=[self.kwargs['pk']])) 
        else:
            return self.form_invalid(form)


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    # if there is no success url is present it will look into get abosulte url

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form) 

    def test_func(self):
        post = self.get_object()
        #  self.get_object() this will get the post that we currently trying to update
        if self.request.user == post.author:
            return True
        return False    

class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False                   

@login_required
def about(request):
    return render(request, 'blogapp/about.html')  

   
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    success_url = '/'

    def test_func(self):
        comnt = self.get_object()
        if self.request.user == comnt.cby:
            return True
        return False 

# def checking(self):
#         comnt = get_object_or_404(Comment, id=self.pk)
#         if self.request.user == comnt.cby:
#             return True
#         return False        

# @user_passes_test(checking)
@login_required
def dcomment(request,pk):
    cmdelete = Comment.objects.get(pk=pk)   
    if request.user == cmdelete.cby:    
        cmdelete.delete()
        return HttpResponseRedirect(reverse('blogapp:detail', kwargs={'pk': cmdelete.pst.pk}))
    else:
        raise PermissionDenied


def ucomment(request,pk):
    pass
    # cmdelete = Comment.objects.get(pk=pk) 
    # if request.method == 'POST':
    #     uu_form = UserUpdateForm(request.POST,instance=request.user)
    #     profile_form = ProfileUpdateForm(request.POST, request.FILES ,instance=request.user.profile)

    #     if uu_form.is_valid() and profile_form.is_valid():
    #         uu_form.save()
    #         profile_form.save()
    #         messages.success(request, f'Your account has been updated!')
    #         return redirect('profile')
    
    # else:
    #     uu_form = UserUpdateForm(instance=request.user)
    #     profile_form = ProfileUpdateForm(instance=request.user.profile)

    # context = {
    #     'uu_form': uu_form,
    #     'profile_form': profile_form
    # }

    # return render(request,'users/profile.html',context)    