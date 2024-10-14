# 📌 Assignment 4-2

## 1. 제목

ChatGPT를 활용한 자료구조 선택과 최적화

## 2. 이름

김가영(Sophia)

## 3. 제출일

24.10.14 (월)

## 4. 과제 목표

> 스스로 생각하는 과제의 목표를 작성해 주세요.

자료구조를 더 유용하게 활용하기 위함이라 생각합니다. 

## 5. ChatGPT 활용

### 👉 질문 내용

> ChatGPT에게 했던 질문을 기록합니다. (예. 여러 과목을 담당하는 선생님을 효율적으로 관리하기 위한 자료구조는 무엇이 좋을까요?)

여기에 작성해 주세요.

### 👉 ChatGPT 답변 요약

> ChatGPT가 제공한 답변을 간단히 요약합니다. (예. 딕셔너리가 적합하며, 각 과목을 키로 하고 선생님들의 목록을 값으로 사용하는 방법이 좋다고 조언을 받았습니다.)

여기에 작성해 주세요.

## 6. 자료구조 선택 이유

> ChatGPT의 조언을 기반으로 선택한 자료구조와 그 이유를 서술합니다.

딕셔너리는 학생 이름을 키로 저장하며, 이름에 대응하는 성적을 값으로 정하기 때문입니다. 그러므로 성적을 조회 혹은 수정할 때 빠르게 
접근 할 수 있습니다. 

## 7. 코드 작성 과정

> 코드를 작성하는 과정을 적습니다.

students = {}

def add_student(name, score):
    students[name] = score

def display_students():
    if students:
        print("학생 목록과 성적:")
        for name, score in students.items():
            print(f"{name}: {score}")
    else:
        print("등록된 학생이 없습니다.")

def remove_student(name):
    if name in students:
        del students[name]
        print(f"{name} 학생의 정보가 삭제되었습니다.")
    else:
        print(f"{name} 학생은 등록되지 않았습니다.")

def update_student(name, score):
    if name in students:
        students[name] = score
        print(f"{name} 학생의 성적이 {score}로 업데이트되었습니다.")
    else:
        print(f"{name} 학생은 등록되지 않았습니다.")

while True:
    print("\n=== 학생 관리 프로그램 ===")
    print("1. 학생 추가")
    print("2. 학생 목록 보기")
    print("3. 학생 삭제")
    print("4. 학생 성적 수정")
    print("5. 종료")

    choice = input("원하는 작업을 선택하세요 (1-5): ")

    if choice == '1':
        name = input("학생 이름을 입력하세요: ")
        score = input("학생 성적을 입력하세요: ")
        add_student(name, score)
    elif choice == '2':
        display_students()
    elif choice == '3':
        name = input("삭제할 학생의 이름을 입력하세요: ")
        remove_student(name)
    elif choice == '4':
        name = input("성적을 수정할 학생의 이름을 입력하세요: ")
        score = input(f"{name} 학생의 새로운 성적을 입력하세요: ")
        update_student(name, score)
    elif choice == '5':
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 선택입니다. 다시 시도하세요.")


## 8. 코드 실행 결과

> 프로그램 실행 결과를 캡쳐 이미지로 첨부합니다.

=== 학생 관리 프로그램 ===
1. 학생 추가
2. 학생 목록 보기
3. 학생 삭제
4. 학생 성적 수정
4. 학생 성적 수정
4. 학생 성적 수정
4. 학생 성적 수정
4. 학생 성적 수정
4. 학생 성적 수정
4. 학생 성적 수정
5. 종료
원하는 작업을 선택하세요 (1-5): 1
학생 이름을 입력하세요: 김가영
학생 성적을 입력하세요: 99


## 9. 문제 해결 과정 및 배운점

> ChatGPT와의 상호작용을 통해 얻은 인사이트와 프로그램을 개선하는 과정에서 배운 내용을 정리합니다.

딕셔너리를 적재적소에 활용하는 법을 배우기 위함입니다. 