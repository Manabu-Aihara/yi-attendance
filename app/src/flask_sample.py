# ライブラリをインポート
from flask import Flask, render_template, request, redirect, url_for

# from config import Config
# cursor = Config.cursor()
# cursor.execute("select * from M_LOGGININFO")

# disp = ""
# for row in cursor.fetchall():
#     # disp = "ID:" + str(row[0]) + "  名前:" + row[1]
#     print(disp)

# cursor.close

# Flaskはインスタンスを生成する
app = Flask(__name__)
# デバッグを可能とする
app.config.update({'DEBUG': True })

# ここからウェブアプリケーション用のルーティングを記述
# index にアクセスしたときの処理
@app.route('/')
def hello():
    # return "Flask DBから取得 "+disp
    # Jinjaを使う
    title = "ようこそ"
    message = "DBから取得 "
    # index.html をレンダリングする
    return render_template('index.html', message=message, title=title)

@app.route('/user')
def move_user():
    return render_template('user.html')

# @app.route('/user/<int:num>')
# def disp_num():
#     return render_template('user.html', val=num)
@app.route('/index/<string:msg>')
def index(msg):
    return render_template('index.html', msg=msg)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888')
