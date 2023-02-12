import uuid
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class MainModel(models.Model):
    """ Here store user name, mobile_no and nitification time """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=128, blank=True, null=True)
    last_name = models.CharField(max_length=128, blank=True, null=True)
    mobile = PhoneNumberField(blank=True, null=True)
    notification_time = models.DateTimeField(db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        db_table = 'MainModel'

    def get_full_name(self):
        fn = self.first_name
        ln = self.last_name
        name = fn + ' ' + ln
        return name