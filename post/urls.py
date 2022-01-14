from  django.urls import path
from . import views

urlpatterns = [
    path("post", views.post,name="post"),
    path("product", views.product,name="product"),
    path("entry/<int:pk>/", views.Entry,name="entry"),
]