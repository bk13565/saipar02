from django.views import generic
from .models import Post

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('created_on')
    template_name = "blog/index.html" 

class PostDetail(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"


# class LeadDetailView(LoginRequiredMixin, generic.DetailView):
#     template_name = "leads/lead_detail.html"
#     # queryset = Lead.objects.all()
#     context_object_name = "lead"
    
