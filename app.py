from flask import Flask

app = Flask(__name__)


@app.route('/')
def homepage():

    return 'Are you there, world? It\'s me, Ducky!'


@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):

    return f'Wait, how did you know {users_animal} is my favorite animal? You the FBI?'


@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):

    return f'Yummy! {users_dessert} is delicious :D'


@app.route('/madlibs/<adjective>/<noun>')
def mad_libs(adjective, noun):
    return f'Then the massive gorilla then saw a {adjective} {noun}, and was petrified!'


@app.route('/multiply/<num1>/<num2>')
def multiply(num1, num2):
    if (num1.isdigit() == True) (num2.isdigit() == True):
        solution = int(num1) * int(num2)
        return solution


if __name__ == '__main__':
    app.run(debug=True)