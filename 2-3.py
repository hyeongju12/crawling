import requests

# GET : 요청, 값을 가져오는 역할
# POST :  생성, 액션
# PUT : 수정, 덮어씌우기
# DELETE : 삭제

res = requests.get('https://www.naver.com')
print(res.text)