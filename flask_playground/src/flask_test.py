from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates', root_path='.', static_folder="static")


@app.route('/hello')
def hello():
    return render_template('hello_world.html', username='monkey')


@app.route('/bye')
def bye():
    input = request.args.get('name')
    input1 = request.args.get('food')
    return 'bye ' + input + ' ' + input1


@app.route('/name', methods=['GET', 'POST'])
def name():
    if request.method == 'GET':
        return render_template('hello_world1.html')
    elif request.method == 'POST':
        first = request.form.get('fname')
        last = request.form.get('lname')
        data = {'first': first, 'last': last}
        return render_template('hello_world1.html', last=last, first=first)


@app.route('/pokemon/<int:num>', )
def pokemon(num):
    Pokemons = ["Pikachu", "Charizard", "Squirtle", "Jigglypuff",
               "Bulbasaur", "Gengar", "Charmander", "Mew", "Lugia", "Gyarados"]
    return render_template("pokemon.html", num=num, pokemons=Pokemons, len=len(Pokemons))


@app.route('/length', methods=['GET', 'POST'])
def length():
    if request.method == 'GET':
        return render_template('length.html')
    elif request.method == 'POST':
        first = request.form.get('first')
        second = request.form.get('second')
        data = {'first': first, 'second': second}
        return render_template('length.html', second=second, first=first)


if __name__ == '__main__':
    app.run(debug=True)