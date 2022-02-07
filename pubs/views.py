from django.shortcuts import render
from django.views import generic

from .models import OccasionalPaperModel, DiscussionPapersModel, ReportsModel, ZSSJModel, SAIPARBookshelfModel

# Create your views here.
class PublicationsView(generic.ListView):
    template_name ="pubs/publications.html"
    context_object_name = "publications"
    
    def get_queryset(self):
        queryset = self.ordered_pub_date(OccasionalPaperModel)
        return queryset
    
    def ordered_pub_date(self, object):
        # docs = list(OccassionalPapersModel.objects.all().order_by('pub_date'))
        docs = list(object.objects.all().order_by('pub_date'))
        doc_dict = {}
        for doc in docs:
            yr = (doc.pub_date).strftime("%Y")
            if yr in doc_dict:
                doc_dict[yr].append(doc)
            else:
                doc_dict[yr] = [doc]
        # sort then convert it back to a dictionary
        doc_dict = dict(sorted(doc_dict.items(), key=lambda x: x[0], reverse=True))
        return doc_dict

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        discussion_papers = self.ordered_pub_date(DiscussionPapersModel)
        reports = self.ordered_pub_date(ReportsModel)
        zssj = self.ordered_pub_date(ZSSJModel)
        
        books = SAIPARBookshelfModel.objects.all()
        e_articles = books.filter(book_type=0)
        e_books = books.filter(book_type=1)
        print_books = books.filter(book_type=2)
        
        context.update({
            "discussion_papers": discussion_papers,
            "reports": reports,
            "zssj" : zssj,
            "eBooks": e_books,
            "eArticles" : e_articles,
            "print_books" : print_books,
        })
        return context
