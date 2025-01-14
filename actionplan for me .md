# Action Plan for Creating an Inventory Management System

## Phase 1: Project Setup

### Step 1: Set Up the Development Environment
1. Install Python (3.9 or later).
2. Install MongoDB and ensure it is running.
3. Install necessary tools like Git and a text editor/IDE (e.g., VS Code).

### Step 2: Create a Django Project
1. Create a new directory for your project.
   ```bash
   mkdir Inventory-Management-System
   cd Inventory-Management-System
   ```
2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```
3. Install Django and MongoDB dependencies:
   ```bash
   pip install django djongo
   ```
4. Start a new Django project:
   ```bash
   django-admin startproject inventory_system .
   ```
5. Create a new app for managing inventory:
   ```bash
   python manage.py startapp inventory
   ```
6. Add `inventory` to the `INSTALLED_APPS` list in `settings.py`.

## Phase 2: Database and Models

### Step 1: Configure MongoDB
1. Update `DATABASES` in `settings.py` to use MongoDB:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'djongo',
           'NAME': 'inventory_db',
       }
   }
   ```

### Step 2: Define Models
1. In `inventory/models.py`, define the models for Product, Supplier, and Sale Order.
   ```python
   from django.db import models

   class Supplier(models.Model):
       name = models.CharField(max_length=255)
       email = models.EmailField()
       phone = models.CharField(max_length=10)
       address = models.TextField()

   class Product(models.Model):
       name = models.CharField(max_length=255)
       description = models.TextField()
       category = models.CharField(max_length=255)
       price = models.DecimalField(max_digits=10, decimal_places=2)
       stock_quantity = models.IntegerField()
       supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

   class SaleOrder(models.Model):
       product = models.ForeignKey(Product, on_delete=models.CASCADE)
       quantity = models.IntegerField()
       total_price = models.DecimalField(max_digits=10, decimal_places=2)
       sale_date = models.DateField()
       status = models.CharField(max_length=50, choices=[
           ('Pending', 'Pending'),
           ('Completed', 'Completed'),
           ('Cancelled', 'Cancelled')
       ])
   ```

### Step 3: Apply Migrations
1. Create and apply migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

## Phase 3: Views and Templates

### Step 1: Create Views
1. Define views in `inventory/views.py` to handle CRUD operations.
2. Example: List and create products:
   ```python
   from django.shortcuts import render, get_object_or_404, redirect
   from .models import Product
   from .forms import ProductForm

   def product_list(request):
       products = Product.objects.all()
       return render(request, 'product_list.html', {'products': products})

   def product_create(request):
       if request.method == 'POST':
           form = ProductForm(request.POST)
           if form.is_valid():
               form.save()
               return redirect('product_list')
       else:
           form = ProductForm()
       return render(request, 'product_form.html', {'form': form})
   ```

### Step 2: Create Templates
1. Add a `templates` folder in the `inventory` app.
2. Create `product_list.html` and `product_form.html` for listing and adding products.
   Example: `product_list.html`
   ```html
   <h1>Product List</h1>
   <a href="/products/new/">Add Product</a>
   <ul>
       {% for product in products %}
       <li>{{ product.name }} - {{ product.stock_quantity }}</li>
       {% endfor %}
   </ul>
   ```

### Step 3: Add URLs
1. Create `urls.py` in the `inventory` app and define routes:
   ```python
   from django.urls import path
   from . import views

   urlpatterns = [
       path('', views.product_list, name='product_list'),
       path('products/new/', views.product_create, name='product_create'),
   ]
   ```
2. Include the app’s URLs in the project’s `urls.py`:
   ```python
   from django.urls import path, include

   urlpatterns = [
       path('', include('inventory.urls')),
   ]
   ```

## Phase 4: Styling and Final Touches

### Step 1: Add Bootstrap
1. Include Bootstrap in your templates for styling:
   ```html
   <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
   ```

### Step 2: Add Navigation
1. Create a base template for consistent navigation across pages.

### Step 3: Test the Application
1. Run the server and test all features:
   ```bash
   python manage.py runserver
   ```

## Phase 5: Deployment

### Step 1: Set Up GitHub Repository
1. Push your project to GitHub:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/yourusername/Inventory-Management-System.git
   git push -u origin main
   ```

### Step 2: Add GitHub Actions
1. Use the provided `.github/workflows/django-ci.yml` file for CI/CD.

### Step 3: Deploy to a Hosting Platform
1. Deploy the application to platforms like Heroku, AWS, or PythonAnywhere.

## Conclusion

Follow this action plan to build your Inventory Management System step-by-step. If you have any questions or run into issues, feel free to ask!
