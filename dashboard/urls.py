from django.urls import path

from . import views


# Define namespace for app routes.
app_name = 'dashboard'

# Define Routes.
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('d1', views.D1View.as_view(), name='d1'),
    path('d2', views.D2View.as_view(), name='d2'),
    path('d3', views.D3View.as_view(), name='d3'),
    path('d4', views.D4View.as_view(), name='d4'),
]
