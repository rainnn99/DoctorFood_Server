# pip install Flask

from flask import Flask, render_template, url_for, session, request, redirect
import sys

app = Flask(__name__)
app.secret_key = "lfko2dfk5-!fgkfiapvn4"


def main():
    app.run(host='0.0.0.0', port=5000)


if __name__ == "__main__":
    main()


ID = 123  # DB 에서 불러오기
PW = 123  # DB 에서 불러오기

# 홈화면


@app.route('/')
def home():
    if 'id' in session:
        return render_template('home.html', login=True)
    else:
        return render_template("home.html", login=False)

# 로그인


@app.route('/login', methods=["post"])
def login():
    global ID, PW
    _id_ = request.args.get("id")
    _password_ = request.args.get("pw")

    for i in ID:
        if _id_ == ID and _password_ == PW:
            session['id'] = _id_
            return redirect(url_for("home"))
        else:
            return redirect(url_for("home"))

# 로그아웃


@app.route('/logout')
def logout():
    session.pop("id")
    return redirect(url_for("home"))
