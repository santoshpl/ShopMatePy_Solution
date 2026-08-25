from django.core.management.base import BaseCommand
from products.models import Product


PRODUCTS = [
    {
        "name": "Wireless Noise Cancelling Headphones",
        "description": "Premium over-ear headphones with active noise cancellation, high-fidelity sound, Bluetooth connectivity, a built-in microphone, and up to 30 hours of battery life.",
        "price": 299.99,
        "category": "Electronics",
        "stock": 50,
        "image": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=800&q=80",
    },
    {
        "name": "Ergonomic Office Chair",
        "description": "A comfortable office chair with adjustable lumbar support, breathable mesh, adjustable armrests and seat height, and a durable foam cushion.",
        "price": 199.99,
        "category": "Furniture",
        "stock": 20,
        "image": "https://images.unsplash.com/photo-1592078615290-033ee584e267?w=800&q=80",
    },
    {
        "name": "Smart Fitness Watch",
        "description": "A smart wearable that tracks heart rate, steps, calories, sleep, and workouts with a bright AMOLED display and smartphone notifications.",
        "price": 149.50,
        "category": "Electronics",
        "stock": 100,
        "image": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=800&q=80",
    },
    {
        "name": "Minimalist Backpack",
        "description": "A water-resistant everyday backpack with a padded laptop sleeve, organized pockets, padded shoulder straps, and a breathable back panel.",
        "price": 79.00,
        "category": "Accessories",
        "stock": 45,
        "image": "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=800&q=80",
    },
    {
        "name": "Mechanical Keyboard",
        "description": "A compact mechanical keyboard with tactile switches, customizable RGB lighting, anti-ghosting, durable construction, and USB-C connectivity.",
        "price": 120.00,
        "category": "Electronics",
        "stock": 30,
        "image": "https://images.unsplash.com/photo-1558050032-160f36233a07?w=800&q=80",
    },
    {
        "name": "Ceramic Coffee Mug Set",
        "description": "A handcrafted modern mug set with a matte finish that is lead-free, microwave-safe, dishwasher-safe, and designed for comfortable everyday use.",
        "price": 35.00,
        "category": "Home",
        "stock": 60,
        "image": "https://images.unsplash.com/photo-1514228742587-6b1558fcca3d?w=800&q=80",
    },
    {
        "name": "Running Shoes",
        "description": "Lightweight running shoes with a breathable mesh upper, responsive cushioning, durable rubber outsole, and supportive fit for everyday training.",
        "price": 89.99,
        "category": "Clothing",
        "stock": 25,
        "image": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=800&q=80",
    },
    {
        "name": "Bamboo Cutting Board",
        "description": "An eco-friendly bamboo cutting board with a juice groove and non-slip feet, designed for durable and hygienic kitchen preparation.",
        "price": 24.99,
        "category": "Home",
        "stock": 75,
        "image": "https://images.unsplash.com/photo-1660002561318-6ef0a0ae1f04?w=800&q=80",
    },
    {
        "name": "Polarized Sunglasses",
        "description": "Classic polarized sunglasses with UV400 protection, glare reduction, a lightweight metal frame, and adjustable nose pads.",
        "price": 55.00,
        "category": "Accessories",
        "stock": 40,
        "image": "https://images.unsplash.com/photo-1572635196237-14b3f281503f?w=800&q=80",
    },
    {
        "name": "Bluetooth Speaker",
        "description": "A portable waterproof Bluetooth speaker with 360-degree sound, up to 12 hours of battery life, and stereo pairing support.",
        "price": 65.00,
        "category": "Electronics",
        "stock": 55,
        "image": "https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?w=800&q=80",
    },
]


class Command(BaseCommand):
    help = "Seed the database with ShopMate products"

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Product.objects.bulk_create([Product(**product) for product in PRODUCTS])
        self.stdout.write(self.style.SUCCESS(f"Seeded {len(PRODUCTS)} products."))
