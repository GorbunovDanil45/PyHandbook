prev_h: int = 0
bad: int = -1

for index in range(int(input())):
    block: int = int(input())

    h_n = block % 256
    r_n = (block // 256) % 256
    m_n = block // 256 ** 2

    if h_n >= 100:
        bad = index
        break

    expected_h = (37 * (m_n + r_n + prev_h)) % 256

    if h_n != expected_h:
        bad = index
        break
    prev_h = h_n

print(bad)
