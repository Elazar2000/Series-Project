
from django.urls import path
from . import views
app_name = 'seriesapp'
urlpatterns = [

    path('',views.home,name='home'),
    path('series/<int:series_id>/',views.detail,name='detail'),
    path('add/',views.add_series,name='add_series'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')
]
