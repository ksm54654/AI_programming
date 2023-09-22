r = float(input('Enter coefficient of restitution : '))
h = float(input('Enter initial height in meters : '))

# 공이 튕긴 전체 거리의 합
total = h
cnt = 1

while (h * r) > 0.1:
    cnt += 1            # 튕긴 횟수 1 증가
    h *= r              # 튀어오를 높이
    total += h * 2.0    # 올라갔다 내려옴
    
print(f"Number of bounces : {cnt}")
print("Meters traveled : {:.2f}".format(total))