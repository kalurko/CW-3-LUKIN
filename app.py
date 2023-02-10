from flask import Flask
from main.views import main_blueprint
from api.views import api_blueprint

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.register_blueprint(main_blueprint)
app.register_blueprint(api_blueprint)


@app.errorhandler(404)
def not_found_error(error):
    return 'Страница не найдена!'


@app.errorhandler(500)
def not_found_error(error):
    return 'Ошибка на сервере'


if __name__ == '__main__':
    app.run(debug=True)

