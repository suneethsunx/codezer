from django.db import models
from django.contrib.auth.models import User


class CodeFile(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length=50)
    code = models.TextField()
    private = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True, null=True, blank=True)
    link_id = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.title