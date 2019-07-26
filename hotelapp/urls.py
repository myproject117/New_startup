from django.contrib import admin
from django.urls import path,re_path
from django.conf.urls import url
from hotelapp import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'hotelapp'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Hotel.as_view(),name='hotel'),
    path('home/',views.Home.as_view(),name='home'),
    path('customer/',views.Table.as_view(),name='customer'),
    path('create/',views.Create,name='create'),
    path('Receipt/',views.Bill.as_view(),name='receipt'),
    re_path(r'^customer/(?P<pk>\d+)/$',views.Detail.as_view(),name='detail'),
    re_path(r'^Receipt/(?P<pk>\d+)/$',views.Receipt.as_view()),
    re_path(r'^update/(?P<pk>\d+)/$',views.Update.as_view(),name='update'),
    re_path(r'^delete/(?P<pk>\d+)/$',views.Delete.as_view(),name='delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
