# 📌 HW Week4 - POST 요청하기

## 1. 제목

Requests 모듈을 활용하여 POST 요청하기

## 2. 이름

> 김가영 (Sophia)


## 3. 제출일

> 24.09.25 (수) 


## 4. 과제 목표

> Requests 모듈을 활용하여 POST를 요청하는 것에 조금 더 익숙해지기 위한 것이라 생각합니다.

## 5. 코드 실행 결과

> 실행한 코드 : 
import requests

data = {"title": "Home", "body": "I love my bed", "userId": 2}
response = requests.post("https://jsonplaceholder.typicode.com/posts",data=data)

print("Status Code", response.status_code)

print("Response Body:", response.text)

실행한 코드의 결과 : 
Status Code 201
Response Body: {
  "title": "Home",
  "body": "I love my bed",
  "userId": "2",
  "id": 101
}

## 6. 문제 해결 과정 및 배운점

> 프로그램 작성 중 별다른 문제는 없었으나 다른 사이트도 해보고싶어 링크를 바꿔보았지만 달라지는게 없었습니다. 지피티한테 물어보니 jsonplaceholder이라는 사이트는
api 요청을 보내면 서버가 데이터를 받아 받은 데이터를 기반으로 json으로 응답하는데에 반해 타 사이트는 단순히 html, css, javascript 파일을 다운로드하여 
웹페이지를 렌더링해 시각적인 정보를 주는 역할을 하여 데이터를 주고받는 형식이 되지 않는다는 답변을 받았습니다. 따라서 과제를 하면서 jsonplaceholder 같은
api 요청을 서버가 받아 json으로 응답하는 것이 아닌 기타 언어를 사용하는 사이트는 post를 요청하여도 결과가 달라지지 않는다 는 것을 배웠습니다.