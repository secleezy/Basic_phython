import turtle

def drawBar(height):
    t.begin_fill() # 배경색 채우기 시작
    t.left(90) #왼쪽으로 90도 회전
    t.forward(height) #height만큼 직진
    t.write(str(height), font = ('Times New Roman', 16, 'bold')) #글씨 출력
    t.right(90) # 오른쪽으로 90도 회전
    t.forward(40) # 40만큼 직진
    t.right(90) # 오른쪽으로 90도 회전
    
    t.forward(height) #height만큼 직진
    t.left(90 ) #왼쪽으로 90도 회전
    t.end_fill() #배경색 채우기 끝
    
data = [120, 56, 309, 220, 156, 23, 98] #막대그래프 수치

t = turtle.Turtle()
t.color("blue") #막대그래프 선 색
t.fillcolor("red") #막대그래프 배경색

t.pensize(3) #막대그래프 선 굵기

for d in data: #data배열에 있는 데이터로 함수 호출
    drawBar(d) #d(배열 속 데이터)는 즉 막대그래프의 height가 된다.

turtle.mainloop() #turtle 호출
turtle.bye() #turtle 호출 종류