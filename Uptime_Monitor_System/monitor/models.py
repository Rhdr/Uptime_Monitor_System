from django.db import models


#models
class Website(models.Model):
    pk_website = models.AutoField(primary_key=True)
    site_name = models.CharField(max_length=264, unique=True)
    site_url = models.URLField(unique=True)
    site_last_http_response = models.IntegerField()
    site_status = models.BooleanField()
    slack_account_url = models.URLField()

    def __str__(self):
        return f'{self.site_name}'