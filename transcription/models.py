from django.db import models
from django.contrib.auth.models import User


class Transcription(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pendente'),
        ('processing', 'Processando'),
        ('completed', 'Concluída'),
        ('failed', 'Falhou'),
        ('cancelled', 'Cancelada'),
    ]
    
    LANGUAGE_CHOICES = [
        ('pt-BR', 'Português (Brasil)'),
        ('en-US', 'Inglês (EUA)'),
        ('es-ES', 'Espanhol'),
        ('fr-FR', 'Francês'),
        ('de-DE', 'Alemão'),
    ]
    
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='transcriptions',
        verbose_name='Usuário'
    )
    
    original_filename = models.CharField(max_length=255, verbose_name='Nome original do arquivo')
    file_size = models.BigIntegerField(null=True, blank=True, verbose_name='Tamanho do arquivo (bytes)')
    duration = models.DurationField(null=True, blank=True, verbose_name='Duração')
    
    language = models.CharField(
        max_length=10, 
        choices=LANGUAGE_CHOICES, 
        default='pt-BR',
        verbose_name='Idioma'
    )
    
    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES, 
        default='pending',
        verbose_name='Status'
    )
    progress = models.IntegerField(default=0, verbose_name='Progresso (%)')
    
    transcription_text = models.TextField(blank=True, verbose_name='Texto transcrito')
    confidence_score = models.FloatField(
        null=True, 
        blank=True, 
        verbose_name='Pontuação de confiança'
    )
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')
    started_at = models.DateTimeField(null=True, blank=True, verbose_name='Iniciado em')
    completed_at = models.DateTimeField(null=True, blank=True, verbose_name='Concluído em')
    
    class Meta:
        verbose_name = 'Transcrição'
        verbose_name_plural = 'Transcrições'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['user', 'status']),
            models.Index(fields=['created_at']),
            models.Index(fields=['status']),
        ]
    
    def __str__(self):
        return f'{self.original_filename} - {self.get_status_display()}'
    
    @property
    def is_completed(self):
        return self.status == 'completed'
    
    @property
    def is_processing(self):
        return self.status == 'processing'
    
    @property
    def has_failed(self):
        return self.status == 'failed'
    
    def get_file_size_display(self):
        """Retorna o tamanho do arquivo em formato legível"""
        if not self.file_size:
            return 'N/A'
        
        for unit in ['B', 'KB', 'MB', 'GB']:
            if self.file_size < 1024.0:
                return f"{self.file_size:.1f} {unit}"
            self.file_size /= 1024.0
        return f"{self.file_size:.1f} TB"
    
    def get_duration_display(self):
        """Retorna a duração em formato legível"""
        if not self.duration:
            return 'N/A'
        
        total_seconds = int(self.duration.total_seconds())
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        
        if hours > 0:
            return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        return f"{minutes:02d}:{seconds:02d}"