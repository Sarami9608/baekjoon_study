# 230315

# 팰린드롬인지 확인하기
# 알파벳 소문자로만 이루어진 단어가 주어진다.
# 이때, 이 단어가 팰린드롬인지 아닌지 확인하는 프로그램을 작성하시오.
# 팰린드롬이란 앞으로 읽을 때와 거꾸로 읽을 때 똑같은 단어를 말한다.
# level, noon은 팰린드롬이고, baekjoon, online, judge는 팰린드롬이 아니다.

strings = input()
strings_re = ""
for i in range(len(strings)-1, -1, -1):
    strings_re += strings[i]
if strings == strings_re:
    print(1)
else:
    print(0)
