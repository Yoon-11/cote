# 키워드 : capitalize() -> 첫문자 대문자로 만듦
def solution(s):
    words = s.split(" ")
    capitalized_words = []
    for word in words:
        capitalized_words.append(word.capitalize())
    return " ".join(capitalized_words)

print(solution("for the last week"))
print(solution("3people unFollowed me"))


# title() 함수를 이용하면 첫문자를 간단하게 대문자로 만들 수 있지만,
# 내부적으로 알파벳이 아닌 문자를 기준으로 단어 경계를 처리가 하기 때문에 "3people" → "3People" 로 바뀜
def solution2(s):
    return s.title()

print(solution2("for the last week"))
print(solution2("3people unFollowed me"))

