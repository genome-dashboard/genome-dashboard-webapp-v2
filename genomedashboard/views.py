# from django.shortcuts import get_object_or_404, render
from django.views import generic


# def index(request):
#     template_name = 'genomedashboard/index.html'
#     index_context_object = []
#     context = {'index_context_object': index_context_object}
#     return render(request, template_name, context)


class IndexView(generic.ListView):
    template_name = 'genomedashboard/index.html'

    def get_queryset(self):
        """
        Return an empty context object for index view.
        """
        index_context_object = []
        context = {'index_context_object': index_context_object}
        return context


class AboutView(generic.ListView):
    template_name = 'genomedashboard/about.html'

    def get_queryset(self):
        """
        Return an empty context object for index view.
        """
        index_context_object = []
        context = {'index_context_object': index_context_object}
        return context
