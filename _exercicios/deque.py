from collections import deque

valores = deque(maxlen=10)
valores.append(1)
valores.append(2)
valores.append(3)
valores.appendleft(4)
valores.reverse()
valores.extend([5, 6])
valores.popleft()

print(valores)
valores.rotate(1)
print(valores)

