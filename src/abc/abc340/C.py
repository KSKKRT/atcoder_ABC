st = [int(input())]
cost = 0
while len(st) > 0:
    n = st.pop()
    if n % 2 == 0 and n != 2:
        st.append(n // 2)
        st.append(n // 2)
    elif n % 2 == 1 and n != 3:
        m = int(n // 2)
        st.append(m)
        st.append(m + 1)
    elif n == 3:
        st.append(2)
    cost += n
print(cost)
