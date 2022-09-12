from ast import stmt
import sqlite3
from this import d


class DBHelper:
  def __init__(self, dbname="todo.sqlite"):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname)
        
  def setup(self):
    
    print("creating table")
    stmt = "CREATE TABLE IF NOT EXISTS items (owner text, channelusername text, channelname text, catagory, channeldescription text, price24hr text, botsusername text, bot text,  botdescription text,  Botsactiveruser text, lastcheack text, botprice text, money text, usdt text, tele text, ltc text)"
    self.conn.execute(stmt)
    self.conn.commit()



  def add_item(self, owner, item_text, channelname, catagory, channeldesc, price):
    stmt = "INSERT INTO items (owner, channelusername, channelname, catagory,  channeldescription, price24hr) VALUES (?, ?, ?, ?, ?, ?)"
    args = (owner, item_text, channelname, catagory, channeldesc, price )
    self.conn.execute(stmt, args)
    self.conn.commit()
  def add_bot(self, owner, botsusername, botdescription, lastcheack, botprice, bot,Botsactiveruser):
    stmt = "INSERT INTO items (owner, botsusername, bot, botdescription, Botsactiveruser, lastcheack, botprice) VALUES (?, ?, ?, ?, ?, ?, ?)"
    args = (owner,botsusername,botdescription,lastcheack,botprice,bot,Botsactiveruser)
    self.conn.execute(stmt, args)
    self.conn.commit()
  def add_ltc(self, item_text, owner):
    stmt = "INSERT INTO items (ltc, owner) VALUES (?, ?)"
    args = (item_text, owner)
    self.conn.execute(stmt, args)
    self.conn.commit()
  def add_money(self, item_text, owner):
    stmt = "INSERT INTO items (money, owner) VALUES (?, ?)"
    args = (item_text, owner)
    self.conn.execute(stmt, args)
    self.conn.commit()
  def add_usdt(self, item_text, owner):
    stmt = "INSERT INTO items (usdt, owner) VALUES (?, ?)"
    args = (item_text, owner)
    self.conn.execute(stmt, args)
    self.conn.commit()
  def add_tele(self, item_text, owner):
    stmt = "INSERT INTO items (tele, owner) VALUES (?, ?)"
    args = (item_text, owner)
    self.conn.execute(stmt, args)
    self.conn.commit()
  def delete_item(self, item_text, owner):
    stmt = "DELETE FROM items WHERE channelusername = (?) AND owner = (?)"
    args = (item_text, owner )
    self.conn.execute(stmt, args)
    self.conn.commit()
  def delete_bot(self, item_text, owner):
    stmt = "DELETE FROM items WHERE botsusername = (?) AND owner = (?)"
    args = (item_text, owner )
    self.conn.execute(stmt, args)
    self.conn.commit()
  def get_money(self, owner):
    stmt = "SELECT money FROM items WHERE owner = (?)"
    args = (owner, )
    return [x[0] for x in self.conn.execute(stmt, args)]
  def get_items(self, owner):
    stmt = "SELECT channelusername FROM items WHERE owner = (?)"
    args = (owner, )
    return [x[0] for x in self.conn.execute(stmt, args)]
  def get_bot(self, owner):
    stmt = "SELECT bot FROM items WHERE owner = (?)"
    args = (owner, )
    return [x[0] for x in self.conn.execute(stmt, args)]

  def get_add(self, owner):
    stmt = "SELECT channelusername FROM items WHERE catagory = (?)"
    args = (owner, )
    return [x[0] for x in self.conn.execute(stmt,args)]
  def get_add2(self):
    stmt = "SELECT channelusername FROM items"
    return [x[0] for x in self.conn.execute(stmt)]
  def get_bit(self):
    stmt = "SELECT bot FROM items"
    return [x[0] for x in self.conn.execute(stmt)]
  def get_id(self, owner):
    stmt = "SELECT owner FROM items WHERE channelusername = (?)"
    args = (owner, )
    return [x[0] for x in self.conn.execute(stmt,args)]
  def get_catagory(self):
    stmt = "SELECT catagory FROM items"
    return [x[0] for x in self.conn.execute(stmt)]
  def get_channalname(self, owner):
    stmt = "SELECT channelname FROM items WHERE channelusername = (?)"
    args = (owner, )
    return [x[0] for x in self.conn.execute(stmt,args)]
  def get_channalcatagory(self, owner):
    stmt = "SELECT catagory FROM items WHERE channelusername = (?)"
    args = (owner, )
    return [x[0] for x in self.conn.execute(stmt,args)]
  def get_channaldescription(self, owner):
    stmt = "SELECT channeldescription FROM items WHERE channelusername = (?)"
    args = (owner, )
    return [x[0] for x in self.conn.execute(stmt,args)]
  def get_channalprice(self, owner):
    stmt = "SELECT price24hr FROM items WHERE channelusername = (?)"
    args = (owner, )
    return [x[0] for x in self.conn.execute(stmt,args)]
  def get_botname(self, owner):
    stmt = "SELECT botsusername FROM items WHERE bot = (?)"
    args = (owner, )
    return [x[0] for x in self.conn.execute(stmt,args)]
  def get_botactive(self, owner):
    stmt = "SELECT Botsactiveruser FROM items WHERE bot = (?)"
    args = (owner, )
    return [x[0] for x in self.conn.execute(stmt,args)]
  def get_botdescription(self, owner):
    stmt = "SELECT botdescription FROM items WHERE bot = (?)"
    args = (owner, )
    return [x[0] for x in self.conn.execute(stmt,args)]
  def get_botprice(self, owner):
    stmt = "SELECT botprice FROM items WHERE bot = (?)"
    args = (owner, )
    return [x[0] for x in self.conn.execute(stmt,args)]
  def bot_last(self, owner):
    stmt = "SELECT lastcheack FROM items WHERE bot = (?)"
    args = (owner, )
    return [x[0] for x in self.conn.execute(stmt,args)]