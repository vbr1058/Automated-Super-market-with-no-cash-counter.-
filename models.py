from peewee import *
db=SqliteDatabase("SuerMarket.db")

class user(Model):
	user_name=CharField()
	passward=CharField()
	class Meta:
		database=db

class Marchent_item(Model):
	item_name=CharField()
	item_cost=FloatField()
	class Meta:
		database=db

class customer_item(Model):
	item_name=ForeignKeyField(Marchent_item, backref="customer")
	item_cost=ForeignKeyField(Marchent_item, backref="customer")
	class Meta():
		database=db

if __name__=='__main__':
	db.connect()
	db.create_tables([user,Marchent_item,customer_item]) 