from flask import Flask, render_template

app = Flask(__name__)


@app.route('/anna')
def index():
    personal_info = {'name': 'anna', 'phone number': '0477031423', 'email': 'anna.johnson@student.kdg.be'}
    return render_template('Anna.html', name=personal_info, )


if __name__ == '__main__':
    app.run(debug=True)
