# 리스트 자료형
# 리스트명 = [요소1. 요소2, 요소3, ...]

odd = [1,3,5,7,9]
print(odd)

# 여러가지 리스트
a = []
b = [1,2,3]
c = ['Life', 'is', 'too', 'short']
d = [1,2, 'Life', 'is']
e = [1,2, ['Life', 'is']]

print(a)
print(b)
print(c)
print(d)
print(e)

# 리스트의 인덱싱과 슬라이싱
# 리스트도 문자열처럼 인덱싱과 슬라이싱이 가능하다

# 리스트 인덱싱
a = [1,2,3]
print(a)

# a[0]은 리스트 a의 첫번째 요소 값을 말한다
print(a[0])
print(a[0] + a[2]) # 1+3

# 파이썬은 숫자를 0부터 세기때문에 a[1]이 리스트 a의 첫번째 요소가 아니라
# a[0]이 리스트 a의 첫번째 요소임을 명심하자.
# a[-1]은 문자열에서와 마찬가지로 리스트 a의 마지막 요소값을 말한다.
print(a[-1])

# 리스트 a 안에 숫자 1,2,3 과 또 다른 리스트인 ['a','b','c']를 포함시켜보자.
a = [1,2,3,['a','b','c']]

print(a)
print(a[0])
print(a[-1])
print(a[3])

# 리스트 a에 포함된 ['a','b','c']라는 리스트에서 'a'라는 값을 인덱싱을
# 이용하여 끄집어내기
a[-1][0]
print(a[-1][0])
print(a[-1][1])
print(a[-1][2])