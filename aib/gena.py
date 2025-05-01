api_op = "open router api"

EMAIL = "hf email"
PASSWD = "hf password"

from openai import OpenAI
from pydub import *
from gtts import gTTS
import os
import shutil
from hugchat import hugchat
from hugchat.login import Login


cookie_path_dir = "data/cookies/"
sign = Login(EMAIL, PASSWD)
cookies = sign.login(cookie_dir_path=cookie_path_dir, save_cookies=True)
chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
chatbot.switch_llm(0)

client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=api_op)

def gen(topic, provider=0):
    if provider == 0:
        return chatbot.chat(topic).wait_until_done()
    
    if provider == 1:
        completion = client.chat.completions.create(
        model="meta-llama/llama-4-scout:free",
        messages=[{"role": "user", "content": topic}])

        return completion.choices[0].message.content

def pers_choice(character=str):
    match character:
        case 'Роза:': return "rose"
        case 'Дружок:': return "druzhok"
        case 'Малыш:': return "malish"
        case 'Гена:': return "gena"
        case 'Лиза:': return "liza"
        case 'Тимоха:': return "timokha"
        case 'Мама:': return "rose"
        case 'Папа:': return "ded"
        case 'Дедушка:': return "ded"
        case _: return "dictor"

def remove_name(text):
    words = text.split()
    return " ".join(words[1:])

def clean_dialog(folder_path="data\\dialog_voice"):
    shutil.rmtree(folder_path)
    os.mkdir(folder_path)
        
def btts(text=str, voice_cur = str, num = 0, path_output = str, speek = 0):
    available_index = f"-ip data\\voice_model\\{voice_cur}\\{voice_cur}.index "
    if voice_cur == "timokha":
        available_index = ""
    
    if speek == 0:
        tts = gTTS(text=text, lang='ru')
        tts.save("voice.wav")
    if speek == 1:
        pass
    
    os.system(f"python -m rvc_python cli -i voice.wav -o {path_output}\\pers{num}.wav -mp data\\voice_model\\{voice_cur}\\{voice_cur}.pth {available_index} -de cuda:0")
    
def connect_audio(input_folder, output_file_name):
    sum((AudioSegment.from_file(f"{input_folder}\\pers{i}.wav") for i in range(len(os.listdir(input_folder)))), AudioSegment.empty()).export(f"{output_file_name}.wav", format="wav")