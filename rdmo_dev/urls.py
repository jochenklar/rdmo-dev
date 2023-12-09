from django.urls import include, path

from config.urls import handler400, handler403, handler404, handler500, urlpatterns  # noqa: F401

urlpatterns += [
    path('__debug__/', include('debug_toolbar.urls'))
]
