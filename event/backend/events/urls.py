from django.urls import path
from events.views import EventListApiView, CreateEventApiView, UpdateEventApiView, EventDetailApiView, DeleteEventApiView
urlpatterns = [
    path('all/', EventListApiView.as_view()),
    path('create/', CreateEventApiView.as_view()),
    path('update/<int:pk>', UpdateEventApiView.as_view()),
    path('delete/<int:pk>', DeleteEventApiView.as_view()),
    path('<int:pk>/', EventDetailApiView.as_view())
]