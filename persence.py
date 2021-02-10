from pypresence import Presence
import time
import random
from mcstatus import MinecraftServer
server = MinecraftServer.lookup("51.38.215.224:25568")
status = server.status()
query = server.query()

client_id = '809046854318555177'  # Put your Client ID here, this is a fake ID
RPC = Presence(client_id)  # Initialize the Presence class
RPC.connect()  # Start the handshake loop

try:
    mynick = open("nick.txt", "r")
except FileNotFoundError:
    print("Файл не найден")
    input("Нажмите для продолжения...")

quotes = [
    "Проходка 200 руб кста",
    f"Мой ник: {mynick.read()}",
    "Советую ставить JEI"
]  # The quotes to choose from



print("ВСЕ РАБОТАЕТ ПОШЛА ВОДА ПА ТРУБАМ")
while True:  # The presence will stay on as long as the program is running
    query = server.query()
    playersonline = str(query.players.names).strip("\'").strip("[").strip("]").replace(",", """
    """)
    RPC.update(details=quotes[0], state="Играю на Fratch Create", large_image="ea", large_text=f"Онлайн игроков: {status.players.online}", small_image="ae", small_text=f"Список игрпоков: {playersonline}") #Set the presence, picking a random quote
    time.sleep(5) #Wait a wee bit
    RPC.update(details=quotes[1], state="Играю на Fratch Create", large_image="ea", large_text=f"Онлайн игроков: {status.players.online}", small_image="ae", small_text=f"Список игрпоков: {playersonline}") #Set the presence, picking a random quote
    time.sleep(5) #Wait a wee bit
    RPC.update(details=quotes[2], state="Играю на Fratch Create", large_image="ea", large_text=f"Онлайн игроков: {status.players.online}", small_image="ae", small_text=f"Список игрпоков: {playersonline}") #Set the presence, picking a random quote
    time.sleep(5) #Wait a wee bit
