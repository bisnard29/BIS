from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class spesometro(models.Model):
    CodiceFiscale_T = models.CharField(max_length=30)
    Carica_T = models.CharField(max_length=30)
    IdPaese_T = models.CharField(max_length=30)
    IdCodice_T = models.CharField(max_length=30)
    Denominazione_T = models.CharField(max_length=30)
    Indirizzo_T = models.CharField(max_length=30)
    NumeroCivico_T = models.CharField(max_length=30)
    CAP_T = models.CharField(max_length=30)
    Comune_T = models.CharField(max_length=30)
    Provincia_T = models.CharField(max_length=30)
    Nazione_T = models.CharField(max_length=30)
    IdPaese2_T = models.CharField(max_length=30)
    IdCodice2_T = models.CharField(max_length=30)
    Denominazione2_T = models.CharField(max_length=30)
    Indirizzo2_T = models.CharField(max_length=30)
    NumeroCivico2_T = models.CharField(max_length=30)
    CAP2_T = models.CharField(max_length=30)
    Comune2_T = models.CharField(max_length=30)
    Provincia2_T = models.CharField(max_length=30)
    Nazione2_T = models.CharField(max_length=30)
    TipoDocumento_T = models.CharField(max_length=30)
    Data_T = models.CharField(max_length=30)
    Numero_T = models.CharField(max_length=30)
    DataRegistrazione_T = models.CharField(max_length=30)
    ImponibileImporto_T = models.CharField(max_length=30)
    Imposta_T = models.CharField(max_length=30)
    Aliquota_T = models.CharField(max_length=30)
    Natura_T = models.CharField(max_length=30)


