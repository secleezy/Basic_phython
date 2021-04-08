print("\n011 변수 사용하기")
samsung = 50000
samsung = samsung * 10
print("평가 금액 :",samsung)

print("\n012 변수 사용하기")
시가총액 = 298000000000000
현재가 = 50000
PER = 15.79
print("시가총액",int(시가총액/1000000000000),"조")
print("현재가",현재가)
print("PER",PER)

print("\n013 문자열 출력")
s="hello"
t="python"
print(s+"!",t)

print("\n014 파이썬을 이용한 값 계산")
print(2+2*3)

print("\n015 type 함수")
a=132
print(type(a))
print("int 형식입니다.")

print("\n016 문자열을 정수로 변환")
num_str=720
num_str=int(num_str)
print("num_str의 형식 :",type(num_str))

print("\n017 정수를 문자열 100으로 변환")
num=100
num=str(num)
print("num의 형식 :",type(num))

print("\n018 문자열을 실수로 변환")
num_str_float="15.79"
num_str_float=float(num_str_float)
print("num_str_float의 형식 :",type(num_str_float))

print("\n019 문자열을 정수로 변환")
year="2020"
year=int(year)
print(year-1,year,year+1)

print("\n020 파이썬 계산")
air_conditioner=48584*36
print("총 금액 :",air_conditioner)

print("\n101 파이썬에서 True 혹은 False를 갖는 데이터 타입은 무엇인가?")
print("bool(boolean) 입니다.")

print("\n102 아래 코드의 출력 결과를 예상하라")
print(3==5)

print("\n103 아래 코드의 출력 결과를 예상하라")
print(3<5)

print("\n104 아래 코드의 결과를 예상하라")
x=4
print(1<x<5)

print("\n105 아래 코드의 결과를 예상하라")
print((3==3) and(4!=3))

print("\n106 아래 코드에서 에러가 발생하는 원인에 대해 설명하라. [누락]")

print("\n107 아래 코드의 출력 결과를 예상하라")
if 4<3:
    print("Hello World")

print("\n108 아래 코드의 출력 결과를 예상하라")
if 4<3:
    print("Hello World.")
else:
    print("Hi, there.")
    
print("\n109 아래 코드의 출력 결과를 예상하라")
if True :
    print ("1")
    print ("2")
else :
    print("3")
print("4")
    
print("\n110 아래 코드의 출력 결과를 예상하라")
if True :
    if False:
        print("1")
        print("2")
    else:
        print("3")
else :
    print("4")
    print("5")
    
print('\n111 사용자로부터 입력받은 문자열을 두 번 출력하라. 아래는 사용자가 "안녕하세요"를 입력한 경우의 출력 결과이다.')
user_str=input("")
print(user_str,user_str)

print('\n112 사용자로부터 하나의 숫자를 입력받고, 입력 받은 숫자에 10을 더해 출력하라.')
num=input('')
num=int(num)
print(num+10)

print('\n113 사용자로부터 하나의 숫자를 입력 받고 짝수 홀수를 판별하라.')
num=input('')
num=int(num)
if num%2==1:
    print("홀수")
else:
    print("짝수")

print('\n114 사용자로부터 값을 입력받은 후 해당 값에 20을 더한 값을 출력하라 단 사용자가 입력한 값과 20을 더한 계산 값이 255를 초과하는 경우 255를 출력해야 한다.')
num=input('')
num=int(num)
if num+20>255:
    print(255)
else:
    print(num+20)

print('\n115 사용자로부터 하나의 값을 입력받은 후 해당 값에 20을 뺀 값을 출력하라. 단 출력 값의 범위는 0`255이다. 예를 들어 결괏값이 0보다 작은 값이 되는 경우 0을 출력하고 255보다 큰 값이 되는 경우 255을 출력해야 한다.')
num=input('')
num=int(num)
if num-20<0:
    print(0)
elif num-20>255:
    print(255)
else:
    print(num-20)

print('\n116 사용자로부터 입력 받은 시간이 정각인지 판별하라.')
num=input("현재시간 : ")
if num[-2:] == "00":
    print("정각 입니다.")
else:
    print("정각이 아닙니다.")


print('\n117 사용자로 입력받은 단어가 아래 fruit 리스트에 포함되어 있는지를 확인하라 포함되었다면 "정답입니다"를 아닐 경우 "오답입니다" 출력하라.')
fruit=["사과","포도","홍시"]
num=input("좋아하는 과일은? ")
if num in fruit:
    print("정답입니다.")
else:
    print("오답입니다.")

print('\n118 투자 경고 종목 리스트가 있을 때 사용자로부터 종목명을 입력 받은 후 해당 종목이 투자 경고 종목이라면 "투자 경고 종목입니다"를 아니면 "투자 경고 종목이 아닙니다"를 출력하는 프로그램을 작성하라.')
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
num = input("종목명: ")
if num in warn_investment_list:
    print("투자 경고 종목입니다.")
else:
    print("투자 경고 종목이 아닙니다.")


print('\n119 아래와 같이 fruit 딕셔너리가 정의되어 있다. 사용자가 입력한 값이 딕셔너리 키 (key) 값에 포함되었다면 "정답입니다"를 아닐 경우 "오답입니다" 출력하라.')
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
num = input("제가좋아하는계절은: ")
if num in fruit:
    print("정답입니다.")
else:
    print("오답입니다.")

print('\n120 아래와 같이 fruit 딕셔너리가 정의되어 있다. 사용자가 입력한 값이 딕셔너리 값 (value)에 포함되었다면 "정답입니다"를 아닐 경우 "오답입니다" 출력하라.')
fruit={"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
num=input("좋아하는과일은? ")
if num in fruit.values():
    print("정답입니다.")
else:
    print("오답입니다.")

print('\n121 사용자로부터 문자 한 개를 입력 받고 소문자일 경우 대문자로, 대문자일 경우 소문자로 변경해서 출력하라.')
num=input("")
if num.islower():
    print(num.upper())
else:
    print(num.lower())

print('\n122 점수 구간에 해당하는 학점이 아래와 같이 정의되어 있다. 사용자로부터 score를 입력받아 학점을 출력하라.')
num=input("score: ")
num=int(num)
if 81 <= num <= 100:
    print("grade is A")
elif 61 <= num <= 80:
    print("grade is B")
elif 41 <= num <= 60:
    print("grade is C")
elif 21 <= num <= 40:
    print("grade is D")
else:
    print("grade is E")



print('\n123 사용자로부터 달러, 엔, 유로 또는 위안 금액을 입력받은 후 이를 원으로 변환하는 프로그램을 작성하라. 각 통화별 환율은 다음과 같다. 사용자는 100 달러, 1000 엔, 13 유로, 100 위안과 같이 금액과 통화명 사이에 공백을 넣어 입력한다고 가정한다.')
dal = {"달러": 1167, "엔": 1.096, "유로": 1268, "위안": 171}
num = input("입력: ")
num, dol = num.split()
print(float(num) * dal[dol], "원")


print('\n124 사용자로부터 세 개의 숫자를 입력 받은 후 가장 큰 숫자를 출력하라.')
num1 = input("input number1: ")
num2 = input("input number2: ")
num3 = input("input number3: ")
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

if num1 > num2 and num1 > num3:
    print(num1)
elif num2 > num1 and num2 > num3:
    print(num2)
else:
    print(num3)

print('\n125 휴대폰 번호 앞자리에 따라 통신사는 아래와 같이 구분된다. 사용자로부터 휴대전화 번호를 입력 받고, 통신사를 출력하는 프로그램을 작성하라.')
num = input("휴대전화 번호 입력: ")
if num[0:3] == "011":
    print("당신은 SKT 사용자입니다.")
elif num[0:3] =="016":
    print("당신은 KT 사용자입니다.")
elif num[0:3] =="019":
    print("당신은 LGU 사용자입니다.")
else:
    print("당신은 알수없는 사용자입니다.")


print('\n126 우편번호는 5자리로 구성되는데, 앞의 세자리는 구를 나타낸다. 예를들어, 강북구의 경우 010, 011, 012 세 자리로 시작한다.')
num = input("우편번호: ")
if num[0:2] in ["010", "011", "012"]:
    print("강북구")
elif num[0:2] in ["014", "015", "016"]:
    print("도봉구")
else:
    print("노원구")


print('\n127 주민등록번호 뒷 자리 7자리 중 첫째 자리는 성별을 나타내는데, 1, 3은 남자 2, 4는 여자를 의미한다. 사용자로부터 13자리의 주민등록번호를 입력 받은 후 성별 (남자, 여자)를 출력하는 프로그램을 작성하라.')
num = input("주민등록번호: ")
if num[7] == "1" or num[7] == "3":
    print("남자")
else:
    print("여자")


print('\n128 주민등록번호의 뒷 자리 7자리 중 두번째와 세번째는 지역코드를 의미한다. 주민 등록 번호를 입력 받은 후 출생지가 서울인지 아닌지 판단하는 코드를 작성하라')
num = input("주민등록번호: ")
if 0 <= int(num[8:10]) <= 8:
    print("서울입니다.")
else:
    print("서울이 아닙니다.")


print('\n129 주민등록번호는 13자리로 구성되는데 마지막 자리수는 주민등록번호의 유효성을 체크하는데 사용된다. 먼저 앞에서부터 12자리의 숫자에 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5를 차례로 곱한 뒤 그 값을 전부 더한다. 연산 결과 값을 11로 나누면 나머지가 나오는데 11에서 나머지를 뺀 값이 주민등록번호의 마지막 번호가 된다.')
num = input("주민등록번호: ")
sub = int(num[0]) * 2 + int(num[1]) * 3 + int(num[2]) * 4 + int(num[3]) * 5 + int(num[4]) * 6 + int(num[5]) * 7 + int(num[7]) * 8 + int(num[8]) * 9 + int(num[9]) * 2 + int(num[10])* 3 + int(num[11])* 4 + int(num[12]) * 5
sub= sub%11
sub=11-sub

if int(num[13:14]) == sub:
    print("유효한 주민등록번호입니다.")
else:
    print("유효하지 않은 주민등록번호입니다.")


print('\n130 아래 코드는 비트코인의 가격 정보를 딕셔너리로 가져오는 코드이다.')
import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

if (float(btc['opening_price'])+(float(btc['max_price']) - float(btc['min_price']))) > float(btc['max_price']):
    print("상승장")
else:
    print("하락장")