# BankSearch
Bank Searching Api (postegress sql)

<!-- postgress sql import data from indian_bank.sql -->

In Setting Change password to corresponding user password

create user with "createsuperuser" command

import db using inspectdb command(db first approch)

corrently db only we can read that(if you want to update just change managed=True in model.py)

----How to Run------

first use migrate command to apply db changeds

python manage.py migrate

python manage.py runserver (defautly running on 8000 port)

----api calls------

1)getting access token
POST : http://127.0.0.1:8000/api/token/ username=xyz password=xxxxx

2)getting bank details with ifsc 
GET : http://127.0.0.1:8000/api/v1/banks/findbank?ifsc=BCBM0000077
header = { Authorization : Bearer xxxxxxxxxxxxxxxxxxxxxxxx}

3)getting banks with city and bank
GET : http://127.0.0.1:8000/api/v1/banks/banklist/?city=BANGALORE&bank=STATE BANK OF INDIA
header = { Authorization : Bearer xxxxxxxxxxxxxxxxxxxxxxxx}

---Pagination and token Validation settings----
defautly we give 
page_size = 5 (you can change in settings.py)
jwt expiry date = 5 days(we can change in settings.py)

-----installation-----

install using requirement file 

pip install -r requirements.txt 
