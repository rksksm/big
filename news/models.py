from __future__ import unicode_literals
from django.utils import timezone
from tinymce.models import HTMLField
from django.db import models

# Create your models here.
class Section(models.Model):
	title = models.CharField(max_length=200)
	def __unicode__(self):
		return self.title
class Slide(models.Model):
	text = HTMLField()
	image = models.ImageField(upload_to = "slide/")

class Card(models.Model):
	Section = models.ForeignKey(Section)
	title = models.CharField(max_length=200)
	text = HTMLField()
	intro_text = models.CharField(max_length=200)
	image = models.ImageField(upload_to = "card/")


class Breaking(models.Model):
	text = models.CharField(max_length=100)
