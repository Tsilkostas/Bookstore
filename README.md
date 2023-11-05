# Bookstore
e-commerce Bookstore
USER REQUIREMENTS

The goal is the creation of an online bookshop.

Users should be able to create an account. Users that have an account should be able to login. When logged-in, they should be able to track their orders, edit their info, and view their wishlist.

The main page should show all the books (book cover and title).

Additionally a button should display the book categories (fantasy, horror etc.).

When clicking on the book title, the software should go to the book’s page. This page should show the book’s cover, title, and price. A user should be able to select how many books wants to buy. Additionally a user should be able to add the book to the basket or add it to his/her favourites.

The basket icon, when clicked, should display the added books and the total price. The user should be able to buy the books by clicking a ‘Checkout’ button or save the basket by clicking a ‘Save for later’ button.

HOW TO RUN THE SERVER

Instructions:

Download
Extract in a folder
Open with visual studio code
In views.py on the ‘payment’ folder, ‘import stripe’ should be changed to ‘# import stripe’.
Commands:

py -m venv venv

venv\Scripts\activate

pip uninstall rest_framework

pip install rest_framework

pip install djangorestframework-jsonapi

pip install django-isbn-field

pip install requests

pip install pillow

py manage.py runserver

Open an internet browser and go to: http://127.0.0.1:8000/

