from django.core.management.base import BaseCommand
from Myshop.models import Category, Product

class Command(BaseCommand):
    help = 'Populates the database with initial categories and products'

    def handle(self, *args, **kwargs):
    
        Product.objects.all().delete()
        Category.objects.all().delete()

        electronics = Category.objects.create(name="Electronics", slug="electronics")
        clothing = Category.objects.create(name="Clothing", slug="clothing")

        Product.objects.create(
            name="Laptop",
            slug="laptop",
            category=electronics,
            price=999.99,
            description="High-performance laptop",
            available=True
        )
        Product.objects.create(
            name="Smartphone",
            slug="smartphone",
            category=electronics,
            price=699.99,
            description="Latest smartphone",
            available=True
        )
        Product.objects.create(
            name="Headphones",
            slug="headphones",
            category=electronics,
            price=99.99,
            description="Wireless headphones",
            available=True
        )
        Product.objects.create(
            name="T-Shirt",
            slug="t-shirt",
            category=clothing,
            price=19.99,
            description="Cotton t-shirt",
            available=True
        )
        Product.objects.create(
            name="Jeans",
            slug="jeans",
            category=clothing,
            price=49.99,
            description="Blue denim jeans",
            available=True
        )
        Product.objects.create(
            name="Jacket",
            slug="jacket",
            category=clothing,
            price=89.99,
            description="Winter jacket",
            available=True
        )

        Product.objects.create(
            name="GTX 1080",
            slug="gtx-1080",
            category=electronics,
            price=549.00,
            description="High-end graphics card",
            available=True
        )
        Product.objects.create(
            name="AMD Ryzen 5 5600X",
            slug="amd-ryzen-5-5600x",
            category=electronics,
            price=329.00,
            description="Powerful CPU for gaming and productivity",
            available=True
        )
        Product.objects.create(
            name="27-inch Monitor",
            slug="27-inch-monitor",
            category=electronics,
            price=299.00,
            description="27-inch IPS display with 144Hz refresh rate",
            available=True
        )

        Product.objects.create(
            name="Summer Dress",
            slug="summer-dress",
            category=clothing,
            price=39.99,
            description="Light and airy summer dress",
            available=True
        )
        Product.objects.create(
            name="Formal Suit",
            slug="formal-suit",
            category=clothing,
            price=199.99,
            description="Classic formal suit for men",
            available=True
        )
        Product.objects.create(
            name="Yoga Pants",
            slug="yoga-pants",
            category=clothing,
            price=29.99,
            description="Comfortable yoga pants for workouts",
            available=True
        )

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with categories and products.'))
