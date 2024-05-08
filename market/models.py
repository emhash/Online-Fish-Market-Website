from django.db import models
from users.models import Profile
import uuid

class CommonBaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, default= uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Category(CommonBaseModel):
    name = models.CharField(max_length=100)
    up_to = models.PositiveIntegerField(null=True, blank=True)
    image = models.ImageField( upload_to="FishCategory", default="fishcat.jpg")

    def __str__(self):
        return self.name

class Offer(CommonBaseModel):
    name = models.CharField(max_length=100)
    up_to = models.PositiveIntegerField(null=True, blank=True)
    image = models.ImageField(upload_to="OffersPoster",default="fishoffer.jpg")
    
    def __str__(self):
        return self.name

class Fish(CommonBaseModel):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="Fishes")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    discount = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    # offers = models.ManyToManyField(Offer, blank=True)

    def discounted_price(self):
        if self.discount:
            return self.price - self.discount
        else:
            return self.price

    def __str__(self):
        return self.name

class CartItem(CommonBaseModel):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    fish = models.ForeignKey(Fish, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def subtotal(self):
        return self.fish.discounted_price() * self.quantity

class Review(CommonBaseModel):
    RATING_CHOICES = (
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    )
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    fish = models.ForeignKey(Fish, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField(blank=True)

class Favorite(CommonBaseModel):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    fish = models.ForeignKey(Fish, on_delete=models.CASCADE)

