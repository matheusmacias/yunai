# transcription/views.py
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .models import Transcription
from .forms import TranscriptionForm

class TranscriptionListView(LoginRequiredMixin, ListView):
    model = Transcription
    template_name = "transcription/transcription_list.html"
    context_object_name = "transcriptions"
    paginate_by = 10

    def get_queryset(self):
        return Transcription.objects.filter(user=self.request.user)


class TranscriptionCreateView(LoginRequiredMixin, CreateView):
    model = Transcription
    form_class = TranscriptionForm
    template_name = "transcription/transcription_form.html"
    success_url = reverse_lazy("transcription:list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Transcrição criada com sucesso!")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Nova Transcrição"
        context["button_text"] = "Criar Transcrição"
        return context


class TranscriptionUpdateView(LoginRequiredMixin, UpdateView):
    model = Transcription
    form_class = TranscriptionForm
    template_name = "transcription/transcription_form.html"
    success_url = reverse_lazy("transcription:list")

    def get_queryset(self):
        return Transcription.objects.filter(user=self.request.user)

    def form_valid(self, form):
        messages.success(self.request, "Transcrição atualizada com sucesso!")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Editar Transcrição"
        context["button_text"] = "Atualizar Transcrição"
        return context


class TranscriptionDeleteView(LoginRequiredMixin, DeleteView):
    model = Transcription
    template_name = "transcription/transcription_confirm_delete.html"
    success_url = reverse_lazy("transcription:list")

    def get_queryset(self):
        return Transcription.objects.filter(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Transcrição excluída com sucesso!")
        return super().delete(request, *args, **kwargs)
