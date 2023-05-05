from sys import stdin
import math

N, s_atk = map(int, stdin.readline().split())
rooms = [list(map(int, stdin.readline().split())) for _ in range(N)]


def can_save(s_hp):
    cur_atk = s_atk
    cur_s_hp = s_hp
    for flag, atk, hp in rooms:
        if flag == 1:
            s_tmp = math.ceil(hp / cur_atk)
            cur_s_hp -= (s_tmp - 1) * atk
            if cur_s_hp <= 0:
                return False
        else:
            cur_atk += atk
            cur_s_hp = min(s_hp, cur_s_hp + hp)
    return True


def solution():
    start = 1
    end = 1
    while not can_save(end):
        end *= 2

    while start <= end:
        mid = (start + end) // 2
        if can_save(mid):
            end = mid - 1
        else:
            start = mid + 1

    print(start)


solution()
