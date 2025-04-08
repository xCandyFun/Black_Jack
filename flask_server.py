from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/normal_game')
def normal_black_jack():
    return render_template("normal_black_jack.html")

@app.route('/special_game')
def special_black_jack():
    return render_template("special_black_jack.html")

@app.route('/normal_rules')
def normal_game_rules():
    return render_template("normal_game_rules.html")

@app.route('/special_rules')
def special_Game_rules():
    return render_template("special_game_rules.html")


if __name__ == '__main__':
    app.run(debug=True)