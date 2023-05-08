# pip install Flask

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return 'hello'


@app.route('/test')
def test():
    return render_template("test.html")


def main():
    app.run(host='127.0.0.1', debug=False, port=80)


if __name__ == "__main__":
    main()
