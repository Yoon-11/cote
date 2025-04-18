score = {
    'math':97,
    'eng':49,
    'kor': 50
}
print(score['math'])

score['sci'] = 100
print(score['sci'])

score['music'] = 99
print(score['music'])

print('music' in score)

if 'music' in score:
    print(score['music'])
else:
    score['music'] = 49
