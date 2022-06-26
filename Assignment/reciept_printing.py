#
#
#
#
# print(f"""
#                                                         Available products:
#                                                 ************************************
#                                                 products            price
#                                                 ************************************
#                                                 rice:               300
#                                                 beans:              400
#                                                 spaghetti:          350
#                                                 egg:                2000
#                                                 salt:               50
#                                                 maggi:              700
# """)
rice_per_kilogram = 300
beans_per_kilogram = 400
spaghetti = 350
egg_per_crate = 2000
salt = 50
maggi = 700

rice_quantity = int(input("How many kilogram of rice will you like to buy: "))
rice_price = rice_per_kilogram * rice_quantity

beans_quantity = int(input("How many kilogram of bean will you like to buy: "))
beans_price = beans_quantity * beans_per_kilogram

spaghetti_quantity = int(input("How many pack(s) of spaghetti will you like to buy: "))
spaghetti_price = spaghetti * spaghetti_quantity

egg_quantity = int(input("How many crate of eggs will you like to buy: "))
egg_price = egg_quantity * egg_per_crate

salt_quantity = int(input("How many pack(s) of salt will you like to buy: "))
salt_price = salt_quantity * salt

maggi_quantity = int(input("How many pack(s) of maggi will you like to buy: "))
maggi_price = maggi_quantity * maggi

print(f"""                                      
    Asher & Sons Group of Companies
    312 Herbert Macaulay Way, Sabo, Yaba
    07014014018 florenceasher@gmail.com
**************************************************
""")
print(f"""
**************************************************
products        price       quantity        amount
**************************************************
""")

print(f"rice\t             {rice_per_kilogram}\t      {rice_quantity}\t      {rice_price}")
print(f"beans\t             {beans_per_kilogram}\t      {beans_quantity}\t      {beans_price}")
print(f"spaghetti\t         {spaghetti}\t      {spaghetti_quantity}\t      {spaghetti_price}")
print(f"eggs\t             {egg_per_crate}\t      {egg_quantity}\t      {egg_price}")
print(f"salt\t             {salt}\t          {salt_quantity}\t      {salt_price}")
print(f"maggi\t             {maggi}\t      {maggi_quantity}\t      {maggi_price}")

# print("""
# ************************************
# Thanks for your patronage
# ************************************
# """)