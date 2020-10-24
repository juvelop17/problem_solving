import time

prev_time = time.time_ns()


def solution(new_id):
    answer = ''

    new_id = new_id.lower()
    # print(new_id)

    new_id2 = ''
    char_set = [i for i in range(ord('a'),ord('z')+1)] + \
               [i for i in range(ord('0'),ord('9')+1)] + \
               [ord('-'),ord('_'),ord('.')]
    for ch in new_id:
        if ord(ch) in char_set:
            new_id2 += ch
    # print(new_id2)

    new_id3 = ''
    # for i in range(len(new_id2)):
    #
    #     if i+1 < len(new_id2) and (new_id2[i] == '.' and new_id2[i+1] == '.'):
    #         continue
    #     new_id3 += new_id2[i]

    temp_id = new_id2[1:] + '\r'
    for a, b in zip(new_id2, temp_id):
        if a == '.' and a == b:
            continue
        new_id3 += a
    # print('3단계', new_id3)

    # 4단계
    if len(new_id3) > 0 and new_id3[0] == '.':
        new_id3 = new_id3[1:]
    if len(new_id3) > 0 and new_id3[-1] == '.':
        new_id3 = new_id3[0:-1]
    # print('4단계', new_id3)

    # 5단계
    if new_id3 == '':
        new_id3 += 'a'
    # print('5단계', new_id3)

    # 6단계
    if len(new_id3) >= 16:
        new_id3 = new_id3[:15]
    if len(new_id3) > 0 and new_id3[0] == '.':
        new_id3 = new_id3[1:]
    if len(new_id3) > 0 and new_id3[-1] == '.':
        new_id3 = new_id3[0:-1]
    # print('6단계', new_id3)

    # 7단계
    while len(new_id3) <= 2:
        new_id3 += new_id3[-1]
    # print('7단계', new_id3)

    answer = new_id3

    return answer

# new_id = "...!@BaT#*..y.abcdefghijklms..."
# new_id = "z-+.^."
# new_id = "=.="
# new_id = "123_.def"
new_id = "abcdefghijklmn.p"
print(solution(new_id))


print('time', time.time_ns()-prev_time)



