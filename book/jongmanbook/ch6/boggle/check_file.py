file1 = open('boggle.out', 'r')
file2 = open('boggle.res', 'r')

fl1 = file1.readlines()
fl2 = file2.readlines()

print(fl1)
print(fl2)
print(len(fl1))
print(len(fl2))

if len(fl1) == len(fl2):
    for line in zip(fl1, fl2):
        if line[0] != line[1]:
            print('NO')


