heights = {'taro':168, 'jiro':171, 'takeshi':165}

total = 0

for i in heights.values():
    total += 1

average = total / len(heights)

print('平均身長は {0}cm です。'.format(average))