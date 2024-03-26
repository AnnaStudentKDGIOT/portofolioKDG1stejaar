from flask import Flask, render_template

app = Flask(__name__)


# Mock function to get the list of Pokémon numbers
@app.route("/AnnaJohnson")
def hello_world(name=None):
    return render_template('AEJ.html', name=name)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000)
