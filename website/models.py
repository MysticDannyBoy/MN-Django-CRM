from django.db import models


class Record(models.Model):
	packaging_choices = (
		('4g', '4g-os'),
		('15g', '15g-os'),
		('30g', '30g-os'),
		('50g', '50g-os'),
	)
	name = models.CharField(max_length=50)
	price = models.IntegerField()
	kiszereles = models.CharField(max_length=3, choices=packaging_choices)
	bevezetes_datuma = models.DateTimeField()

	def __str__(self):
		return f"{self.name}"
