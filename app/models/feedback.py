from django.db import models


class Feedback(models.Model):
    full_name = models.TextField()
    email = models.EmailField()
    phone = models.TextField()
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'feedback'

    def __str__(self):
        return self.full_name