from products.models import Product

products = [

# 📱 ELECTRONICS (5)
("Samsung Galaxy S21", 49999, "samsung-s21", "Smartphone with powerful performance", "https://images.unsplash.com/photo-1610945265064-0e34e5519bbf"),
("iPhone 14", 79999, "iphone-14", "Apple smartphone with A15 chip", "https://images.unsplash.com/photo-1663499482523-1d65e1b6b0d6"),
("OnePlus Nord CE3", 26999, "oneplus-nord-ce3", "Smooth performance smartphone", "https://images.unsplash.com/photo-1598327105666-5b89351aff97"),
("Realme Narzo 60", 17999, "realme-narzo-60-2", "Budget gaming phone", "https://images.unsplash.com/photo-1580910051074-3eb694886505"),
("Vivo Y100", 24999, "vivo-y100-2", "Stylish design smartphone", "https://images.unsplash.com/photo-1616348436168-de43ad0db179"),


# 👕 MEN SHIRTS (5)
("Levis Casual Shirt", 1499, "levis-shirt-3", "Comfortable cotton shirt", "https://images.unsplash.com/photo-1603252109303-2751441dd157"),
("Peter England Formal Shirt", 1299, "peter-shirt-3", "Perfect office wear", "https://images.unsplash.com/photo-1593032465171-8b4c2b0c9d9f"),
("Van Heusen Slim Shirt", 1799, "vanheusen-shirt-3", "Premium slim fit shirt", "https://images.unsplash.com/photo-1586790170083-2f9ceadc732d"),
("Wrangler Denim Shirt", 1599, "wrangler-shirt-3", "Stylish denim wear", "https://images.unsplash.com/photo-1556906781-9a412961c28c"),
("Spykar Printed Shirt", 1399, "spykar-shirt-3", "Trendy casual wear", "https://images.unsplash.com/photo-1523381210434-271e8be1f52b"),


# 👗 WOMEN CLOTHING (5)
("Zara Women Top", 1999, "zara-top-4", "Stylish casual top", "https://images.unsplash.com/photo-1520975916090-3105956dac38"),
("HM Women Shirt", 1499, "hm-shirt-4", "Comfortable everyday wear", "https://images.unsplash.com/photo-1524503033411-c9566986fc8f"),
("Forever21 Dress", 2299, "forever-dress-1", "Trendy party dress", "https://images.unsplash.com/photo-1509631179647-0177331693ae"),
("Biba Kurti", 1799, "biba-kurti-1", "Traditional ethnic wear", "https://images.unsplash.com/photo-1524504388940-b1c1722653e1"),
("Vero Moda Top", 1699, "vero-top-4", "Elegant western wear", "https://images.unsplash.com/photo-1517841905240-472988babdf9"),


# 👜 BAGS (5)
("Wildcraft Backpack", 1999, "wildcraft-bag-1", "Durable travel backpack", "https://images.unsplash.com/photo-1509762774605-f07235a08f1f"),
("Skybags Laptop Bag", 2499, "skybags-bag-1", "Stylish laptop bag", "https://images.unsplash.com/photo-1514474959185-1472d4c4e0b2"),
("American Tourister Bag", 2999, "tourister-bag-1", "Travel friendly bag", "https://images.unsplash.com/photo-1526178613658-3f1622045557"),
("Lavie Handbag", 1599, "lavie-bag-1", "Elegant women handbag", "https://images.unsplash.com/photo-1528701800489-20be3c7c69b2"),
("Caprese Handbag", 1799, "caprese-bag-1", "Premium stylish bag", "https://images.unsplash.com/photo-1584917865442-de89df76afd3"),


# 📚 BOOKS (5)
("Python Programming Book", 499, "python-book-1", "Learn Python easily", "https://images.unsplash.com/photo-1512820790803-83ca734da794"),
("Data Science Guide", 599, "datascience-book-1", "Complete data science book", "https://images.unsplash.com/photo-1524995997946-a1c2e315a42f"),
("Machine Learning Basics", 699, "ml-book-1", "Intro to ML concepts", "https://images.unsplash.com/photo-1532012197267-da84d127e765"),
("Django Web Development", 549, "django-book-1", "Build web apps using Django", "https://images.unsplash.com/photo-1519681393784-d120267933ba"),
("AI Handbook", 799, "ai-book-1", "Artificial Intelligence guide", "https://images.unsplash.com/photo-1522202176988-66273c2fd55f"),


# 💍 JEWELLERY (5)
("Gold Necklace Set", 9999, "necklace-1", "Elegant gold finish necklace", "https://images.unsplash.com/photo-1515562141207-7a88fb7ce338"),
("Silver Earrings", 999, "earrings-1", "Stylish silver earrings", "https://images.unsplash.com/photo-1522335789203-aabd1fc54bc9"),
("Diamond Ring", 14999, "ring-1", "Premium diamond ring", "https://images.unsplash.com/photo-1603561596112-0a132b757442"),
("Pearl Necklace", 2999, "pearl-necklace-1", "Classic pearl jewelry", "https://images.unsplash.com/photo-1617038220319-276d3cfab638"),
("Bracelet Set", 1999, "bracelet-1", "Trendy bracelet collection", "https://images.unsplash.com/photo-1519741497674-611481863552"),


# ⌚ WATCHES (5)
("Fossil Watch", 8999, "fossil-watch-2", "Premium leather watch", "https://images.unsplash.com/photo-1518546305927-5a555bb7020d"),
("Casio Digital Watch", 2499, "casio-watch-2", "Sporty digital watch", "https://images.unsplash.com/photo-1511381939415-e44015466834"),
("Titan Analog Watch", 3499, "titan-watch-2", "Classic analog watch", "https://images.unsplash.com/photo-1522312346375-d1a52e2b99b3"),
("Apple Watch Series 8", 45999, "apple-watch-9", "Smartwatch with health tracking", "https://images.unsplash.com/photo-1516574187841-cb9cc2ca948b"),
("Noise Smartwatch", 3999, "noise-watch-2", "Affordable smart watch", "https://images.unsplash.com/photo-1523275335684-37898b6baf30"),
]

for name, price, slug, desc, image in products:
    Product.objects.create(
        name=name,
        price=price,
        description=desc,
        slug=slug,
        image=image
    )

print("All category products added successfully")