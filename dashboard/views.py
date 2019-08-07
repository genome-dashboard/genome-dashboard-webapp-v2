from django.shortcuts import render
from django.views import generic

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'dashboard/index.html'

    def get_queryset(self):
        """
        Return an empty context object for index view.
        """
        index_context_object = []
        context = {'index_context_object': index_context_object}
        return context


class D1View(generic.ListView):
    template_name = 'dashboard/d1.html'

    def get_queryset(self):
        """
        Return an empty context object for index view.
        """
        index_context_object = []
        context = {'index_context_object': index_context_object}
        return context


class D2View(generic.ListView):
    template_name = 'dashboard/d2.html'

    def get_queryset(self):
        """
        Return an empty context object for index view.
        """
        index_context_object = []
        context = {'index_context_object': index_context_object}
        return context


class D3View(generic.ListView):
    template_name = 'dashboard/d3.html'

    def get_queryset(self):
        """
        Return an empty context object for index view.
        """
        index_context_object = []
        context = {'index_context_object': index_context_object}
        return context


class D4View(generic.ListView):
    template_name = 'dashboard/d4.html'

    def get_queryset(self):
        """
        Return an empty context object for index view.
        """
        index_context_object = []
        context = {'index_context_object': index_context_object}
        return context
