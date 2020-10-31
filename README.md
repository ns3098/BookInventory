# ONLINE BOOK INVENTORY

[![N|Solid](https://media-exp1.licdn.com/dms/image/C560BAQH3K_P2R_8m3A/company-logo_200_200/0?e=2159024400&v=beta&t=ay-4drqvrQBWQvj_Uqc_eXhccMBnXvE-eltkvowyVRg)](https://nodesource.com/products/nsolid)

 ONLINE BOOK INVENTORY is a fully responsive Web App made using Python/Django. 
It contains the list of book and also have information about its copies and book info link provided by Google Book Api. It is publicly accessible, there is no need to login or signup.

 

# Features!
- User can add books, remove books.
- User can also get more information about the book by clicking on its Title.
- User can also search books and the results will be displayed using Google API.
- User can get the information about the number of copies and ID of that book.
- If Searched book already exist in inventory, then it'll show 'Available in Bookstore' below the title of the book.
- In inventory if any book goes out of stock, then it'll show 'Out of Stock' below the title of the book.
- To Add or Remove any book, user need to hover over the book and then choose the option.

# Installation
> Make sure python3 is installed before performing below steps.

- Clone the Repo and navigate to root directory.
```sh
git clone https://github.com/ns3098/BookInventory.git
```
- Create a Virtual Environment(env), make sure 'venv' package is installed.
```sh
py -m venv env
```
- Activate the Environment
```sh
.\env\Scripts\activate
```
- Install all required dependencies.
```sh
pip install -r requirements.txt
```
- Migrate the database.
```sh
python manage.py makemigrations
python manage.py migrate
```
- Finally, run the server.
```sh
python manage.py runserver
```
- In your browser go to [127.0.0.1:8000](127.0.0.1:8000) .

### Development

Want to contribute? Great!

- All the configurations of the project are in the file **settings.py** file.
- Make Sure to create your own SECRET_KEY for the project.
- For Database related information, checkout **models.py**.
- For frontend part of the application, checkout **templates** folder.
