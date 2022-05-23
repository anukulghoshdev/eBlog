from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView, View, TemplateView

from App_Blog.models import Blog, Comment, Likes

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy #kaj na houa obdi redirect kore na

from django.contrib.auth.decorators import login_required # function based view te decorator use hoy
from django.contrib.auth.mixins import LoginRequiredMixin # class based view te mixins use korte hoy

# unique_id generate kore
import uuid

from App_Blog.forms import CommentForm

# def blog_list(request):
#     return render(request, 'App_Blog/blog_list.html', context={})




class Blog_list(ListView):
    context_object_name = 'blogs'
    model = Blog
    template_name = 'App_Blog/blog_list.html'
    # queryset = Blog.objects.order_by('-publish_date')




#context_object_name, model, fields, template_name, success_url
class CreateBlog(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = 'App_Blog/create_blog.html'
    fields = ('blog_title', 'blog_content', 'blog_image')

    def form_valid(self, form): #form submit korar por  ei fun ta kaj kore
        blog_objs = form.save(commit=False)
        blog_objs.author = self.request.user


        title = blog_objs.blog_title
        new_title = ''.join(char for char in title if char.isalnum())
        blog_objs.slug = new_title + "-" + str(uuid.uuid4())   #blog_objs.slug = title.replace(" ", "-") + "-" + str(uuid.uuid4())
        blog_objs.save()
        return HttpResponseRedirect(reverse('index'))





@login_required
def blog_details(request, slug):
    blog = Blog.objects.get(slug=slug)
    comment_form = CommentForm()

    already_liked = Likes.objects.filter(blog=blog, user=request.user)
    if already_liked:
        liked = True
    else:
        liked = False

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.blog = blog
            comment.save()
            return HttpResponseRedirect(reverse('Blog:blog_details', kwargs={'slug':slug}))


    return render(request, 'App_Blog/blog_details.html', context={'blog':blog, 'comment_form':comment_form, 'liked':liked})





@login_required
def liked(request, pk):
    blog = Blog.objects.get(pk = pk)
    user = request.user

    already_liked = Likes.objects.filter(blog=blog, user=user)
    if not already_liked:
        like_post = Likes(blog=blog, user=user)
        like_post.save()

    return HttpResponseRedirect(reverse('Blog:blog_details', kwargs={'slug': blog.slug }))




@login_required
def unliked(request, pk):
    blog = Blog.objects.get(pk=pk)
    user = request.user
    already_liked = Likes.objects.filter(blog=blog, user=user)
    already_liked.delete()
    return HttpResponseRedirect(reverse('Blog:blog_details', kwargs={'slug':blog.slug}))



class my_blogs(LoginRequiredMixin, TemplateView):
    template_name = 'App_Blog/my_blogs.html'


class update_blog(LoginRequiredMixin, UpdateView):
    model = Blog
    fields = ('blog_title', 'blog_content', 'blog_image')
    template_name = 'App_Blog/update_blog.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('Blog:blog_details', kwargs={'slug':self.object.slug})
