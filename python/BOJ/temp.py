
new_li = [2,2,4,4,8,4,8,8]
add_li = []

new_li += [0]
idx = 0
while idx + 1 < len(new_li):
    if new_li[idx] == new_li[idx +1]:
        add_li.append(new_li[idx] * 2)
        idx += 2
    else:
        add_li.append(new_li[idx])
        idx += 1

print(add_li)

