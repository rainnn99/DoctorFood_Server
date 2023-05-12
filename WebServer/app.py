# pip install Flask

from flask import Flask, render_template, url_for, session, request, redirect
import sys
import pymysql

app = Flask(__name__)
app.secret_key = "lfko2dfk5-!fgkfiapvn4"


conn = pymysql.connect(host='localhost',
                       user='root',
                       password='',  # 비밀번호
                       db='food_recommendation',
                       charset='utf8')


def main():
    app.run(host='0.0.0.0', port=5000)


if __name__ == "__main__":
    main()


#  홈화면
@app.route('/')
def home():
    if 'id' in session:
        return render_template('home.html', login=True)
    else:
        return render_template("home.html", login=False)


# 로그인
# @app.route('/login')
# def login():
#    return render_template('login.html')

# 로그인
# 아이디 비밀번호 확인
@app.route('/login', methods=["post"])
def login():
    id = request.args.get("id")
    password = request.args.get("password")

    with conn:
        with conn.cursor() as cursor:
            cursor.execute(
                'SELECT * FROM customer WHERE username = %s AND password = %s', (id, password))
            user = cursor.fetchone()

    if user:
        session['id'] = user[1]
        return redirect(url_for("home"))
    else:
        return redirect(url_for("home"))

# 로그아웃


@app.route('/logout')
def logout():
    session.pop("id")
    return render_template('home.html')


# 회원가입
@app.route('/signup', methods=['POST'])
def sign_up():
    id = request.args.get("id")
    password = request.args.get("password")
    name = request.args.get("name")
    birth = request.args.get("birth")
    sex = request.args.get("sex")
    phone_number = request.args.get("phone_number")
    email = request.args.get("eamil")
    job = request.args.get("job")
    height = request.args.get("height")
    weight = request.args.get("weight")
    bmi = request.args.get("bmi")

    sql = "INSERT INTO customer (id, password, name, birth, sex, phone_number, email, job, height, weight, bmi) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    with conn:
        with conn.cursor() as cur:
            cur.execute(sql, (id, password, name, birth, sex,
                        phone_number, email, job, height, weight, bmi))
            conn.commit()

    return redirect(url_for("login"))


# 커뮤니티_글작성
@app.route('/community_writing', methods=['POST'])
def community_writing():
    id = request.args.get("id")
    title = request.args.get("title")
    main_text = request.args.get("main_text")

    sql = "INSERT INTO community (id, title, main_text) VALUES (%s, %s, %s)"

    with conn:
        with conn.cursor() as cur:
            cur.execute(sql, (id, title, main_text))
            conn.commit()

    return redirect(url_for("community_list"))


# 커뮤니티_글목록
@app.route('/community_list', methods=['POST'])
def community_list():

    sql = "select * from community"

    with conn:
        with conn.cursor() as cur:
            cur.execute(sql)

    row = cur.fetchall()

    return render_template('community.html', row=row)

# 음식추천


@app.route('/food_recommendation', methods=['POST'])
def food_recommendation():
    sql_preferred_food = "select * from preferred_food"

    with conn:
        with conn.cursor() as cur:
            cur.execute(sql_preferred_food)

    preferred_food = cur.fetchall()

    sql_healthy_food = "select * from healthy_food"

    with conn:
        with conn.cursor() as cur:
            cur.execute(sql_healthy_food)

    healthy_food = cur.fetchall()

    return render_template('recommendation.html', preferred_food=preferred_food, healthy_food=healthy_food)


# 게임
