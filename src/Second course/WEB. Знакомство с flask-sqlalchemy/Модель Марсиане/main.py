from flask import Flask
from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    app.run()


if __name__ == '__main__':
    db_session.global_init("db/people.db")
    main()
