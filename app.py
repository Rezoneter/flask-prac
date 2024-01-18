# flask rewalk
# restful 이란 서버나 서비스에 존재하는 모든 자원에
# URL 을 부여해 활용하는 것을 말한다

from flask import request
from flask_jwt_extended import create_access_token, get_jwt, jwt_required
from flask_restful import Resource
from mysql_connection import get_connection
from mysql.connector import Error

from email_validator import validate_email, EmailNotValidError

from utils import check_password, hash_password

class UserResisterResource(Resource) :

    def post(self):
        # 클라이언트가 보낸 데이터 수용
        data = request.get_json()

        # 이메일 주소 형식 확인
        try:
            validate_email(data['email'])
        except EmailNotValidError as e:
            print(e)
            return {'error': str(e)}, 400
        
        # 비밀번호길이 확인
        if len(data['password']) < 4 or len(data['password']) > 14:
            return {'error': '암호길이가 적당하지 않습니다'}, 400
        
        # 비밀번호 암호화
        password = hash_password(data['password'])

        print(password)
        
        # DB의 user 테이블에 데이터 저장
        try:
            connection = get_connection()
            query = ''' insert into user
                        (email, password)
                        valuses
                        (%s, %s);'''
            record = (data['email'],
                      password)
            cursor = connection.cursor()
            cursor.execute(query, record)
            connection.commit()

            # insert 한 id 가져오기

            user_id = cursor.lastrowid

            cursor.close()
            connection.close()
        except Error as e :
            print(e)
            cursor.close()
            connection.close()
            return {'error' : str(e)}, 500
        
        # user table 의 id로 JWT token 생성
        access_token = create_access_token(user_id)

        # token 을 클라이언트에게 전달 -> response
        return {'result' : 'success',
                'access_token' : access_token}, 200
    