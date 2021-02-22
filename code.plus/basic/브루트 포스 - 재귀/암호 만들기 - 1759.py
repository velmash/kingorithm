def check(password):
    ja, mo = 0, 0
    for a in password:
        if a in 'aeiou':
            mo += 1
        else:
            ja += 1

    if ja >= 2 and mo >= 1:
        return True
    else:
        return False


def go(n, alpha, password, index):
    if len(password) == n:
        if check(password):
            print(password)
        return
    if index == len(alpha):
        return
    go(n, alpha, password + alpha[index], index + 1)  # 알파벳 사용하는 경우
    go(n, alpha, password, index + 1)  # 알파벳 사용하지 않는 경


l, c = map(int, input().split())
alphabet = input().split()
alphabet.sort()

print(go(l, alphabet, "", 0))
