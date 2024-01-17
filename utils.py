from passlib.hash import pbkdf2_sha256
from config import Config

# 원문비밀번호를 단방향 암호화 하는 함수
def hash_password(origianl_password) :
    origianl_password = origianl_password + Config.PASSWORD_SALT
    password = pbkdf2_sha256.hash(origianl_password)
    return password


# 유저가 로그인 할 때 
# 입력한 비밀번호가 암호화뇐 비밀번호와 맞는지
# 체크하는 함수
def check_password(orinal_password, hashed_password):
    orinal_password = orinal_password + Config.PASSWORD_SALT
    check = pbkdf2_sha256.verify(orinal_password,)
    return check






