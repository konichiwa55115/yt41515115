import os
from pyrogram import Client, filters
from pyrogram.types import ForceReply
import subprocess
import shutil
from os import system as cmd
from pyrogram.types import InlineKeyboardMarkup , InlineKeyboardButton , ReplyKeyboardMarkup , CallbackQuery
from yt_dlp import YoutubeDL

CHOOSE_UR_LANG = " Choose Your folmula ! "
CHOOSE_UR_LANG_BUTTONS = [
    [InlineKeyboardButton("vid 360p",callback_data="vid 360p")],
     [InlineKeyboardButton("vid 720p",callback_data="vid 720p")],
     [InlineKeyboardButton("aud",callback_data="aud")]
]
CHOOSE_UR_LANG2 = " Choose Your folmula ! "
CHOOSE_UR_LANG2_BUTTONS = [
    [InlineKeyboardButton("vid 360p",callback_data="vidcont360p")],
     [InlineKeyboardButton("vid 720p",callback_data="vidcont720p")],
     [InlineKeyboardButton("aud",callback_data="audcont")]
]
CHOOSE_UR_MOD = " Choose Your mode ! "
CHOOSE_UR_MOD_BUTTONS = [
    [InlineKeyboardButton("من البداية",callback_data="frmstrt")],
     [InlineKeyboardButton("استكمال",callback_data="cont")]
]


bot = Client(
    "myfirs",
    api_id=17983098,
    api_hash="ee28199396e0925f1f44d945ac174f64",
    bot_token="5714654934:AAEVIR8baWhJcgUOtWeNmrSjvdRfYRiY7tI"
)
@bot.on_message(filters.command('start') & filters.private)
def command1(bot,message):
    bot.send_message(message.chat.id, " االسلام عليكم أنا بوت التحميل من يوتيوب  ",disable_web_page_preview=True)
@bot.on_message(filters.command('clear') & filters.private)
def command2(bot,message):
    cmd('rm file.txt')
    shutil.rmtree('./downloads/')

@bot.on_message(filters.private & filters.reply )
async def refunc(client,message):
   if (message.reply_to_message.reply_markup) and isinstance(message.reply_to_message.reply_markup, ForceReply)  :
          global hazard
          hazard = message.text ;await message.delete()
          await message.reply(
             text = CHOOSE_UR_LANG2,
             reply_markup = InlineKeyboardMarkup(CHOOSE_UR_LANG2_BUTTONS))



@bot.on_message(filters.private & filters.incoming & filters.text  )
def _telegram_file(client, message):

  global user_id
  user_id = message.from_user.id 
  global felo
  felo = message
  global url
  url = message.text
  cmd(f'''yt-dlp --flat-playlist -i --print-to-file url file.txt {url}''')
  message.reply(
             text = CHOOSE_UR_MOD,
             reply_markup = InlineKeyboardMarkup(CHOOSE_UR_MOD_BUTTONS)

        )

@bot.on_callback_query()
def callback_query(CLIENT,CallbackQuery):
  CallbackQuery.edit_message_text(
      
      "جار التنزيل "
  )
  global numbofvid
  cmd(f'wc -l < file.txt > res.txt')
  with open('res.txt', 'r') as file:
        temp = file.read().rstrip('\n') 
  numbofvid = int(temp)
  cmd('unlink res.txt')
  if CallbackQuery.data == "vid 360p":
      CallbackQuery.edit_message_text("تجد ملفاتك هنا \n https://t.me/+asgctos1WR81OGI0 ")   
      zaza = 1
      while (zaza <= numbofvid): 
       cmd(f'sed -n {zaza}p file.txt > res.txt')
       with open('res.txt', 'r') as file:
        link = file.read().rstrip('\n')   
       
       try:
        cmd(f'''yt-dlp -f 18 -ciw  -o downloads/"%(title)s.%(ext)s" "{link}"''')
        cmd(f'''uploadgram -1001821573758 downloads''')
        shutil.rmtree('./downloads/')
       except FileNotFoundError: 
         pass  
       zaza += 1  
      CallbackQuery.edit_message_text("تم التنزيل ✅  تجد ملفاتك هنا \n https://t.me/+asgctos1WR81OGI0  ")   
      cmd(f'unlink file.txt')

  elif CallbackQuery.data == "vid 720p":
      CallbackQuery.edit_message_text("تجد ملفاتك هنا \n https://t.me/+asgctos1WR81OGI0 ")   
      zaza = 1
      while (zaza <= numbofvid): 
       cmd(f'sed -n {zaza}p file.txt > res.txt')
       with open('res.txt', 'r') as file:
        link = file.read().rstrip('\n')
       try:
        cmd(f'''yt-dlp -f 22 -ciw  -o downloads/"%(title)s.%(ext)s" "{link}"''')
        cmd(f'''uploadgram -1001821573758 downloads''')
        shutil.rmtree('./downloads/')
       except FileNotFoundError: 
         pass  
       zaza += 1  
      CallbackQuery.edit_message_text("تم التنزيل ✅  تجد ملفاتك هنا \n https://t.me/+asgctos1WR81OGI0 ")   
      cmd(f'unlink file.txt')

  elif CallbackQuery.data == "aud":
      CallbackQuery.edit_message_text("تجد ملفاتك هنا \n https://t.me/+asgctos1WR81OGI0 ")   
      zaza = 1
      while (zaza <= numbofvid): 
       cmd(f'sed -n {zaza}p file.txt > res.txt')
       with open('res.txt', 'r') as file:
        link = file.read().rstrip('\n')   
       try :
        cmd(f'''yt-dlp -ciw  --extract-audio --audio-format mp3  -o downloads/"%(title)s.%(ext)s"  "{link}"''')
       except FileNotFoundError: 
         pass  
       zaza += 1    
      cmd(f'''uploadgram -1001821573758 downloads''')
      shutil.rmtree('./downloads/')
      CallbackQuery.edit_message_text("تم التنزيل ✅ تجد ملفاتك هنا \n https://t.me/+asgctos1WR81OGI0 ")   
      cmd(f'unlink file.txt')
  elif CallbackQuery.data == "vidcont360p":
      CallbackQuery.edit_message_text("تجد ملفاتك هنا \n https://t.me/+asgctos1WR81OGI0 ")   
      zaza = int(hazard) +1
      while (zaza <= numbofvid): 
       cmd(f'sed -n {zaza}p file.txt > res.txt')
       with open('res.txt', 'r') as file:
        link = file.read().rstrip('\n')   
       
       try:
        cmd(f'''yt-dlp -f 18 -ciw  -o downloads/"%(title)s.%(ext)s" "{link}"''')
        cmd(f'''uploadgram -1001821573758 downloads''')
        shutil.rmtree('./downloads/')
        cmd('''rm res.txt''')
       except FileNotFoundError: 
         pass  
       zaza += 1  
      CallbackQuery.edit_message_text("تم التنزيل ✅  تجد ملفاتك هنا \n https://t.me/+asgctos1WR81OGI0 ")   
      cmd(f'unlink file.txt')

  elif CallbackQuery.data == "vidcont720p":
      CallbackQuery.edit_message_text("تجد ملفاتك هنا \n https://t.me/+asgctos1WR81OGI0 ")   
      zaza = int(hazard) +1
      while (zaza <= numbofvid): 
       cmd(f'sed -n {zaza}p file.txt > res.txt')
       with open('res.txt', 'r') as file:
        link = file.read().rstrip('\n')
       try :
        cmd(f'''yt-dlp -f 22 -ciw  -o downloads/"%(title)s.%(ext)s" "{link}"''')
        cmd(f'''uploadgram -1001821573758 downloads''')
        shutil.rmtree('./downloads/')
        cmd('''rm res.txt''')
       except FileNotFoundError: 
         pass   
       zaza += 1  
      CallbackQuery.edit_message_text("تم التنزيل ✅ \n  تجد ملفاتك هنا \n https://t.me/+asgctos1WR81OGI0  ")   
      cmd(f'unlink file.txt')

  elif CallbackQuery.data == "audcont":
      CallbackQuery.edit_message_text("تجد ملفاتك هنا \n https://t.me/+asgctos1WR81OGI0 ")   
      zaza = int(hazard) +1
      while (zaza <= numbofvid): 
       cmd(f'sed -n {zaza}p file.txt > res.txt')
       with open('res.txt', 'r') as file:
        link = file.read().rstrip('\n')   
       
       try :
        cmd(f'''yt-dlp -ciw  --extract-audio --audio-format mp3  -o downloads/"%(title)s.%(ext)s"  "{link}"''')
        cmd(f'''uploadgram -1001821573758 downloads''')
        shutil.rmtree('./downloads/')
        cmd('''rm res.txt''')
       except FileNotFoundError: 
         pass  
       zaza += 1           
      CallbackQuery.edit_message_text("تم التنزيل ✅ تجد ملفاتك هنا \n https://t.me/+asgctos1WR81OGI0 ")   
      cmd(f'unlink file.txt')
  elif CallbackQuery.data == "frmstrt":
      felo.reply_text(
             text = CHOOSE_UR_LANG,
             reply_markup = InlineKeyboardMarkup(CHOOSE_UR_LANG_BUTTONS)

        )
  elif CallbackQuery.data == "cont":
      felo.reply_text("الآن أدخل عدد الفيديوهات التي تم تحميلها ",reply_markup=ForceReply(True))
      CallbackQuery.edit_message_text(
      
      "👇"
   ) 

bot.run()
