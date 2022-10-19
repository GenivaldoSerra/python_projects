from ma import ma
from src.models.book import BookModel


class BookSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = BookModel
        load_instance = True
        include_fk = True