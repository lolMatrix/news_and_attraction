from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('news/', views.get_all_news),
    path('news/save/', views.save_news),
    path('news/update/', views.update_news),
]

urlpatterns = format_suffix_patterns(urlpatterns)
