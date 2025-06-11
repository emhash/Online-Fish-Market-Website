from django.db import models
import uuid

class BillingAddress(models.Model):
    uid=models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)

    owner = models.OneToOneField("users.Profile", on_delete=models.CASCADE, related_name="bill_owner")
    city = models.CharField( max_length=100,blank=True)
    country = models.CharField( max_length=50,blank=True)
    area = models.CharField( max_length=100,blank=True)
    house_or_road_no = models.CharField(max_length=150, blank=True)
    post_code = models.CharField( max_length=100,blank=True)
    phone_no = models.PositiveIntegerField(null=True,blank=True)

    def __str__(self) -> str:
        return f"{self.owner.name}'s Billing"
    
    def is_fully_filled(self):
        required_fields = [self.city, self.country, self.area, self.post_code, self.phone_no]
        return all(field not in (None, '', 0) for field in required_fields)