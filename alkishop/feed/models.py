from django.db import models

class Item(models.Model):
	title = models.CharField(max_length=50, unique=True)
	slug = models.SlugField(max_length=50, unique=True)
	body = models.TextField(blank=True, db_index=True)
	categories = models.ManyToManyField('Category', blank=True, related_name='categories')

	def __str__(self):
		return self.title()


class Category(models.Model):
	title = models.CharField(max_length=50, unique=True)
	slug = models.SlugField(max_length=50, unique=True)

	def __str__(self):
		return self.title()
