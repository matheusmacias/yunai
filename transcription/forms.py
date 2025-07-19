from .models import Transcription
from django import forms


class TranscriptionForm(forms.ModelForm):
    class Meta:
        model = Transcription
        fields = ["original_filename", "language", "transcription_text"]
        help_texts = {
            "status": "Mantenha como 'Pendente' para que o arquivo seja enviado para processamento.",
            "transcription_text": "Se este arquivo estiver sendo processado, o conteúdo atual será sobrescrito."
        }
        widgets = {
            "original_filename": forms.TextInput(
                attrs={
                    "class": "w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500",
                    "placeholder": "Nome do arquivo",
                }
            ),
            "language": forms.Select(
                attrs={
                    "class": "w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                }
            ),
            "transcription_text": forms.Textarea(
                attrs={
                    "class": "w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500",
                    "placeholder": "Texto da transcrição",
                    "rows": 10,
                }
            ),
        }