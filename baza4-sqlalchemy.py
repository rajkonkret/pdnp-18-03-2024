# ORM - dostep do bazy danych w sposb obiektowy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


# echo=True - logi z bazy danych
engine = create_engine('sqlite:///mydatabase.db', echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

new_user = User(name="Jan Kowalski", age=30)
session.add(new_user)  # INSERT INTO users (name, age) VALUES (?, ?)
session.commit()
session.close()

users = session.query(User).all()
for user in users:
    print(user)
    print(user.name)

# <__main__.User object at 0x00000280176C22D0>
# Jan Kowalski
# <__main__.User object at 0x00000280176C2270>
# Jan Kowalski
# <__main__.User object at 0x00000280176C1D60>
# Jan Kowalski
# <__main__.User object at 0x00000280176C1CD0>
# Jan Kowalski
