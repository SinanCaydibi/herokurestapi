from .views import ExampleListAPIView , ExampleCreateAPIView ,ExampleUpdateAPIView
from django.urls import path

app_name = "api"
urlpatterns = [
   
    path('list', ExampleListAPIView.as_view(), name='list'),
   
    path('create',ExampleCreateAPIView.as_view(),name='create'),
    path('update/<slug>',ExampleUpdateAPIView.as_view(),name='update')
]