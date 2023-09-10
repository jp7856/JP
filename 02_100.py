
        
def grader(n1,s1) :
    if s1 >= 95 :
        print('학생이름 :', n1)
        print('점수 :', s1)
        print('학점 : A+')

    elif s1 >= 90 :
        print('학생이름 :', n1)
        print('점수 :', s1)
        print('학점 : A')
    
    elif s1 >= 85 :
        print('학생이름 :', n1)
        print('점수 :', s1)
        print('학점 : B+')
    
    elif s1 >= 80 :
        print('학생이름 :', n1)
        print('점수 :', s1)
        print('학점 : B')
    
    elif s1 >= 75 :
        print('학생이름 :', n1)
        print('점수 :', s1)
        print('학점 : C+')
    
    elif s1 >= 70 :
        print('학생이름 :', n1)
        print('점수 :', s1)
        print('학점 : C')
    
    elif s1 >= 65 :
        print('학생이름 :', n1)
        print('점수 :', s1)
        print('학점 : D+')
    
    elif s1 >= 60 :
        print('학생이름 :', n1)
        print('점수 :', s1)
        print('학점 : D')                

    else: 
        print('학생이름 :', n1)
        print('점수 :', s1)
        print('학점 : F')     


name = input("이름을 입력하세요 :")
score = int(input("점수를 입력하세요 : "))

grader(name,score)
         


# # 이름과 점수 입력
# grader("이호창", 99)

# # 출력
# 학생이름 : 이호창
# 점수 : 99점
# 학점 : A+