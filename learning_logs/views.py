from django.views.generic import (TemplateView, ListView,
                                  DetailView)
from django.views.generic.edit import CreateView
from django.shortcuts import get_object_or_404

from .models import Topic, Entry
from .form import EntryForm


class IndexView(TemplateView):
    template_name = 'index.html'


class TopicView(ListView):
    model = Topic
    template_name = 'topic.html'


class TopicDetailView(DetailView):
    model = Topic
    template_name = 'topic_detail.html'


class TopicCreateView(CreateView):
    model = Topic
    fields = ['text']
    template_name = 'topic_new.html'


class EntryCreateView(CreateView):
    form_class = EntryForm
    model = Entry
    template_name = 'entry_new.html'

    def dispatch(self, request, *args, **kwargs):
        self.topic = get_object_or_404(Topic,
                                       pk=kwargs['topic_pk'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.topic = self.topic
        return super().form_valid(form)
