from django.shortcuts import render
from django.db.models import Q

# Create your views here.
from django.views.generic import ListView
from categoryApp.models import Product

class SearchProductView(ListView):
    template_name = "search/result.html"
    def get_context_data(self, *args, **kwargs):
        context = super(SearchProductView, self).get_context_data(*args, **kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        return context

    def get_queryset(self, *args, **kwargs):
        query = self.request.GET.get('q', None) # method_dict['q']
        print(query+'s')
        if query is not None:
            return Product.objects.filter(Q(title__icontains=query)|Q(company__icontains=query)|Q(model__icontains=query))

        '''
        __icontains = field contains this
        __iexact = fields is exactly this
        '''
