from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model): #models.Model gibt an, dass das Post Model ein Django Model ist, deshalb wird es in Datenbank gespeichert
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #foreignKey stellt verknüpfung zu anderem Model her
    title = models.CharField(max_length=200) #Feld mit limitierter Anzahl an Zeichen (200)
    text = models.TextField() #Feld mit unbegrenzt vielen Zeichen
    created_date = models.DateTimeField(default=timezone.now) #Feld für Datum und Uhrzeit
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title