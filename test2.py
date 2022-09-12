from cgitb import text
from email import message, message_from_file
from fileinput import filename
from re import S, U
import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
from test import DBHelper
import test3 as img


dbx = DBHelper()
dbx.setup()
userid = 0
channelname = 0 
e = 0
amount = 0 
bot = Bot(token='5455991149:AAGezFfpSLxlwIJ_XEArPE56apWAKa6_0jU')
 
moneywith = 0
storage = MemoryStorage()  # external storage is supported!
dp = Dispatcher(bot, storage=storage)
menu_markupd = types.ReplyKeyboardMarkup(resize_keyboard=True ,selective=True)
menu_markupd.add("🔊Advertise")
menu_markupd.add("📢My Channels", "🤖My Bots")
menu_markupd.add("📥Deposit")
menu_markupd.add("Balance💰","💲Withdraw") 
menu_markupd.add("Support❓")
catagory1 = []
catagoryad = 0
def catagoryfun():
    global catagoryad, catagory1
    catagoryad = InlineKeyboardMarkup()
    items = dbx.get_catagory()
    for i in range(len(items)):
            b=items[i] 
            if str(b) == "None" or b in catagory1:
                test = 1
            else:
                a = InlineKeyboardButton(text=b, callback_data=b)   
                catagoryad.add(a)
                catagory1.append(b)
    b2 = InlineKeyboardButton(text="🔙 Back", callback_data="back2")
    catagoryad.add(b2)



catagory = types.ReplyKeyboardMarkup(resize_keyboard=True ,selective=True , one_time_keyboard=True)
catagory.add("Video Games")
catagory.add("News and Media")
catagory.add ("Music")
catagory.add ("Movie")
catagory.add("Motivation & Self-Development")
catagory.add("Humor & Memes")
catagory.add("Food & Cooking")
catagory.add("Online Shopping")
catagory.add("Fitness")
catagory.add("Fashion")
catagory.add("Earnings")
catagory.add("Computer science")
catagory.add("Cryptocurrencies")
catagory.add("Bets & Gambling")


bot1 = dict() 
channelist = dict()

def dechannelist():
    global channelist
    channelist = dict()
def channelist2():
    
    global channelist
    channelist[userid] = types.ReplyKeyboardMarkup(resize_keyboard=True ,selective=True)
    items = dbx.get_items(userid)
    for i in range(len(items)):
        b=items[i]
        if str(b) == "None":
            test = 1
        else:  
            channelist[userid].add(str(b))
    channelist[userid].add("➕Add Channel",'🔙 Back', "❌Delete Channel")

def debot():
    global bot1
    bot1 = dict()
def bot2():
    
    global bot1
    bot1[userid] = types.ReplyKeyboardMarkup(resize_keyboard=True ,selective=True)
    items = dbx.get_bot(userid)
    for i in range(len(items)):
        b=items[i]
        if str(b) == "None":
            test = 1
        else:     
            bot1[userid].add(str(b))
    bot1[userid].add("➕Add Bot",'🔙 Back', "❌Delete Bot")



withdraw1 = types.ReplyKeyboardMarkup(resize_keyboard=True ,selective=True, one_time_keyboard=True)
withdraw1.add("🏧Litcoin")
withdraw1.add("🏧Tether")
withdraw1.add("🏧Tele-Birr")
withdraw1.add('🔙 Back')


withdraw = types.ReplyKeyboardMarkup(resize_keyboard=True ,selective=True, one_time_keyboard=True)
withdraw.add("Litcoin(LTC)")
withdraw.add("Tether(USDT)")
withdraw.add("Tele Birr")
withdraw.add('🔙 Back')


advetiserlist = []
advetiserlist1 = []
b1 = InlineKeyboardButton(text="Channels", callback_data="choice")
b2 = InlineKeyboardButton(text="Bots", callback_data="choice1")
b3 = InlineKeyboardButton(text="🔙 Back", callback_data="back4")
chose = InlineKeyboardMarkup().add(b1, b2)
chose.add(b3)
advetiser = 0
advetiserbot = 0

def advertiserfun1():
    global advetiser, advetiserlist

    advetiser = InlineKeyboardMarkup()
    items = dbx.get_add2()

    for i in range(len(items)):
        b=items[i] 
        if str(b) == "None":
            test = 1
        else:
            a = InlineKeyboardButton(text=b, callback_data=b)   
            advetiser.add(a)
            advetiserlist.append(b)
    b2 = InlineKeyboardButton(text="🔙 Back", callback_data="back1")
    advetiser.add(b2)
def advertiserfun(owner):
    global advetiser, advetiserlist

    advetiser = InlineKeyboardMarkup()
    items = dbx.get_add(owner)

    for i in range(len(items)):
        b=items[i] 
        if str(b) == "None":
            test = 1
        else:
            a = InlineKeyboardButton(text=b, callback_data=b)   
            advetiser.add(a)
            advetiserlist.append(b)
    b2 = InlineKeyboardButton(text="🔙 Back", callback_data="back1")
    advetiser.add(b2)   
def advertiserfunbot():
    global advetiserbot, advetiserlist1
    advetiserbot = InlineKeyboardMarkup()
    itemsbott = dbx.get_bit()
    for i in range(len(itemsbott)):
        b=itemsbott[i]

        if str(b) == "None":
            test = 1
        else:
            a = InlineKeyboardButton(text=b, callback_data=b)    
            advetiserbot.add(a)
            advetiserlist1.append(b)
    b2 = InlineKeyboardButton(text="🔙 Back", callback_data="back3")
    advetiserbot.add(b2)
msg = 0 


class Form(StatesGroup):
    ltc = State()
    tele = State()
    USDT = State()
    ltc1 = State()
    tele1 = State()
    USDT1 = State()
    channel = State()
    dele = State()
    bot3 = State()
    dele1 = State()
    botadd = State()
    channelname = State()
    channelcat = State()
    channeldisc = State()
    channelprice = State()
    botprice =  State()
    bottime =  State()
    botname =  State() 
    botusers = State()
    botdisc = State()
    advertiserpost = State()
    advertiserpost48 = State()
    advertiserpost72 = State()
    withdraw = State()
    advertiserpostbot = State()
    advertiserpost25 = State()
    addprice = State()
    info = State()
    addprice1 = State()


channelname2 = 0
channelname1 = 0
channelcat1 = 0
channeldisc1 = 0
channelprice1 = 0
botprice = 0
bottime = 0
botname = 0
botusers = 0
botdisc = 0
botusername = 0

msg = 0
msg1 = 0
msg2 = 0
msg3 = 0
msg4 = 0
addbotprice = dict()

@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):  
    global userid
    userid = message.from_user.id
    await message.reply("Welcome " + message.from_user.first_name, reply_markup=menu_markupd)

@dp.message_handler(commands='add')
async def cmd_start(message: types.Message):  
    await Form.addprice.set()
    await message.reply("amount:-")

@dp.message_handler(commands='get')
async def cmd_start(message: types.Message):  
    await Form.info.set()
    await message.reply("channel name:-")

@dp.message_handler()
async def kb_answer(message: types.Message):
    global userid,msg
    if "Balance💰" in message.text:
     userid = message.from_user.id
     l = dbx.get_money(userid)
     moneylist = []
     for i in range(len(l)):
        b=l[i]
        if str(b) == "None":
            test = 1
        else:
            moneylist.insert(0, int(b))
            
     s = sum(moneylist)
     
     await message.answer(
   """ Balance:- 
🤴 User : """ + message.from_user.first_name  + """

💰USD: """ + """$""" + str(s), reply_markup=menu_markupd)


    if "📢My Channels" in message.text:
        advertiserfun1()
        userid = message.from_user.id
         
        channelist2()
        await     message.answer('Your Channels:-', reply_markup=channelist[userid])
    
    if "🤖My Bots" in message.text:
        advertiserfunbot()
        userid = message.from_user.id
         
        bot2()
        await     message.answer('Your Bots:-', reply_markup=bot1[userid])
         

    if "🔙 Back" in message.text:
      await message.answer(' Welcome', reply_markup=menu_markupd)
      
    if "💲Withdraw" in message.text:
        userid = message.from_user.id
        l = dbx.get_money(userid)
        moneylist = []
        for i in range(len(l)):
            b=l[i]
            if str(b) == "None":
                test = 1
            else:
                moneylist.insert(0, int(b))
  
        s = sum(moneylist) 
         
        if  25 <= s:
          await Form.withdraw.set()
          await message.answer('Enter 💲Withdraw Amount Minimum $25:-')
        else:
          await message.reply("insufficient Balance" ,reply_markup=menu_markupd)
          

    if "➕Add Channel" in message.text:
        await Form.channel.set()
        await message.answer("Enter Your Channel Username Without @ :- ")
    if "➕Add Bot" in message.text:
        await Form.botadd.set()
        await message.answer("Enter Your Bot Username Without @ :- ")
        await message.answer("To pass the moderation, the admin must add the text TELEGA_BOTCATALOG to the bot description. After adding the bot to the directory, the text can be removed.")
    if "Support❓"  in message.text:
       await message.answer("You can contact us using @ghostadvertsingchatbot", reply_markup=menu_markupd)

    if "Litcoin(LTC)" in message.text:
        await Form.ltc.set()
        await message.reply("Please Enter Your LTC Addrees + Network:-")
    if "Tether(USDT)" in message.text:
        await Form.USDT.set()
        await message.reply("Please Enter Your USDT Addrees + Network:-")
    if "Tele Birr" in message.text:
        await Form.tele.set()
        await message.reply("Please Enter Your Tele Birr Phone Number:-")
    if "❌Delete Channel" in message.text:
        await Form.dele.set()
        dechannelist()
        channelist2()
        await message.reply("Which Channel Do You Want To Delete:-", reply_markup=channelist[userid])
    if "❌Delete Bot" in message.text:
        await Form.dele1.set()
        debot()
        bot2()
        await message.reply("Which Bot Do You Want To Delete:-", reply_markup=bot1[userid])
    if "📥Deposit" in message.text:
        userid = message.from_user.id
        await message.answer('Select 📥Deposit Method:-', reply_markup=withdraw1)


    if "🏧Litcoin" in message.text:
        await bot.send_photo(userid, photo=open("LTC.jpg", 'rb'), caption= """
        Network:- LTC
Address:- MFA8HLE3BMz6akUtM4XqWzmMiJuRZiJeVR """ )
        await Form.ltc1.set()
        await message.reply("Please Enter Your Addrees That You Sent From:-")
    if "🏧Tether" in message.text:
        await bot.send_photo(userid, photo=open("USDT.jpg", 'rb'), caption= """
        Network:- TRX(TRC20)
Address:- TX451FWXaEwU8UWcVFWFkF3WRidH3eFyN2 """ )
        await Form.USDT1.set()
        await message.reply("Please Enter Your Addrees That You Sent From:-")
    if "🏧Tele-Birr" in message.text:
        await bot.send_photo(userid, photo=open("telebirr.jpg", 'rb'), caption= """
        Phone Number:- +251924135200
Name:- Nahom Getachew""" )
        await Form.tele1.set()
        await message.reply("Please Enter Your Tele Birr Phone Number:-")    
    if "🔊Advertise" in message.text:
        userid = message.from_user.id
        global msg4
        msg4 = await message.reply("On Which One Do You Want To Advertise:-", reply_markup=chose)

    if message.text in advetiserlist:
        
        channelname = message.text
        channeldisc = dbx.get_channaldescription(message.text)
        channelusername = dbx.get_channalname(message.text)
        addchannelprice = dbx.get_channalprice(message.text)
        channelcatagory = dbx.get_channalcatagory(message.text)
        b2 = InlineKeyboardButton(text="🔙 Back", callback_data="back")
        chose3 = InlineKeyboardMarkup()
        chose3.add(b2)
 
        msg = await bot.send_photo(userid, photo=open(str(' '.join(map(str, channelusername))) + ".jpg", 'rb'), caption=
"""    Channel:- """  + str(' '.join(map(str, channelname))) + """
    Channel Link:- t.me/""" + str(' '.join(map(str, channelusername))) + """
    Channel Description:- """ + str(' '.join(map(str, channeldisc))) + """
    Channel Catagory:- """ + str(' '.join(map(str, channelcatagory))) +"""
    Channel Price for 24 hours in the feed and
    1 hour in the top:- $""" + str(' '.join(map(str, addchannelprice))) , reply_markup=chose3)


    if message.text in advetiserlist1:
        
        botname = message.text
        botdisc = dbx.get_botdescription(message.text)
        botusername = dbx.get_botname(message.text)
        addbotprice = dbx.get_botprice(message.text)
        botprice = dbx.get_botactive(message.text)
        b2 = InlineKeyboardButton(text="🔙 Back", callback_data="back")
        chose56 = InlineKeyboardMarkup()
        chose56.add(b2)

        msg = await bot.send_photo(userid, photo=open(str(' '.join(map(str, botusername))) + ".jpg", 'rb'), caption=
""" Bot:- """  + str(' '.join(map(str, botname))) + """
    Bot Link:- t.me/""" + str(' '.join(map(str, botusername))) + """
    Bot Description:- """ + str(' '.join(map(str, botdisc))) + """
    Bot last Time Cheack:- """ + str(' '.join(map(str, botprice))) +"""
    Bot Price For All Users:- $""" + str(' '.join(map(str, addbotprice))) , reply_markup=chose56)





@dp.callback_query_handler(text=["choice", "choice1", "advertise", "back", "back1", "back2", "back3", "back4", "advertise2", "advertise24", "advertise48", "advertise72"])
async def random_value(call: types.CallbackQuery):
    global msg2, msg3
    if call.data == "choice":
        catagoryfun()
        
        msg2= await call.message.reply("Avilable Catagorys To Advertise On:-", reply_markup=catagoryad)
       
    if call.data == "choice1":
        advertiserfunbot()
        
        msg3 = await call.message.reply("Available Bots to Advetsie On:-", reply_markup=advetiserbot)

    if call.data == "advertise24":
        l = dbx.get_money(userid)
        moneylist = []
        for i in range(len(l)):
            b=l[i]
            if str(b) == "None":
                test = 1
            else:
                moneylist.insert(0, int(b))
  
        s = sum(moneylist)     
        if  int(addchannelprice[0]) <= s:
          await Form.advertiserpost.set()
          await call.message.reply("Please Send The Ad Post You Want To Show:- ") 
        else:
          await call.message.reply("insufficient Balance Please Deposit First:-" ,reply_markup=menu_markupd)
    if call.data == "advertise48":
        l = dbx.get_money(userid)
        moneylist = []
        for i in range(len(l)):
            b=l[i]
            if str(b) == "None":
                test = 1
            else:
                moneylist.insert(0, int(b))
  
        s = sum(moneylist)     
        if  int(addchannelprice[0])+1 <= s:
          await Form.advertiserpost48.set()
          await call.message.reply("Please Send The Ad Post You Want To Show:- ") 
        else:
          await call.message.reply("insufficient Balance Please Deposit First:-" ,reply_markup=menu_markupd)
    if call.data == "advertise72":
        l = dbx.get_money(userid)
        moneylist = []
        for i in range(len(l)):
            b=l[i]
            if str(b) == "None":
                test = 1
            else:
                moneylist.insert(0, int(b))
  
        s = sum(moneylist)     
        if  int(addchannelprice[0])+2 <= s:
          await Form.advertiserpost72.set()
          await call.message.reply("Please Send The Ad Post You Want To Show:- ") 
        else:
          await call.message.reply("insufficient Balance Please Deposit First:-" ,reply_markup=menu_markupd)  
    if call.data == "advertise2":
        l = dbx.get_money(userid)
        moneylist = []
        for i in range(len(l)):
            b=l[i]
            if str(b) == "None":
                test = 1
            else:
                moneylist.insert(0, int(b))
  
        s = sum(moneylist)     
        if  int(addbotprice[0]) <= s:
          await Form.advertiserpostbot.set()
          await call.message.reply("Please Send The Ad Post You Want To Show:- ") 
        else:
          await call.message.reply("insufficient Balance Please Deposit First:-" ,reply_markup=menu_markupd)
    if call.data == "back":
        await bot.delete_message(userid, msg["message_id"])
    if call.data == "back1":
        await bot.delete_message(userid, msg1["message_id"])
    if call.data == "back2":
        await bot.delete_message(userid, msg2["message_id"])
    if call.data == "back3":
        await bot.delete_message(userid, msg3["message_id"])
    if call.data == "back4":
        await bot.delete_message(userid, msg4["message_id"])
    await call.answer()

@dp.callback_query_handler(text=advetiserlist)
async def adverisercard(call: types.CallbackQuery ):
    global msg, addchannelprice, e, channelname
    channelname = call.data
    channeldisc = dbx.get_channaldescription(call.data)
    channelusername = dbx.get_channalname(call.data)
    addchannelprice = dbx.get_channalprice(call.data)
    channelcatagory = dbx.get_channalcatagory(call.data)
    b1 = InlineKeyboardButton(text="24 hours in the feed and 1 hour in the top(1/24)", callback_data="advertise24")
    b3 = InlineKeyboardButton(text="48 hours in the feed and 2 hour in the top(2/48)", callback_data="advertise48")
    b4 = InlineKeyboardButton(text="72 hours in the feed and 3 hour in the top(3/72)", callback_data="advertise72")
    b2 = InlineKeyboardButton(text="🔙 Back", callback_data="back")
    chose = InlineKeyboardMarkup().add(b1)
    chose.add(b3)
    chose.add(b4)
    chose.add(b2)
    e = addchannelprice[0]
    
    msg = await bot.send_photo(userid, photo=open(str(' '.join(map(str, channelusername))) + ".jpg", 'rb'), caption=
"""     Channel:- """  + str(' '.join(map(str, channelname))) + """
    Channel Link:- t.me/""" + str(' '.join(map(str, channelusername))) + """
    Channel Description:- """ + str(' '.join(map(str, channeldisc))) + """
    Channel Catagory:- """ + str(' '.join(map(str, channelcatagory))) +"""
    Channel Price:-
    24 hours in the feed and 1 hour in the top(1/24):- $""" + str(' '.join(map(str, addchannelprice))) + """
    48 hours in the feed and 2 hour in the top(2/48):- $""" + str(int(e) + 1) + """
    72 hours in the feed and 3 hour in the top(3/72):- $""" + str(int(e) + 2)  , reply_markup=chose)
    await call.answer()

@dp.callback_query_handler(text=advetiserlist1)
async def adverisercard(call: types.CallbackQuery ):
    global msg, addbotprice, botusername
    botname = call.data
    botdisc = dbx.get_botdescription(call.data)
    botusername = dbx.get_botname(call.data)
    addbotprice = dbx.get_botprice(call.data)
    botprice = dbx.get_botactive(call.data)
    b1 = InlineKeyboardButton(text="Advertise", callback_data="advertise2")
    b2 = InlineKeyboardButton(text="🔙 Back", callback_data="back")
    chose5 = InlineKeyboardMarkup().add(b1)
    chose5.add(b2)

    msg = await bot.send_photo(userid, photo=open(str(' '.join(map(str, botusername))) + ".jpg", 'rb'), caption=
""" Bot:- """  + str(' '.join(map(str, botname))) + """
    Bot Link:- t.me/""" + str(' '.join(map(str, botusername))) + """
    Bot Description:- """ + str(' '.join(map(str, botdisc))) + """
    Bot last Time Cheack:- """ + str(' '.join(map(str, botprice))) +"""
    Bot Price For All Users:- $""" + str(' '.join(map(str, addbotprice))) , reply_markup=chose5)
    await call.answer()


@dp.callback_query_handler(text=catagory1)
async def catagorycallback(call: types.CallbackQuery):
    advertiserfun(call.data)
    global msg1
    msg1 = await call.message.reply("Available Channels On This Catagory To Advetsie On:-", reply_markup=advetiser)
        
    await call.answer()


@dp.message_handler(state=Form.dele)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['dele'] = message.text
    global userid
    userid = message.from_user.id
    dbx.delete_item(message.text, userid)
    dechannelist()
    channelist2()
    await message.answer('Channel Deleted Your Channels:-', reply_markup=channelist[userid])  
    await bot.send_message(1201526685, "Channel deleted By:- " + message.from_user.username + " userid:- " + str(message.from_user.id) + " channel username:- " + message.text)

    await state.finish()    
    
@dp.message_handler(state=Form.dele1)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['dele1'] = message.text
    global userid
    userid = message.from_user.id
    dbx.delete_bot(message.text, userid)
    debot()
    bot2()
    await message.answer('Bot Deleted Your Bots:-', reply_markup=bot1[userid])  
    await bot.send_message(1201526685, "Bot deleted By:- " + message.from_user.username + " userid:- " + str(message.from_user.id) + " Bot username:- " + message.text)

    await state.finish()    

@dp.message_handler(state=Form.ltc)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['ltc'] = message.text
    global userid
    userid = message.from_user.id
    dbx.add_ltc(message.text, userid)
    dbx.add_money("-"+moneywith, userid)
    await message.answer('Thank you! We Will Notify You When You Recive Your Payment', reply_markup=menu_markupd)
    await bot.send_message(1201526685, "Ltc Withdraw Requested By:- " + str(message.from_user.id) + " Addres:- " + message.text + " Amount:- " + moneywith)

    await state.finish()


@dp.message_handler(state=Form.withdraw)
async def process_name30(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['withdraw'] = message.text
    global userid,moneywith
    userid = message.from_user.id
    moneywith = message.text
    
    await message.answer('Select 💲Withdraw Method:-', reply_markup=withdraw)

    await state.finish()


@dp.message_handler(state=Form.USDT)
async def process_name1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['USDT'] = message.text
    global userid
    userid = message.from_user.id
    dbx.add_money("-"+moneywith, userid)
    dbx.add_usdt(message.text, userid)
    await message.answer('Thank you! We Will Notify You When You Recive Your Payment', reply_markup=menu_markupd)
    await bot.send_message(1201526685, "Usdt Withdraw Requested By:- " + str(message.from_user.id) + " Addres:- " + message.text + " Amount:- " + moneywith)

    await state.finish()


@dp.message_handler(state=Form.tele)
async def process_name2(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['tele'] = message.text
    global userid
    userid = message.from_user.id
    dbx.add_tele(message.text, userid)
    dbx.add_money("-"+moneywith, userid)
    await message.answer('Thank you! We Will Notify You When You Recive Your Payment', reply_markup=menu_markupd)
    await bot.send_message(1201526685, "tele Withdraw Requested By:- " + str(message.from_user.id) + " Phone Number:- " + message.text + " Amount:- " + moneywith)

    await state.finish()   


@dp.message_handler(state=Form.channel)
async def process_name3(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['channel'] = message.text
    global channelname2
    await message.answer("Downlading Your Channel Profile Picture....")
    url = "https://t.me/" + message.text 
    img.getimg(url, message.text)
    channelname2 = message.text
    await message.answer("✅Done...")
    await Form.channelname.set()
    await message.reply("The name of your Telegram channel:-")


@dp.message_handler(state=Form.channelname)
async def process_name3(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['channelname'] = message.text
    global channelname1
    channelname1 = message.text
    await Form.channelcat.set()
    await message.reply("Now Select Your Channel Catagory:- ", reply_markup=catagory)

@dp.message_handler(state=Form.channelcat)
async def process_name3(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['channelcat'] = message.text
    global channelcat1
    channelcat1 = message.text
    await Form.channeldisc.set()
    await message.reply("Describe the features of your channel that will make you stand out:- ")

@dp.message_handler(state=Form.channeldisc)
async def process_name3(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['channeldisc'] = message.text
    await Form.channelprice.set()
    global channeldisc1
    channeldisc1 = message.text
    await message.reply("Price for 24 hours in the feed and 1 hour in the top(1/24) in Dollar Using 1$ = 52ETB :- ")

@dp.message_handler(state=Form.channelprice)
async def process_name3(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['channelprice'] = message.text
    global channelprice1, userid
    userid = message.from_user.id
    channelprice1 = message.text
    dbx.add_item(userid, channelname1, channelname2, channelcat1, channeldisc1, channelprice1)
    channelist2()
    await message.answer("Channel Added")
    await     message.answer('Your Channels:-', reply_markup=channelist[userid])
    await bot.send_message(1201526685, "New bot Added By:- " + message.from_user.username + " userid:- " + str(message.from_user.id) + " bot username:- " + message.text)
    await state.finish()



 
@dp.message_handler(content_types=[types.ContentType.PHOTO, types.ContentType.VIDEO, types.ContentType.TEXT], state=Form.advertiserpost)
async def process_name10(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['advertiserpost'] = "message.text"
        
    await bot.forward_message(1201526685, userid, message["message_id"])
    dbx.add_money("-"+str(e), userid)
    await bot.send_message(1201526685, "price:- $" + str(e) + " channel:- @" + str(' '.join(map(str, channelusername))) + " userid:- " + str(userid) )

    await state.finish()
    str(int(e) + 2)
@dp.message_handler(content_types=[types.ContentType.PHOTO, types.ContentType.VIDEO, types.ContentType.TEXT], state=Form.advertiserpost48)
async def process_name10(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['advertiserpost48'] = "message.text"
        
    await bot.forward_message(1201526685, userid, message["message_id"])
    dbx.add_money("-"+str(e), userid)
    await bot.send_message(1201526685, "price:- $" + str(int(e) + 1) + " channel:- @" + str(' '.join(map(str, channelusername))) + " userid:- " + str(userid))

    await state.finish()

@dp.message_handler(content_types=[types.ContentType.PHOTO, types.ContentType.VIDEO, types.ContentType.TEXT], state=Form.advertiserpost72)
async def process_name10(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['advertiserpost72'] = "message.text"
        
    await bot.forward_message(1201526685, userid, message["message_id"])
    dbx.add_money("-"+str(e), userid)
    await bot.send_message(1201526685, "price:- $" + str(int(e) + 2) + " channel:- @" + str(' '.join(map(str, channelusername))) + " userid:- " + str(userid) )
    await state.finish()
    
@dp.message_handler(content_types=[types.ContentType.PHOTO, types.ContentType.VIDEO, types.ContentType.TEXT], state=Form.advertiserpostbot)
async def process_name10(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['advertiserpostbot'] = "message.text"
    dbx.add_money("-"+str(' '.join(map(str, addbotprice))), userid)    
    await bot.forward_message(1201526685, userid, message["message_id"])
    await bot.send_message(1201526685, "price:- $" +  str(' '.join(map(str, addbotprice))) + " Bot:- @" + str(' '.join(map(str, botusername))) + " userid:- " + str(userid))

    await state.finish()



@dp.message_handler(state=Form.botadd)
async def process_name3(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['botadd'] = message.text
    await message.answer("Downlading Your Bot Profile Picture....")
    url = "https://t.me/" + message.text 
    img.getimg(url, message.text)
    global botusername
    botusername = message.text
    await message.answer("✅Done...")
    await Form.botname.set()
    await message.reply("Bots Name:- ")

@dp.message_handler(state=Form.botname)
async def process_name3(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['botname'] = message.text
    global botname
    botname = message.text
    await Form.botdisc.set()
    await message.reply("Bots Description:- ")

@dp.message_handler(state=Form.botdisc)
async def process_name3(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['botdisc'] = message.text
    global botdisc
    botdisc = message.text
    await Form.botusers.set()
    await message.reply("Bots Active Users:- ")

@dp.message_handler(state=Form.botusers)
async def process_name3(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['botusers'] = message.text
    global botusers
    botusers = message.text
    await Form.bottime.set()
    await message.reply("Last Time Cheacked:- ")

@dp.message_handler(state=Form.bottime)
async def process_name3(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['bottime'] = message.text
    global bottime
    bottime = message.text
    await Form.botprice.set()
    await message.reply("Price For All Users in Dollar Using 1$ = 52ETB:- ")



@dp.message_handler(state=Form.botprice)
async def process_name3(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['botprice'] = message.text

    global userid, botprice
    userid = message.from_user.id
    botprice = message.text
    dbx.add_bot(userid,botusername,botname,botdisc,botusers,bottime,botprice)
    await message.answer("Bot Added")
    bot2()
    await     message.answer('Your Bots:-', reply_markup=bot1[userid])
    await bot.send_message(1201526685, "New bot Added By:- " + message.from_user.username + " userid:- " + str(message.from_user.id) + " bot username:- " + message.text)
    await state.finish()




@dp.message_handler(state=Form.ltc1)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['ltc1'] = message.text
    global userid
    userid = message.from_user.id
    await message.answer('Thank you! We Will Notify You When We Verify Your Payment', reply_markup=menu_markupd)
    await bot.send_message(1201526685, "Ltc deposit Requested By:- " + str(message.from_user.id) + " Addres:- " + message.text)

    await state.finish()


@dp.message_handler(state=Form.USDT1)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['USDT1'] = message.text
    global userid
    userid = message.from_user.id
    await message.answer('Thank you! We Will Notify You When We Verify Your Payment', reply_markup=menu_markupd)
    await bot.send_message(1201526685, "usdt deposit Requested By:- " + str(message.from_user.id) + " Addres:- " + message.text)

    await state.finish()

@dp.message_handler(state=Form.tele1)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['tele1'] = message.text
    global userid
    userid = message.from_user.id
    await message.answer('Thank you! We Will Notify You When We Verify Your Payment', reply_markup=menu_markupd)
    await bot.send_message(1201526685, "tele deposit Requested By:- " + str(message.from_user.id) + " number:- " + message.text)

    await state.finish()


@dp.message_handler(state=Form.addprice)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['addprice'] = message.text
    global amount
    amount = message.text
    await Form.addprice1.set()
    await message.reply("userid:- ")


@dp.message_handler(state=Form.addprice1)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['addprice1'] = message.text
        
    dbx.add_money(amount, message.text)
    await message.answer("done")
    await state.finish()

@dp.message_handler(state=Form.info)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['info'] = message.text

    global msg        
    channelname = message.text
    channeldisc = dbx.get_channaldescription(message.text)
    channelusername = dbx.get_channalname(message.text)
    addchannelprice = dbx.get_channalprice(message.text)
    channelcatagory = dbx.get_channalcatagory(message.text)
    b2 = InlineKeyboardButton(text="🔙 Back", callback_data="back")
    chose3 = InlineKeyboardMarkup()
    chose3.add(b2)
 
    msg = await bot.send_photo(1201526685, photo=open(str(' '.join(map(str, channelusername))) + ".jpg", 'rb'), caption=
"""    Channel:- """  + str(' '.join(map(str, channelname))) + """
    Channel Link:- t.me/""" + str(' '.join(map(str, channelusername))) + """
    Channel Description:- """ + str(' '.join(map(str, channeldisc))) + """
    Channel Catagory:- """ + str(' '.join(map(str, channelcatagory))) +"""
    Channel Price for 24 hours in the feed and
    1 hour in the top:- $""" + str(' '.join(map(str, addchannelprice))) , reply_markup=chose3)
    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)



