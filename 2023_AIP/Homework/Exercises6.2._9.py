import random
import string
 
# 알파벳 3개를 랜덤으로 

alphabet = 'abcdefghijklmnopqrstuvwxyz'

select_alp = random.sample(alphabet, 3)

print(select_alp)

# string 이용

alphabet_s = string.ascii_lowercase

select_s = random.sample(alphabet_s, 3)
select_c = random.choices(alphabet_s, k = 3) # 중복 허용해서 뽑기 

select_chr = [chr(random.randint(ord('A'), ord('Z'))) for _ in range(3)] # for문에서 안쓰면 _해도 ㄱㅊ 

print(select_s)
print(select_c)
print(select_chr)