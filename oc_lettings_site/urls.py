from django.contrib import admin
from django.urls import include, path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("lettings/", include("lettings.urls", namespace="lettings")),
    path("profiles/", include("profiles.urls", namespace="profiles")),
    path("admin/", admin.site.urls),
]


def trigger_error(request) -> None:
    """For sentry test"""
    division_by_zero = 1 / 0


urlpatterns += [
    path("sentry-debug/", trigger_error),
    # ...
]
