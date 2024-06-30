from django.db import models
import uuid

class Account(models.Model):
    email = models.EmailField(unique=True)
    account_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255)
    app_secret_token = models.CharField(max_length=255, editable=False)
    website = models.URLField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.app_secret_token:
            self.app_secret_token = uuid.uuid4().hex
            print("secret ",self.app_secret_token)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

