from django.urls import path
from .views import (IndexView, TopicView, TopicDetailView,
                    TopicCreateView, EntryCreateView)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('topics/', TopicView.as_view(), name='topics'),
    path('topics/<int:pk>', TopicDetailView.as_view(),
        name='topic_detail'),
    path('topics/new/', TopicCreateView.as_view(), name='new_tospic'),
    path('topics/<int:topic_pk>/entry/', EntryCreateView.as_view(), name='new_entry'),
]
