import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import Publisher, Book, Stock, Shop, Sale, create_tables
import json


def add_info(login, password, name_bd, name_file):
  DSN = f'postgresql://{login}:{password}@localhost:5432/{name_bd}'
  engine = sqlalchemy.create_engine(DSN)
  create_tables(engine)

  Session = sessionmaker(bind=engine)
  session = Session()

  with open(name_file) as f:
    data = json.load(f)
    for record in data:
      fld = record['fields']
      model = record['model']
      pk = record['pk']
      if model == 'publisher':
        session.add(
          Publisher(
            id=pk,
            name=fld['name']
            )
          )
      if model == 'book':
        session.add(
          Book(
            id=pk,
            title=fld['title'],
            publisher_id=fld['id_publisher']
            )
          )
      if model == 'shop':
        session.add(
          Shop(
            id=pk,
            name=fld['name']
            )
          )
      if model == 'stock':
        session.add(
          Stock(
            id=pk,
            shop_id=fld['id_shop'],
            book_id=fld['id_book'],
            count=fld['count']
            )
          )
      if model == 'sale':
          session.add(
            Sale(
              id=pk,
              price=int(float(fld['price'])),
              date_sale=fld['date_sale'],
              count=fld['count'],
              stock_id=fld['id_stock']
              )
            )

    session.commit()

  session.close()


def purchase_info(login, password, name_bd, publisher):
  DSN = f'postgresql://{login}:{password}@localhost:5432/{name_bd}'
  engine = sqlalchemy.create_engine(DSN)
  create_tables(engine)

  Session = sessionmaker(bind=engine)
  session = Session()

  if publisher.isdigit() == True:
     pub = Publisher.id
  else:
     pub = Publisher.name

  q = session.query(
      Book.title,
      Shop.name,
      Sale.price,
      Sale.date_sale
      ).join(
          Sale.stock
          ).join(
              Stock.shop
              ).join(
                  Stock.book
                  ).join(
                      Book.publisher
                      ).filter(pub == publisher)

  for s in q.all():
    date = s[3]
    date_str = date.strftime("%d-%m-%Y")
    print(f'{s[0]} | {s[1]} | {s[2]} | {date_str}')

  session.close()
