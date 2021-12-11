from django.urls import path, include
from django.urls.resolvers import URLPattern

from products import views

urlpatterns = [
    path('products/', views.Categories.as_view()),
    path('products/<slug:category_slug>/', views.CategoryDetail.as_view()),
    path('products/<slug:category_slug>/<slug:product_slug>/', views.ProductView.as_view())
]