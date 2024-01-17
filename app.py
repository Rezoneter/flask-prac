# flask rewalk

from flask import Flask
from flask_restful import Api

# 기본 구조

app = Flask(__name__)

api = Api (app)

# APU 를 구분해서 실행시키는건 
# HTTP Method 와 URL 의 조합

# 경로와 리소스 연결


if __name__ == '__main__':
    app.run()

