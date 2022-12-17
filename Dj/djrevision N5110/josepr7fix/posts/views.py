from wsgiref.util import request_uri
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404
from django.views import generic
from braces.views import SelectRelatedMixin
from . import forms
from . import models
from grps.models import Group
from .forms import SelGrp
from django.contrib.auth import get_user_model
User = get_user_model()


class PostList(SelectRelatedMixin, generic.ListView):
    model = models.Post
    select_related = ("user", "group")

# class UserPosts(generic.ListView):
#     model = models.Post
#     template_name = "posts/user_post_list.html"

#     def get_queryset(self):
#         try:
#             self.post_user = User.objects.prefetch_related("posts").get(
#                 username__iexact=self.kwargs.get("username")
#             )
#         except User.DoesNotExist:
#             raise Http404
#         else:
#             return self.post_user.posts.all()

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["post_user"] = self.post_user
#         return context

class UserPosts(generic.ListView):
    model = models.Post
    template_name = "posts/user_postpr7.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_user"] = models.Post.objects.filter(user__username = self.kwargs.get("username"))
        return context



class PostDetail(SelectRelatedMixin, generic.DetailView):
    model = models.Post
    select_related = ("user", "group")

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     return queryset.filter(
    #         user__username__iexact=self.kwargs.get("username")
    #     )
    #     """
    #     return queryset.filter(
    #         user__username__iexact=self.kwargs.get("username"),id = self.kwargs.get("pk")
    #     )
    #     """


class CreatePost(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    # form_class = forms.PostForm
    form_class = SelGrp
    model = models.Post

    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     kwargs.update({"user": self.request.user})
    #     return kwargs

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


def WritePost(request,slug):
    if request.method =='POST':
        f = SelGrp(request.POST)
        if f.is_valid():
            formy = f.save(commit=False)
            formy.user = request.user
            sg = Group.objects.get(slug=slug)
            formy.group = sg
            formy.save()
            return redirect('posts:all')
    else:
        f = SelGrp()
    return render(request,'posts/post_form.html',{'form':f})



class DeletePost(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
    model = models.Post
    select_related = ("user", "group")
    success_url = reverse_lazy("posts:all")

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     print(Group.objects.get(slug='dogs'))
    #     return queryset.filter(user_id=self.request.user.id)

    # def delete(self, *args, **kwargs):
    #     messages.success(self.request, "Post Deleted")
    #     return super().delete(*args, **kwargs)
