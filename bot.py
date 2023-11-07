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
    bot_token="6251349619:AAHWY6-_BIwHqTUzvH62ukVUThjohP13d5k"
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
  try: 
    with open('file.txt', 'r') as fh:
        if os.stat('file.txt').st_size == 0: 
            pass
        else:
            sent_message = message.reply_text('هناك عملية تحميل الآن يا نرم  ', quote=True)
            return
  except FileNotFoundError: 
    pass  
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
      zaza = 1
      while (zaza <= numbofvid): 
       cmd(f'sed -n {zaza}p file.txt > res.txt')
       with open('res.txt', 'r') as file:
        link = file.read().rstrip('\n')   
       
       with YoutubeDL() as ydl: 
        info_dict = ydl.extract_info(f'{link}', download=False)
        video_url = info_dict.get("url", None)
        video_id = info_dict.get("id", None)
        video_title = info_dict.get('title', None)    
       cmd(f'''yt-dlp -f 18 -ciw  -o ./downloads/"{video_title}.mp4" "{link}"''')
       cmd(f'''uploadgram "{user_id}" ./downloads/''')
       shutil.rmtree('./downloads/') 
       cmd(f'''rm res.txt ''' ) 
       zaza += 1  
      cmd(f'unlink file.txt')

  elif CallbackQuery.data == "vid 720p":
      zaza = 1
      while (zaza <= numbofvid): 
       cmd(f'sed -n {zaza}p file.txt > res.txt')
       with open('res.txt', 'r') as file:
        link = file.read().rstrip('\n')
       with YoutubeDL() as ydl: 
        info_dict = ydl.extract_info(f'{link}', download=False)
        video_url = info_dict.get("url", None)
        video_id = info_dict.get("id", None)
        video_title = info_dict.get('title', None)    
       cmd(f'''yt-dlp -f 22 -ciw  -o ./downloads/"{video_title}.mp4" "{link}"''')
       cmd(f'''uploadgram "{user_id}" ./downloads/''')
       shutil.rmtree('./downloads/') 
       zaza += 1  
      cmd(f'unlink file.txt')

  elif CallbackQuery.data == "aud":
      zaza = 1
      while (zaza <= numbofvid): 
       cmd(f'sed -n {zaza}p file.txt > res.txt')
       with open('res.txt', 'r') as file:
        link = file.read().rstrip('\n')   
       with YoutubeDL() as ydl: 
        info_dict = ydl.extract_info(f'{link}', download=False)
        video_url = info_dict.get("url", None)
        video_id = info_dict.get("id", None)
        video_title = info_dict.get('title', None)    
       cmd(f'''yt-dlp -ciw  --extract-audio --audio-format m4a  -o downloads/"%(title)s.%(ext)s"  "{link}"''')
       cmd(f'''uploadgram "{user_id}" ./downloads/''')
       shutil.rmtree('./downloads/') 
       zaza += 1    
      
      cmd(f'unlink file.txt')
  elif CallbackQuery.data == "vidcont360p":
      zaza = int(hazard) +1
      while (zaza <= numbofvid): 
       cmd(f'sed -n {zaza}p file.txt > res.txt')
       with open('res.txt', 'r') as file:
        link = file.read().rstrip('\n')   
       
       with YoutubeDL() as ydl: 
        info_dict = ydl.extract_info(f'{link}', download=False)
        video_url = info_dict.get("url", None)
        video_id = info_dict.get("id", None)
        video_title = info_dict.get('title', None)    
       cmd(f'''yt-dlp -f 18 -ciw  -o ./downloads/"{video_title}.mp4" "{link}"''')
       cmd(f'''uploadgram "{user_id}" ./downloads/''')
       shutil.rmtree('./downloads/') 
       zaza += 1  
      cmd(f'unlink file.txt')

  elif CallbackQuery.data == "vidcont720p":
      zaza = int(hazard) +1
      while (zaza <= numbofvid): 
       cmd(f'sed -n {zaza}p file.txt > res.txt')
       with open('res.txt', 'r') as file:
        link = file.read().rstrip('\n')
       with YoutubeDL() as ydl: 
        info_dict = ydl.extract_info(f'{link}', download=False)
        video_url = info_dict.get("url", None)
        video_id = info_dict.get("id", None)
        video_title = info_dict.get('title', None)    
       cmd(f'''yt-dlp -f 22 -ciw  -o ./downloads/"{video_title}.mp4" "{link}"''')
       cmd(f'''uploadgram "{user_id}" ./downloads/''')
       shutil.rmtree('./downloads/') 
       zaza += 1  
      cmd(f'unlink file.txt')

  elif CallbackQuery.data == "audcont":
      zaza = int(hazard) +1
      while (zaza <= numbofvid): 
       cmd(f'sed -n {zaza}p file.txt > res.txt')
       with open('res.txt', 'r') as file:
        link = file.read().rstrip('\n')   
       with YoutubeDL() as ydl: 
        info_dict = ydl.extract_info(f'{link}', download=False)
        video_url = info_dict.get("url", None)
        video_id = info_dict.get("id", None)
        video_title = info_dict.get('title', None)    
       cmd(f'''yt-dlp -ciw  --extract-audio --audio-format m4a  -o downloads/"%(title)s.%(ext)s"  "{link}"''')
       cmd(f'''uploadgram "{user_id}" ./downloads/''')
       shutil.rmtree('./downloads/') 
       zaza += 1           
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
