from django.db import models

from billing.models import BillingProfile

ADDRESS_TYPES = (
	('billing', 'Billing'),
	('shipping', 'Shipping')
)

class Address(models.Model):
	billing_profile = models.ForeignKey(BillingProfile)
	address_type 	= models.CharField(max_length=120, choices=ADDRESS_TYPES)
	address_line_1  = models.CharField(max_length=120)
	address_line_2  = models.CharField(max_length=120, null=True, blank=True)
	İlçe 			= models.CharField(max_length=120)
	şehir 		 	= models.CharField(max_length=120)
	ülke		 	= models.CharField(max_length=120, default='Türkiye')
	postal_code		= models.CharField(max_length=120)

	def __str__(self):
		return str(self.billing_profile)

	def get_address(self):
		return "{line1}\n{line2},\n{İlçe},\n{Şehir},\n{postal_code},\n{Ülke}".format(
				line1 = self.address_line_1,
				line2 = self.address_line_2 or "",
				İlçe = self.İlçe,
				Şehir = self.şehir,
				postal_code = self.postal_code,
				Ülke = self.ülke,

			)