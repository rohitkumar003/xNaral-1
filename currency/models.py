from django.db import models
from django.urls import reverse


class CurrencyPair(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    currency_code = models.CharField(max_length=3, help_text='currency code')
    language = models.CharField(max_length=20, help_text='language')
    target_currency_code = models.CharField(max_length=3, help_text='target currency code')

    # …

    #Metadata
    class Meta:
        db_table = 'currency_pair'

    # Methods
    # def get_absolute_url(self):
    #     """Returns the URL to access a particular instance of MyModelName."""
    #     return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.currency_code + ":" + self.language + ":" + self.target_currency_code
