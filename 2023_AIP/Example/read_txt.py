infile = open('textfile.txt', 'r')

for s in infile:
    # print(s, end='')
    print(s.rstrip())

infile.close()

# ldconfig
# 파일이 안읽어짐  - 수정필요 