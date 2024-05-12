import timeit
from hashlib import sha256

# Алгоритм Боєра-Мура
def boyer_moore_search(text, pattern):
    m, n = len(pattern), len(text)
    if m > n:
        return -1

    skip = {}
    for i in range(m):
        skip[pattern[i]] = m - i - 1

    i = m - 1  # Індекс в основному тексті
    while i < n:
        j = m - 1  # Індекс в патерні
        while j >= 0 and text[i] == pattern[j]:
            i -= 1
            j -= 1
        if j == -1:
            return i + 1
        i += max(skip.get(text[i], m), 1)

    return -1

# Алгоритм Кнута-Морріса-Пратта
def kmp_search(text, pattern):
    m, n = len(pattern), len(text)
    lps = [0] * m
    j = 0

    # Побудова lps масиву
    compute_lps_array(pattern, m, lps)

    i = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            return i - j

        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1

def compute_lps_array(pattern, m, lps):
    length = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

# Алгоритм Рабіна-Карпа
def rabin_karp_search(text, pattern, d=256, q=101):
    m, n = len(pattern), len(text)
    h = pow(d, m-1) % q
    p = 0
    t = 0
    result = []

    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for i in range(n - m + 1):
        if p == t:
            if text[i:i+m] == pattern:
                return i
        if i < n-m:
            t = (t - h * ord(text[i])) % q
            t = (t * d + ord(text[i + m])) % q
            t = (t + q) % q

    return -1

global text, pattern

def measure_time(func, text, pattern):
    setup_code = f"from __main__ import {func.__name__}, text, pattern"
    stmt = f"{func.__name__}(text, pattern)"
    times = timeit.repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)
    return min(times)

# Зчитування файлів та ініціалізація даних
with open('/Users/lesyakatanova/Documents/Навчання/GOIT/ДЗ_5_Катанова/goit-algo-hw-05/file01.txt', 'r', encoding='windows-1252') as file:
    text1 = file.read()

with open('/Users/lesyakatanova/Documents/Навчання/GOIT/ДЗ_5_Катанова/goit-algo-hw-05/file02.txt', 'r', encoding='windows-1252') as file:
    text2 = file.read()

patterns = ['existing_substring', 'nonexistent_substring']

for pattern in patterns:
    print(f"Testing pattern: {pattern}")
    for text in [text1, text2]:
        print(f"Text length: {len(text)}")
        print(f"Boyer-Moore: {measure_time(boyer_moore_search, text, pattern)} seconds")
        print(f"KMP: {measure_time(kmp_search, text, pattern)} seconds")
        print(f"Rabin-Karp: {measure_time(rabin_karp_search, text, pattern)} seconds")
