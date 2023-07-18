# ベースイメージ作成
FROM python:3

# requirements.txtをコピー
COPY requirements.txt .

# pipアップグレード
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# 作業ディレクトリ指定
WORKDIR /workdir/appserver/src

# 公開ポート指定
EXPOSE 5000

ENV FLASK_ENV="docker"
ENV FLASK_DEBUG=main.py

# COPY . src
CMD ["gunicorn", "--reload", "--bind", "0.0.0.0:5000", "main:app"]