from app.modules import app, db
from app.models import ProductType, Product, User

with app.app_context():
    db.create_all()

    cpu = ProductType(name="CPU")
    gpu = ProductType(name="GPU")
    hdd = ProductType(name="HDD")
    psu = ProductType(name="PSU")
    ram = ProductType(name="RAM")

    db.session.add_all([cpu, gpu, hdd, psu, ram])
    db.session.commit()

    corei7 = Product(manufacturer="Intel", product_type=1, name="Core i7", price=600)
    corei5 = Product(manufacturer="Intel", product_type=1, name="Core i5", price=400)
    corei3 = Product(manufacturer="Intel", product_type=1, name="Core i3", price=200)

    amd = Product(manufacturer="AMD", product_type=1, name="Threadripper", price=600)

    nvidia = Product(manufacturer="Nvidia", product_type=2, name="Geforce GTX 1070", price=600)

    db.session.add_all([corei7,corei5, corei3, amd, nvidia])
    db.session.commit()

    admin_user = User(username="admin", password="password123", role="Admin")
    admin_user.create()

