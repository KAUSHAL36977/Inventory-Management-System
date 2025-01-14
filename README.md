# Inventory Management System

A Django-based Inventory Management System designed to efficiently manage products, stock levels, suppliers, and sales.

## Features

- **Product Management**: Add, edit, delete, and view products.
- **Supplier Management**: Manage supplier details such as name, email, phone, and address.
- **Sales Tracking**: Track sales orders with product, quantity, total price, sale date, and status.
- **Responsive Design**: Built with HTML, CSS, JavaScript, and Bootstrap.
- **Database Integration**: Uses MongoDB for data storage.

## Tech Stack

- **Backend**: Django
- **Frontend**: HTML, CSS, JavaScript (Bootstrap)
- **Database**: MongoDB

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/inventory-management-system.git
   cd inventory-management-system
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure the database:
   - Update `DATABASES` in `settings.py` for MongoDB.

4. Apply migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Run the server:
   ```bash
   python manage.py runserver
   ```

6. Access the app at: `http://127.0.0.1:8000`

## Project Structure

- **`models.py`**: Database models for Product, Supplier, and Sales Order.
- **`views.py`**: Logic for CRUD operations.
- **`forms.py`**: Django forms for data handling.
- **`templates/`**: HTML templates for the UI.
- **`urls.py`**: URL routing for the application.

## Screenshots

### Product List
![Product List](path/to/screenshot1.png)

### Add Product
![Add Product](path/to/screenshot2.png)

## Contributions

Contributions are welcome! Fork the repo, create a new branch, and submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
