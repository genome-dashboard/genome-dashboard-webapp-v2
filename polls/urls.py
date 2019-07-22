from django.urls import path

from . import views


# Define namespace for app routes.
app_name = 'polls'

# version 1.
# urlpatterns = [
#     ### ex: /polls/
#     path('', views.index, name='index'),
#
#     ### ex: /polls/5/
#     path('<int:question_id>/', views.detail, name='detail'),
#     ### Example were we added the word 'specifics'
#     ### path('specifics/<int:question_id>/', views.detail, name='detail'),
#
#     ### ex: /polls/5/results/
#     path('<int:question_id>/results/', views.results, name='results'),
#
#     ### ex: /polls/5/vote/
#     path('<int:question_id>/vote/', views.vote, name='vote'),
# ]

# version 2.
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
