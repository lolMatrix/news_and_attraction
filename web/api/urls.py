from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('news/', views.get_all_news),
    path('news/page/<int:page>/', views.get_news_page),
    path('news/count/', views.get_count_pages),
    path('news/save/', views.save_news),
    path('news/update/', views.update_news),
    path('view/', views.get_news_html),
]

urlpatterns = format_suffix_patterns(urlpatterns)
