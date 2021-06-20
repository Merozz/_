class Rooms(object):
    """Хранит названия, номера и уровни доступа комнат

        Названия и номер комнат должны различаться
    """
    class director:
        type = "director"
        number = 0
        lv = 4
    class teachers:
        type = "teachers room"
        number = 1
        lv = 3
    class studying:
        type = "studying room"
        number = 2
        lv = 2
    class act:
        type = "act"
        number = 3
        lv = 1

    room0 = director
    room1 = teachers
    room2 = studying
    room3 = act
    roomsmass = [room0,room1,room2,room3]
class User(object):
    """Хранит виды пользователей, их уровень и список всех пользователей

        У каждого пользователя должен быть свой тип
    """
    class student:
        type = "student"
        lv = 2
        def __init__(self, name, surname, strange):
            self.name = name
            self.surname = surname
            self.strange = strange
    class teacher(student):
        type = "teacher"
        lv = 3
    class parent(student):
        type = "visitor"
        lv = 1
    class director(student):
        type = "director"
        lv = 4

    user1 = student("Арсений", "Воронин", "Тотемное животное СУНЦ УрФУ")
    user2 = parent("Федор", "Томлиов", "Любопытный владелец Арсения Воронина")
    user3 = teacher("Нина", "Гейн", "Перехвалила Данила Клюкина")
    user4 = director("Dungeon", "Master", "Съедает 3 киндер буено в день")
    usermass = [user1, user2, user3, user4]
def showUserInfo(user):
    print(user.type, user.name, user.surname, user.strange)
def showRoomInfo(room):
    print(room.type, room.number, room.lv)
def check(user, room):
    if user.lv >= room.lv:
        print(f"{user.type} {user.name} {user.surname} пытается войти в {room.type} {room.number}: успех")
    else:
        print(f"{user.type} {user.name} {user.surname} пытается войти в {room.type} {room.number}: провал")
for i in range(len(User.usermass)):
    showUserInfo((User.usermass)[i])
for i in range(len(Rooms.roomsmass)):
    showRoomInfo((Rooms.roomsmass)[i])
for i in range(len(User.usermass)):
    for j in range(len(Rooms.roomsmass)):
        check(User.usermass[i], Rooms.roomsmass[j])










