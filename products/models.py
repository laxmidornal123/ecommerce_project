from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


# ✅ CATEGORY OPTIONS
CATEGORY_CHOICES = [
    ('mobile', 'Mobiles'),
    ('laptop', 'Laptops'),
    ('clothing', 'Clothing'),
    ('watch', 'Watches'),
    ('shoes', 'Footwear'),
    ('jewellery', 'Jewellery'),
    ('books', 'Books'),
]


# ✅ PRODUCT MODEL
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='mobile'
    )

    def save(self, *args, **kwargs):
        # 🔥 AUTO GENERATE SLUG
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1

            # prevent duplicate slug
            while Product.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


# ✅ REVIEW MODEL
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} - {self.rating}"


# ✅ WISHLIST MODEL
class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"