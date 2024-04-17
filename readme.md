# Food Delivery App Backend

This repository is for The server side of a food delivery app
It has Endpoints to
# Login   login/
# Register signup/
# Password Reset password/reset/
# Password reset confirm password/reset/<uidb64>/<token>/
# Endpoint to view junks junks/
# Endpoint to view foods foods/
# Endpoint to get all orders order/
# Endpoint to add to cart addtocart/
# Endpoint to remove from cart removefromcart/


## Installation andn running

Clone the Repository:
```
git clone [repository URL]
```
Install Dependencies:
Navigate to the project directory and run:
```
pip install -r requirements.txt
```
This will install all necessary Python libraries as listed in requirements.txt.


## Migrations
```
python manage.py makemigrations
python manage.py migrate

The above two lines of codes should run for any  change made in the models.py
```


## Running
```
python manage.py runserver
```