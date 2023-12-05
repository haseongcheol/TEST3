import streamlit as st
import os
os.system('cls')

col1, col2 = st.columns([1, 2])
with col1:
    st.image('순심이.jpg')
with col2:
    '놓치면 후회할 인재 (신수인, 시급 3만원, 대박 쩔어~~)'
    '전화번호(📞) : 010-xxxx-xxxx'
    '이메일(📧) : gktjdcjf97@n  aver.com'
    '주소(🏠) : 충남 논사시 대학로 121'

''
'-----------------------'
col = st.columns(4)
with col[0]:
    st.link_button("Google(🌐)", "https://google.com")
with col[1]:
    st.link_button("Naver(✅)", "https://naver.com")
with col[2]:
    st.link_button("Daum(🇩)", "https://daum.net")
with col[3]:
    st.link_button("Facebook(ⓕ)", "https://facebook.com")

''
''
'## :orange[자기 소개]'
'#### 저는 시골에서 2남 1녀의 :red[가난한] 집의 장남으로 태어나...'


# import numpy as np
# # import pandas as pd

# os.system('cls')

# p = pd.Series
# li = [1, 2, 3, 4]
# n = np.array(li)
# p = pd.Series(li, index=['a', 'b', 'c', 'd'])
# li
# n
# p

# import streamlit as st
# st.write('Hello, **World!** :sunglasses:🤩🤑')
# 'Hello, World! :sunglasses:🤩🤑'
# '# Hello, World! color :blue :sunglasses:🤩🤑'

# import streamlit as st

# st.markdown("*Streamlit* is **really** ***cool***.")
# st.markdown('''
#     :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
#     :gray[pretty] :rainbow[colors].''')
# st.markdown("Here's a bouquet &mdash;\
#             :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

# multi = '''If you end a line with two spaces,
# a soft return is used for the next line.

# Two (or more) newline characters in a row will result in a hard return.
# '''
# st.markdown(multi)

# import streamlit as st
# import matplotlib.pyplot as plt
# import numpy as np
# fig, ax = plt.subplots()

# x = []
# y = []
# for i in range(-10, 11, 2):
#     x.append(i)
#     y.append(3*i*3 - 5*i**2 + 3*i - 7)

# col1, col2, col3 = st.columns(3)
# with col1 : 
#     cc = st.radio('선의 색을 선택하시오.', ['red', 'green', 'blue', 'orange'])
# with col2:
#     ma = st.radio('마커의 형태를 선택하시오.', ['o', '^', 's', 'p', 'h'])
# with col3:
#     ls = st.radio('선의 형태를 선택하시오.', ['-', '-.', ':', '--'])
# # plt.plot(x, y, '-go')
# plt.plot(x, y, color = cc, linestyle = ls, marker = ma)
# st.pyplot(fig)


# x = []
# y = []
# for i in range(-100, 101, 50):
#     x.append(i)
#     y.append(2*i**3 + 5*i**2 + 3*i + -7)

# col1, col2, col3 = st.columns(3)
# with col1:
#     color = st.radio('색을 선택하시오.', ('red', 'green', 'blue'))
# with col2:
#     linestyle = st.radio('선의 스타일을 선택하시오', ('-', '-.', ':'))
# with col3:
#     marker = st.radio('마커의 스타일을 선택하시오.', ('s', '^', 'o'))
# plt.plot(x,y, color = color, marker = marker, linestyle = linestyle)
# st.pyplot(fig)

# x = []
# for i in range(-100, 100):
#     x. append(i/10.0)

# col = st.columns(3)
# with col[0]:
#     a = st.number_input('Insert a', step = 1)
# with col[1]:
#     b = st.number_input('Insert b', step = 1)
# with col[2]:
#     c = st.number_input('Insert c', step = 1)

# y = []
# for i in x:
#     y.append(a*i**2 + b*i + c)
# plt.plot(x,y)
# st.pyplot(fig)  

# import sys
# sys.exit()

# list1 = list([['한빛', '남자', '20', '180'], ['한결', '남자', '21', '177'], ['김한결', '충성', '51', '155'], ['한라', '여자', '20', '160']])
# n = np.array(list1)
# col_names = ['이름', '성별', '나이', '키']
# df = pd.DataFrame(list1, columns=col_names, index=['1행', '2행', '3행', '4행'])
# df

# genre = st.radio("선택하시오", ["오름차순", "내림차순", "기타"], horizontal=True, index=2)

# number = st.number_input('Insert a number', value=20, step=1)
# st.write('The current number is ', number)
# df.iloc[3,2] = number  

# if '오름' in genre:
#     st.dataframe(df.sort_values(by=['키']))
# if '내림' in genre:
#     st.dataframe(df.sort_values(by=['키'],ascending=False))
# if '기타' in genre:
#     st.dataframe(df)
# if '요약' in genre:
#     st.dataframe(df.describe())


#     li[i] = li[i] + 3
# li 

# li = np. array([1, 2, 3, 4])
# li + 30

# li = np.array([7, 2, 5, 4])
# li
# li_sort = np.sort(li)[::-1]
# li_sort



# import turtle
# import turtle as t
# import random
# t = turtle.Turtle()
# t.shape('turtle')
# random.random()
# t.speed(0)
# t.pensize(3)
# t.penup()
# t.goto(-200, 0)
# t.pendown()

# def shape(n):
#     for i in range(n):
#         t.forward(1 + 5*i)
#         t.left(360/n)



# while True:
#     for i in range(30):
#         shape(7)
#         t.color(random.random(), random.random(), random.random())
#         t.goto(i*20, 0)
#     t.clear()
# turtle.done()






# t1.color('red')
# t1.penup()
# t1.goto(-100, 100)
# t1.pendown()
# t1.forward(100)
# t2 = turtle.Turtle()
# t2.shape('turtle')
# t2.width(5)
# t2.color('blue')
# t2.penup()
# t2.goto(-300, -100)
# t2.pendown()
# t2.forward(100)

# for i in range(30):
#     d1 = random.randint(1, 60)
#     t1. forward(d1)
#     d2 = random.randint(1, 60)
#     t2. forward(d2)




# a = np.arange(8)
# a

# a.shape = (4,2)
# a

# b = a.flatten()
# b

# b.resize((4,2))
# b

# os.system('cls')
# a = np.array([1, 10, -5, 2])
# print(np.abs(a))
# print(np.sqrt(a))
# print(np.square(a))
# print(a**0.5)
# print(np.square(a))
# print(a**2)

# --------------------------------------
# -중간고사 2번 문제-
# n = 7
# arr = np.full((n, n), '나머지')
# arr

# for i in range(n):
#     for j in range(n):
#         # arr[i,j] = '나머지'
#         if i == j or i + j == n-1:
#             arr[i, j] = '대'
#         # if i + j == n-1:
#         #     arr[i, j] = '대'
# arr
# -------------------------------------
# -중간고사 3번 문제-
# n = 100
# for i in range(1, n+1):
#     if i%7 == 3:
#         i
# ------------------------------------
# #-----------------------------------------------------------
# # #<10월 10일>
# list1 = [[1,2,3,4], [3,5,7,9]]
# # a = np.array(list1)
# # a

# # b = np.ones((10,5))
# # b
# # c = np.zeros((10,5))
# # c
# # d = np.full((10,5),3)
# # d
# e = np.eye(5)
# e


# e
# def user_eye(n):
#     arr = np.zeros((n,n))
#     for i in range(n):
#         for j in range(n):
#             if i ==n-j-1:
#                 arr[i,j]=1
#     return arr
# arr = user_eye(10)            
# arr


# list1= [[1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1]]
# n = np.array(list1)
# n

# def arry():
#     array = [[10]*5 for _ in range(4)]
#     for k in arry:
#         k
#     return k

# def user_eye(n):
#     arr = np.full((n,n))
#     for i in range(n):
#         for j in range(n):
#             if i ==  j:
#                 arr[i, j] = 1
#             else:
#                 st.write("나머지")
#         return arr

# arr = user_eye(10)
# arr



# def user_eye(n):
#     for i in range(n):
#         for j in range(n):
#             if i == j:
#                 st.write("대각선", end = " ")
#             else:
#                 st.write("나머지", end = " ")
#         st.write()

# n = user_eye(10)
# n



# for h in range(1,n+1):
#     if h%7 == 3 :
#         h

# s= 0
# # for i in range(2,1000+1,2):
# #     s=s+i
# # s

#-----------------------------------------------------------
# #<9월 26일>
#  list_1 = [1,2,7,4,50,33]
#  s=sum(list_1)
#  mx = max(list_1)
#  mn = min(list_1)
#  s,mx, mn

# def sta(arr):
#     s = 0
#     mx = -1e10
#     mn = 1e10
#     for i in arr: 
#         s = s +i
#         if mx<i:
#             mx=i
#         mx
#         if mn>i:
#             mn=i
#         mn
#     arr
#     'sum = ', s, 'min = ', mn, 'max = ', mx
#     return s, mx, mn
# list_1 =[5,13,7,4,11]
# [s1,mx1, mn1] = sta(list_1)
# s1, mx1, mn1

# import numpy as np
# list_1 = [1,2,3,4]

# a= np.array(list_1)
# a+10
#-----------------------------------------------------------

# #리스트 생성하기
# list_1 = [1,2,3,4,5,1,3]
# list_2 =[]
# list_1
# list_2
# len(list_1)

# #리스트 변경하기
# list_1[3] = 9999
# list_1
# list_1.append(100)
# list_1
# list_1.remove(9999)
# list_1
# list_1.insert(0,777)
# list_1

# list_2 = list_1.copy()
# list_2

# import turtle 
# t = turtle.Turtle()
# n=60
# t.shape('turtle')
# t.speed(0)
# t.write("HA", move=False, align="center", font=("arial",50,"bold"))

# t.penup()
# t.sety(-100)
# t.pendown()


# # for i in range(5):
# #     t. forward(100)
# #     t.left(144)
# turtle.done()





#딕셔너리 생성하기
# dict_1={'name' : '홍길동', 
#         'birth' : '1990', 
#         'addr' : '대한민국'}
# dict_1
# dict_1['addr']

# dict_1['weight'] = 60.5
# dict_1['family'] = ['아빠','엄마','여동생']
# dict_1

# dict_1.update({'weight' : 67.8, 'hobby' : ['게임','독서']})
# dict_1

# dict_1['hobby'] = ['축구','등산']
# dict_1

# del dict_1['weight']
# del dict_1['birth']
# del dict_1['addr']
# dict_1 


# for key in dict_1.keys():
#     key
# for v in dict_1.values():
#     v 
# for k, v in dict_1.items():
#     k
#     v




# print('파이썬의 세계에 오신 것을 환영합니다.')

# st. write('파이썬의 세계에 오신것을 환영합니다.')

# st.image('im.jpg')
# st.title('스트림릿...')
# a=2+3+8

#관계연산자

# a=5
# if a==5:
#     'right!'
#     'a is 5'

# if a==3:
#     'right'
#     'a is 3'
# if a !=3:
#     'right'
#     'a is not 3'

# grade = 51
# if grade >=90:
#     "a"
# elif grade >=80:
#     "b"
# elif grade >=70:
#     "c"
# elif grade >=60:
#     "d"
# elif grade >=50:
#     "f"

#for 반복문으로 구구단 출력

# for a in range(2,10):
#     a,'단 입니다'
#     for i in range(1,10):
#         b = str(a) + 'X' + str(i) +'='+str(i*a)
#         b 

