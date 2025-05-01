from gena import *
#from playsound import *
import time
import os

start_time = time.time()
# тема диалога
tema = """Малыш приведствует всех на своём репозитории в Github"""
provider = 0
tts = True

# расспаковка данных для генерации
with open('data.txt', 'r', encoding="utf-8") as f:
    data = f.read()
 
# генерация диалога
print("Генерация...")

dialog = gen(f"{data} {tema}", provider=provider)
print(dialog)

# парсер
print("Парсинг...")

clean_dialog()


for flow_str in range(len(dialog.split('\n'))):
    character_words = remove_name(dialog.split('\n')[flow_str])
    character_name = pers_choice(dialog.split('\n')[flow_str].split()[0])
    
    print(character_name, " ", character_words)
    
    if tts == True:
        btts(character_words, character_name, flow_str, "data\\dialog_voice", speek=0)
    flow_str += 1

if tts == True:
    os.remove("voice.wav")
    connect_audio("data\\dialog_voice","voices")

#os.system("cls")
print("Генерация окончена")
print("Весь диалог:")
print(dialog)
print("Время генерации: ", f"секунд {time.time()-start_time}, минут {(time.time()-start_time)/60}")
print(flow_str)
with open("data\\gen_time.txt","a", encoding="utf-8") as f:
    f.write(f"{(time.time()-start_time)/60}\n")


os.system("pause")