from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from pyhtonProject4.security import authenticate, identity
from pyhtonProject4.resources.user import Userregister
from pyhtonProject4.resources.item import Item, Itemlist
from pyhtonProject4.db import db
from pyhtonProject4.resources import Store, StoreList


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'maya'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity)  # /auth


api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(Itemlist, '/items')
api.add_resource(StoreList, '/stores')

api.add_resource(Userregister, '/userregister')

if __name__ == "__main__":
    db.init_app(app)
    app.run()



