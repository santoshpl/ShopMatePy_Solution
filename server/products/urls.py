from django.urls import path
from .views import ProductDetailView, ProductListCreateView

urlpatterns = [
    # Support both forms because the existing React client uses no trailing slash.
    path("", ProductListCreateView.as_view(), name="product-list-create"),
    path("<int:pk>", ProductDetailView.as_view(), name="product-detail"),
    path("<int:pk>/", ProductDetailView.as_view(), name="product-detail-slash"),
]
