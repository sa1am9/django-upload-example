from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from mysite.core import views
from django.views.generic.base import TemplateView


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    # path('reports/<int:pk>/', views.delete_report, name='delete_report')

    path('reports/', views.ReportListView.as_view(), name='reports_list'),
    path('reports/upload/', views.UploadDataView.as_view(), name='upload_data'),
    path('download/<int:pk>/', views.download_file, name="download"),

    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
