from flask import Flask, jsonify
from query import get_animal_by_id

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/<int:id>')
def get_post_by_id(id_num):
    """ Функция ищет по ID """
    animal = get_animal_by_id(id_num)
    return jsonify(animal)


if __name__ == '__main__':
    app.run()
