#import codecademylib
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])
print(visits.head())
print(cart.head())
print(checkout.head())
print(purchase.head())

visits_cart = visits.merge(cart, how = 'left')
print(visits_cart)
l1 = len(visits_cart)

null_rows = visits_cart[visits_cart.cart_time.isnull()]
print(null_rows)

percent_nocart = float(len(null_rows))/(l1+len(null_rows))
print(percent_nocart)

cart_checkout = cart.merge(checkout, how = 'left')
print(cart_checkout)
l2 = len(cart_checkout)

null_cart = cart_checkout[cart_checkout.checkout_time.isnull()]
null_rows2 = len(null_cart) 

percent_nocheck = float(null_rows2)/(l2+null_rows2)
print (percent_nocheck)

all_data = visits.merge(cart,how='left').merge(checkout,how='left').merge(purchase, how='left')
print(all_data.head())

all_data['time_to_purchase'] = \
all_data.purchase_time - all_data.visit_time
print (all_data.time_to_purchase)
print (all_data.time_to_purchase.mean())