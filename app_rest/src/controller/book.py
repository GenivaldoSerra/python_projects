from flask import request
from flask_restplus import Resource, fields

from src.models.book import BookModel
from src.schemas.book import BookSchema

from src.server.instance import server

book_ns = server.book_ns

book_schema = BookSchema()
boo_list_schema = BookSchema(many=True)

class Book(Resource):
    def get(self, id):
        book = BookModel.find_by_id(id)
        if book:
            return book_schema.dump(book), 200
        return {'message': 'Book not found'}, 404

    def delete(self, id):
        book = BookModel.find_by_id(id)
        if book:
            book.delete_from_db()
            return {'message': 'Book deleted.'}, 200
        return {'message': 'Book not found.'}, 404