from django.urls import path
from . import views

urlpatterns = [
    path('', views.events , name="events"),
    path('login/',views.loginP ,name="login"),
    path('logout/',views.logoutuser ,name="logout"),
    path('register/',views.register ,name="register"),
    path('schedule/',views.schedule ,name='schedule'),
    path('<slug:event_slug>/deregister_event',views.deregister_event,name='deregister_event'),
    path('<slug:event_slug>/register_event',views.register_event,name='register_event'),
    path('<slug:event_slug>/success', views.confirm_registration , name='confirm_registration'),
    path('<slug:event_slug>/',views.event_details,name='event-details'),
]