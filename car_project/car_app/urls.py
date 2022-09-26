from django.urls import path


from car_app import views
app_name='car_app'
urlpatterns=[
    path('',views.home,name='home'),
    path('<slug:c_slug>/<slug:o_slug>/',views.car_detail,name='car_detail'),
    path('<slug:c_slug>/',views.home,name='car_by_category'),
    path('update/<slug:c_slug>/<slug:o_slug>/',views.update,name='update'),
    path('delete/<slug:c_slug>/<slug:o_slug>/',views.delete,name='delete'),

]