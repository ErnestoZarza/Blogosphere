from django.views.generic import ListView, DetailView, TemplateView
from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404
from django.utils.translation import ugettext_lazy as _

from ..models import Post, Blog, Comment


class PostListView(ListView):
    template_name = 'blogs/post_list.html'
    context_object_name = 'post'
    queryset = Post.objects.published()
    paginate_by = 15

    def get_queryset(self):
        qs = super(PostListView, self).get_queryset()
        return qs


class PostDetailView(TemplateView):
    # model = Post
    queryset = Post.objects.published()
    # context_object_name = 'post'
    # slug_url_kwarg = 'post_slug'
    template_name = 'blogs/post_detail.html'

    # def get_queryset(self, *args, **kwargs):
    #     # try:
    #     #     self.post = Post.objects.published().get(slug=self.kwargs['post_slug'], blog__slug=self.kwargs['blog_slug'])
    #     # except:
    #     #     raise Http404(_('La url del post es incorrecta'))
    #
    #     return Post.objects.published()

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        try:
            context['post'] = Post.objects.published().get(slug=self.kwargs['post_slug'],
                                                           blog__slug=self.kwargs['blog_slug'])
        except:
            raise Http404(_('La url del post es incorrecta'))

        return context

    def post(self, request, *args, **kwargs):

        cm_name = request.POST.get('name', '')
        cm_email = request.POST.get('email', '')
        cm_content = request.POST.get('content', '')
        cm_ip = request.META.get('REMOTE_ADDR')

        # comment = Comment.objects.create(name=cm_name, email=cm_email, content=cm_content, ip=cm_ip)

        post = Post.objects.published().get(slug=self.kwargs['post_slug'], blog__slug=self.kwargs['blog_slug'])
        post.comments.create(name=cm_name, email=cm_email, content=cm_content, ip=cm_ip)

        return redirect(post.get_absolute_url())
