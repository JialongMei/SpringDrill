from django.dispatch import receiver
from django.urls import reverse
from django.db import models
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower
from django.db.models.signals import post_save
from PIL import Image


@receiver(post_save, sender=Image)
def crop_image(sender, instance, **kwargs):
    imgage = instance.image
    original = Image.open(imgage.src.path).convert("RGBA")
    new_image = Image.new("RGBA", original.size, "BLACK")
    new_image.paste(original, mask=original)
    instance.image = new_image


class Archetype(models.Model):
    name = models.CharField(max_length=40, unique=True,help_text="Name of this archetype(e.g. Martial Artist)")

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('archetype-detail', args=[str(self.id)])

    def __str__(self):
        return self.name


class ClassEngraving(models.Model):
    name = models.CharField(max_length=40, unique=True)
    description = models.TextField(max_length=1000)
    associated_class = models.ForeignKey('AllClass', on_delete=models.RESTRICT, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('class-engraving-detail', args=[str(self.id)])



class AllClass(models.Model):
    name = models.CharField(max_length=40, unique=True, help_text="Name of this class(e.g. Wardancer)")
    archetype = models.ForeignKey('Archetype', on_delete=models.RESTRICT, null=True)
    icon = models.ImageField(upload_to='icons',default='media/default/default_icon.jpg')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('class-detail', args=[str(self.id)])

    class Meta:
        ordering = ['name']
        constraints = [
            UniqueConstraint(
                Lower('name'),
                name='genre_name_case_insensitive_unique',
                violation_error_message="Class already exists (case insensitive match)"
            ),
        ]


class CombatEngraving(models.Model):
    name = models.CharField(max_length=40, unique=True)
    description = models.TextField(max_length=1000, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('combat-engraving-detail', args=[str(self.id)])



