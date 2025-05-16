# Myshop/management/commands/add_images.py
from django.core.management.base import BaseCommand
from django.core.files import File
from Myshop.models import Product
import os

class Command(BaseCommand):
    help = 'Adds images to existing products'

    def handle(self, *args, **kwargs):
        # Map product slugs to image filenames (updated to match actual files)
        product_images = {
            'laptop': 'Laptop.png',
            'smartphone': 'Smartphone.png',
            'headphones': 'Headphones.png',
            't-shirt': 'Tshirt.png',
            'jeans': 'Jeans.png',
            'jacket': 'Jacket.png',
        }

        # Path to the images directory
        images_dir = os.path.join('Myshop', 'media', 'images')

        for slug, image_name in product_images.items():
            try:
                product = Product.objects.get(slug=slug)
                image_path = os.path.join(images_dir, image_name)
                if os.path.exists(image_path):
                    with open(image_path, 'rb') as f:
                        product.image.save(image_name, File(f), save=True)
                    self.stdout.write(self.style.SUCCESS(f'Added image to {product.name}'))
                else:
                    self.stdout.write(self.style.WARNING(f'Image {image_name} not found for {product.name}'))
            except Product.DoesNotExist:
                self.stdout.write(self.style.ERROR(f'Product with slug {slug} not found'))

        self.stdout.write(self.style.SUCCESS('Finished adding images to products.'))