#!/usr/bin/python3

from pyrob.api import *


def fill():
    move_right()
    fill_cell()
    move_down()
    fill_cell()
    move_right()
    fill_cell()
    move_left()
    move_down()
    fill_cell()
    move_up()
    move_left()
    fill_cell()
    move_up()


def check_move() -> bool:
    ans = 0
    while not wall_is_on_the_right() and ans < 3:
        move_right()
        ans += 1
    for _ in range(ans):
        move_left()
    return ans == 3


@task
def task_2_2():
    move_down()
    if check_move():
        fill()
    while check_move():
        for _ in range(4):
            move_right()
        fill()


if __name__ == '__main__':
    run_tasks()
