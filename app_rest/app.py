from flask import jsonify
from marshmallow import ValidationError

from db import db
from ma import ma
from src.controller.book import Book, BookList
# from src.models.book import BookModel
from src.server.instance import server

api = server.api
app = server.app

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(Book, '/books/<int:id>')
api.add_resource(BookList, '/books')

if __name__ == '__main__':
    db.init_app(app)
    ma.init_app(app)
    server.run()