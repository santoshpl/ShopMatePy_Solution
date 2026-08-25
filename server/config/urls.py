from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    # Support the existing React client's URLs with or without a trailing slash.
    path("api/products", include("products.urls")),
    path("api/products/", include("products.urls")),
    path("api/ai/", include("ai.urls")),
]
