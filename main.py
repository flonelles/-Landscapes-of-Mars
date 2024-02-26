from data.users import *
from flask import Flask
from data.db_session import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    global_init('db/mars_explorer.db')
    session = create_session()
    user2 = User()
    user2.surname = "Scott"
    user2.name = "Ridley"
    user2.age = 21
    user2.position = "captain"
    user2.speciality = "research engineer"
    user2.address = "module_1"
    user2.email = "scott_chief@mars.org"
    session.add(user2)
    user3 = User()
    user3.surname = "Jim"
    user3.name = "Carry"
    user3.age = 20
    user3.position = "boatswain"
    user3.speciality = "botanist"
    user3.address = "module_2"
    user3.email = "jim_carry@mars.org"
    session.add(user3)
    user4 = User()
    user4.surname = "Jonn"
    user4.name = "leon"
    user4.age = 25
    user4.position = "cook"
    user4.speciality = "builder"
    user4.address = "module_3"
    user4.email = "jonn_leon@mars.org"
    session.add(user4)
    session.commit()


if __name__ == '__main__':
    main()
