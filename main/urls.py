from django.urls import path
from main import views

urlpatterns = []
for url, view in views.url_and_view_list.items():
    pattern = path(url, getattr(views, view), name=view)
    urlpatterns.append(pattern)