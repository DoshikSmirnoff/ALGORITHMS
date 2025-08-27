"""
Ты — игрок в текстовой игре.
Ты находишься в лабиринте из комнат. Каждая комната описана словарём и соединена с другими.
Твоя задача — найти выход, двигаясь по командам "влево", "вправо", "вперёд", "назад".
Если ты попадёшь в комнату с "выходом": True, ты победил!
"""

labirint = {
     "start": {
         "description": "Ты у входа в старый мрачный лабиринт. Только вперёд.",
         "вперед": "room1"
     },
     "room1": {
         "description": "Ты в круглой каменной комнате. Отсюда можно пойти влево или вперёд.",
         "влево": "room2",
         "вперед": "room3"
     },
     "room2": {
         "description": "Тёмная комната, стены покрыты плесенью. Только назад.",
         "назад": "room1"
     },
     "room3": {
         "description": "Яркая комната с лестницей. Есть путь вперёд и направо.",
         "вперед": "room4",
         "направо": "room5"
     },
     "room4": {
         "description": "Комната с древними письменами. Что-то шепчет тебе повернуть назад.",
         "назад": "room3"
     },
     "room5": {
         "description": "Ты видишь впереди свет в конце тоннеля! Возможно, это выход.",
         "вперед": "exit"
     },
     "exit": {
         "description": "Ты выбрался на свободу! 🌟 Поздравляем!",
         "выход": False
     }
 }

def play_game():
     position = "start"

     while True:
         room = labirint[position]
         print("\n🧱", room["description"])
         next_direction = input("Выберите следующее направление: ")
         next_room = labirint[position][next_direction]
         print(next_room)
         room = labirint[next_room]
         print("\n🧱", room["description"])
         next_direction = input("Выберите следующее направление: ")
         next_room = labirint[position][next_direction]
         print(next_room)
