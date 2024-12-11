from django.db import models


# Create your models here.


class Coffe(models.Model):
	tittle = models.CharField(max_length = 255)
	content = models.TextField(blank = True)
	cat = models.ForeignKey('Category', on_delete = models.PROTECT, null=True)

	def __str__(self):
		return self.tittle


class Category(models.Model):
	name = models.CharField(max_length = 100, db_index = True)

	def __str__(self):
		return self.name

class Taste(models.Model):
	name = models.CharField(max_length = 100, db_index = True)

	def __str__(self):
		return self.name

class FavCoffe(models.Model):
	tittle = models.CharField(max_length = 255)
	content = models.TextField(blank = True)
	cat = models.ForeignKey('Category', on_delete = models.PROTECT, null=True)

	def __str__(self):
		return self.tittle

class AlergensForCoffee(models.Model):
	content = models.TextField(blank = True)
	coffe_cat = models.ForeignKey('Coffe', on_delete = models.PROTECT, null=True)

	def __str__(self):
		return self.tittle

class Stores(models.Model):
	address = models.CharField(max_length=100)

	def __str__(self):
		return self.tittle

class OrdersHistory(models.Model):
	content = models.TextField(blank = True)
	date = models.DateField()

	def __str__(self):
		return self.tittle

class RewardsHistory(models.Model):
	content = models.TextField(blank = True)
	date = models.DateField()

	def __str__(self):
		return self.tittle

class Specials(models.Model):
	tittle = models.CharField(max_length = 255)
	content = models.TextField(blank = True)
	cat = models.ForeignKey('Category', on_delete = models.PROTECT, null=True)

	def __str__(self):
		return self.tittle
