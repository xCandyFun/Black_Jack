from flask import Flask, render_template, request, jsonify
from normal_black_jack import NormalBlackJackGame

app = Flask(__name__)
game = NormalBlackJackGame()

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/normal_game')
def normal_black_jack():
    return render_template("normal_black_jack.html")

@app.route('/hit', methods=['POST'])
def hit():
    card = game.get_a_card()  # use updated method name
    return jsonify({'card': card})

@app.route('/normal_rules')
def normal_game_rules():
    return render_template("normal_game_rules.html")

if __name__ == '__main__':
    app.run(debug=True)