# 삐-익
# 패턴이 무조건 한문자 * 한문자인줄~!
N = int(input())

pattern = list(map(str, input().split("*")))

str_list = []
for _ in range(N):
    str_list.append(input())

for s in str_list:
    if ((len(s) >= len(pattern[0])+len(pattern[1])) and s.startswith(pattern[0]) and s.endswith(pattern[1])) : print("DA")
    else: print("NE")


N = int(input())

left_code, right_code = input().split("*")

for _ in range(N):
    string = input()

    if len(string) < len(left_code) + len(right_code):
        print("NE")
    elif string.startswith(left_code) and string.endswith(right_code) :
        print("DA")
    else:
        print("NE")







