from sqlalchemy.orm import sessionmaker
from papasha.models import *

Session = sessionmaker(bind=engine)
session = Session()

user = User(username="Ostap",password='Ostappassword')
user2 = User(username="Alex",password='Alexpassword')
provisor1=Provisor(provisorname="Valodya",provisorpass="Valodyapassword")
item1=Item(name='Mezym',quantity=30,price='29.90',describe='123 mezym, pislya yizhi lehshe z nym')
item2=Item(name='Sorbex',quantity=100,price='200',describe='sorbex vid zhyvota')
order1=Order(order_user_id=1,order_item_id=1,quantity_in_order=10)
order2=Order(order_user_id=1,order_item_id=2,quantity_in_order=13)
session.add(user)
session.add(user2)
session.add(provisor1)
session.add(item1)
session.add(item2)
session.add(order1)
session.add(order2)
session.commit()
session.close()
