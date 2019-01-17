from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404

from ..models import Blog


class BlogDetailView(ListView):
    template_name = 'blogs/blog_detail.html'
    # model = Blog
    slug_field = 'slug'
    slug_url_kwarg = 'blog_slug'
    context_object_name = 'posts'
    paginate_by = 4

    def get_queryset(self):
        self.blog = get_object_or_404(Blog, **{'slug': self.kwargs['blog_slug']})
        return self.blog.posts.published()

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        # context['featured_post'] = context['blog'].published().featured()
        # context['featured_post'] = context['blog'].posts.all()
        context['blog']=self.blog
        return context


class BlogListView(ListView):
    template_name = 'blogs/blog_list.html'
    context_object_name = 'blogs'
    paginate_by = 20
