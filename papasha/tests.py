from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.util import b64encode
from flask_testing import TestCase
from papasha.models import *
from main import *

engine = create_engine('sqlite:///database.db', echo=True, connect_args={'check_same_thread': False})
Session = sessionmaker(bind=engine)
Base.metadata.bind = engine


class Tests(TestCase):
    app.config['TESTING'] = True
    app.config['LIVESERVER_PORT'] = 5000

    def create_app(self):
        return app

    def setUp(self):
        session = Session()
        Base.metadata.drop_all()
        Base.metadata.create_all()
        user = User(username="Ostap", password='$2b$12$uch6JHQ.RPyp9Vldn7fTAuMMne8gl0Ae0h/KQTtOy3ACDcwpfbeM2')
        user2 = User(username="Alex", password='$2b$12$WS9clYn2x68I/Z1c6LBlOOe.7A1JFZo9ygeKIBsNAJt.obSQ4FQVS')
        provisor1 = Provisor(provisorname="Valodya", provisorpass="$2b$12$065Q4s8QHQ62e4TDGjXPx.HF9tqS5.3GFTgMnFwakD/YZr2DHO.eK")
        item1 = Item(name='Mezym', quantity=30, price='29.90', describe='123 mezym, pislya yizhi lehshe z nym')
        item2 = Item(name='Sorbex', quantity=100, price='200', describe='sorbex vid zhyvota')
        order1 = Order(order_user_id=1, order_item_id=1, quantity_in_order=10)
        order2 = Order(order_user_id=1, order_item_id=2, quantity_in_order=13)
        session.add(user)
        session.add(user2)
        session.add(provisor1)
        session.add(item1)
        session.add(item2)
        session.add(order1)
        session.add(order2)
        session.commit()
        session.close()


class TestApi(Tests):
    def test_user_post(self):
        test = self.client.post("/user", data={"username": "os", "password": "pass"})
        print(test.data)
        self.assertEqual(405, test.status_code)

    def test_getuserbyid(self):
        credentials = b64encode(b"Ostap:pass123")
        res = self.client.get("/user/1", headers={"Authorization": f"Basic {credentials}"})
        assert res.status_code == 200

    def test_getuserbyidwrong(self):
        credentials = b64encode(b"Ostap:Pass123")
        res = self.client.get("/user/10", headers={"Authorization": f"Basic {credentials}"})
        assert res.status_code == 404