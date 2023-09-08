import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Publisher(Base):
  __tablename__ = "Publisher"

  id = sq.Column(sq.Integer, primary_key=True)
  name = sq.Column(sq.String(length=40), unique=True)


class Book(Base):
  __tablename__ = "Book"

  id = sq.Column(sq.Integer, primary_key=True)
  title = sq.Column(sq.String(length=40), unique=True)
  publisher_id = sq.Column(sq.Integer, sq.ForeignKey("Publisher.id"), nullable=False)

  publisher = relationship(Publisher, backref="Book")


class Shop(Base):
  __tablename__ = "Shop"

  id = sq.Column(sq.Integer, primary_key=True)
  name = sq.Column(sq.String(length=40), unique=True, nullable=False)


class Stock(Base):
  __tablename__ = "Stock"

  id = sq.Column(sq.Integer, primary_key=True)
  book_id = sq.Column(sq.Integer, sq.ForeignKey("Book.id"), nullable=False)
  shop_id = sq.Column(sq.Integer, sq.ForeignKey("Shop.id"), nullable=False)
  count = sq.Column(sq.Integer, nullable=False)

  book = relationship(Book, backref="Stock")
  shop = relationship(Shop, backref="Stock")

class Sale(Base):
  __tablename__ = "Sale"

  id = sq.Column(sq.Integer, primary_key=True)
  price = sq.Column(sq.Integer, nullable=False)
  date_sale = sq.Column(sq.Date, nullable=False)
  stock_id = sq.Column(sq.Integer, sq.ForeignKey("Stock.id"), nullable=False)
  count = sq.Column(sq.Integer, nullable=False)

  stock = relationship(Stock, backref="sale")


def create_tables(engine):
  # Base.metadata.drop_all(engine)
  Base.metadata.create_all(engine)
