m = int(input())
if m < 100:
    print("00")
elif 100 <= m < 1000:
    print(f"0{int(m/100)}")
elif 1000 <= m <= 5000:
    print(int(m/100))
elif 6000 <= m <= 30000:
    print(int(m/1000)+50)
elif 35000 <= m <= 70000:
    print(int((m/1000-30)/5)+80)
else:
    print(89)