from flask import request
from flask_restplus import Resource, fields

from src.models.book import BookModel
from src.schemas.book import BookSchema
from src.server.instance import server

book_ns = server.book_ns

book_schema = BookSchema()
boo_list_schema = BookSchema(many=True)

ITEM_NOT_FOUND = 'Book not found'

item = book_ns('Book', {
    'title': fields.String(required=True, description='The book title'),
    'pages': fields.Integer(required=True, description='The book pages',),
    })

class Book(Resource):
    def get(self, id):
        book = BookModel.find_by_id(id)
        if book:
            return book_schema.dump(book), 200
        return {'message': ITEM_NOT_FOUND}, 404

    def delete(self, id):
        book = BookModel.find_by_id(id)
        if book:
            book.delete_from_db()
            return {'message': 'Book deleted.'}, 200
        return {'message': ITEM_NOT_FOUND}, 404

class BookList(Resource):
    def get(self):
        return {'books': boo_list_schema.dump(BookModel.find_all())}, 200

    @book_ns.expect(item)
    # @book_ns.doc('create_book')
    def post(self):
        book_json = request.get_json()
        book = book_schema.load(book_json)
        try:
            book.save_to_db()
        except:
            return {'message': 'An error occurred inserting the book.'}, 500
        return book_schema.dump(book), 201
