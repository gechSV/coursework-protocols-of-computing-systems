from peewee import *

db = SqliteDatabase('db/database.db')


# Шаблон класса
class BaseModel(Model):
    id = PrimaryKeyField(unique=True)

    class Meta:
        database = db
        order_by = 'id'


# Категории новостей
class Category(BaseModel):
    category = TextField()

    class Meta:
        db_table = 'Categories'


# Новость
class NewsPost(BaseModel):
    category = ForeignKeyField(Category)
    date = DateField()
    title = TextField()
    text = TextField()
    image = TextField()

    class Meta:
        db_table = 'NewsPosts'
