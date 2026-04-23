# 🛒 E-Commerce Web Application (Django)

A full-featured E-Commerce web application built using **Django**, supporting product browsing, cart management, wishlist, orders, and user authentication.
📌 Features

* 🔍 Product search and filtering
* 🛍 Add to cart functionality
* ❤️ Wishlist system (AJAX-based toggle)
* 📦 Order management
* 👤 User authentication (Login/Register/Logout)
* ⭐ Product reviews and ratings
* 📂 Category-based product filtering
* 📄 Pagination for product listing
* 📊 Admin panel for product management

---

## 🛠 Tech Stack

* **Backend:** Django (Python)
* **Frontend:** HTML, CSS, JavaScript
* **Database:** SQLite (can be upgraded to PostgreSQL)
* **Deployment:** Render
* **Server:** Gunicorn
* **Static Files:** WhiteNoise

---

## 📁 Project Structure

```
ecommerce_project/
│
├── ecommerce_project/   # Main project settings
├── products/            # Product & wishlist app
├── cart/                # Cart functionality
├── orders/              # Order management
├── accounts/            # Authentication system
├── templates/           # HTML templates
├── static/              # CSS, JS, images
├── media/               # Uploaded images
├── manage.py
└── requirements.txt
```

---

## ⚙️ Installation (Local Setup)

### 1️⃣ Clone repository

```
git clone https://github.com/yourusername/ecommerce_project.git
cd ecommerce_project
```

---

### 2️⃣ Create virtual environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Run migrations

```
python manage.py migrate
```

---

### 5️⃣ Create superuser

```
python manage.py createsuperuser
```

---

### 6️⃣ Run server

```
python manage.py runserver
```

👉 Open: http://127.0.0.1:8000/

---

## 🌐 Deployment (Render)

* Connect GitHub repository
* Set Build Command:

  ```
  pip install -r requirements.txt
  ```
* Set Start Command:

  ```
  gunicorn ecommerce_project.wsgi
  ```
* Add Environment Variables:

  ```
  SECRET_KEY=your_secret_key
  DEBUG=False
  ```

---

## ⚠️ Important Notes

* Static files handled using **WhiteNoise**
* Media files may not persist on free hosting
* Use **Cloudinary / AWS S3** for production image storage

---

## 🧪 Future Improvements

* 💳 Payment integration (Razorpay/Stripe)
* 📱 Mobile responsive UI improvements
* 🔔 Notifications system
* 📊 Advanced analytics dashboard
* 🌍 Multi-language support

---

## 👨‍💻 Author

**Laxmi Dornal**
GitHub: https://github.com/laxmidornal123

---

## 📄 License

This project is for educational purposes.
