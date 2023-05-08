# pip install Flask

from flask import Flask, render_template
import sys

app = Flask(__name__)


@app.route('/')
def test():
    return render_template("test.html")


def main():
    app.run(host='0.0.0.0', port=80)


if __name__ == "__main__":
    main()
