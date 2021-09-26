from django.db import models


#models
class Website(models.Model):
    pk_website = models.AutoField(primary_key=True)
    site_name = models.CharField(max_length=264, unique=True)
    site_url = models.URLField(unique=True)
    site_last_http_response = models.IntegerField(default=404)
    site_up_status = models.BooleanField(default=False)
    slack_token = models.CharField(max_length=264)
    slack_channel = models.CharField(max_length=264)

    def __str__(self):
        return f'{self.site_name}'