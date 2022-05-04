from flask import Flask, jsonify
from query import get_animal_by_id

def main():

    app = Flask(__name__)
    app.config['JSON_AS_ASCII'] = False


    @app.route('/<int:id>')
    def get_post_by_id(id):
        """ Функция ищет по ID """

        animal = get_animal_by_id(id)
        return jsonify(animal)
    app.run()



if __name__ == '__main__':
    main()