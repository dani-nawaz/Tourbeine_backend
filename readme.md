# Tourbeine backend


- to run the server run these command

```bash 
python -m venv venv
```

```bash 
pip install -r requirements.txt
```
```bash 
python manage.py makemigrations
```
```bash 
python manage.py migrate
```

```bash 
python manage.py runserver
```
   
## API'S
### User
 - http://localhost:8000/user/current = current logged in user info and can update it too
- http://localhost:8000/user/register = for registeration
- http://localhost:8000/user/login = for login
- http://localhost:8000/user/password = for changing password
### product
 - http://localhost:8000/product/category =get all category or create category
 - http://localhost:8000/product/category/<int:pk>/ = get update or delete single category
- http://localhost:8000/product/all = get all products or create produdcts
- http://localhost:8000/product/<int:pk>/ = get update or delete single prodcut
- http://localhost:8000/product/product-bookmarks/<int:pk>/ = to delete or add products to the list
- http://localhost:8000/product/user-saved-products = to get all the saved products
