# import sys
# sys.setrecursionlimit(5000)

def is_prime(n, d = 2):
    if n > d:
        if not n % d:
            return False
        else:
          return is_prime(n, d + 1) if d < 20 else True
    return True

print(is_prime(1999))
