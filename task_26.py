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


def check_move_right() -> bool:
    ans = 0
    while not wall_is_on_the_right() and ans < 3:
        move_right()
        ans += 1
    for _ in range(ans):
        move_left()
    return ans == 3


def check_move_down() -> bool:
    ans = 0
    while not wall_is_beneath() and ans < 3:
        move_down()
        ans += 1
    for _ in range(ans):
        move_up()
    return ans == 3


@task(delay=0.02)
def task_2_4():
    while check_move_down():
        fill()
        while check_move_right():
            for _ in range(4):
                move_right()
            fill()
        for _ in range(4):
            move_down()
        while not wall_is_on_the_left():
            move_left()
    fill()
    while check_move_right():
        for _ in range(4):
            move_right()
        fill()
    while not wall_is_on_the_left():
        move_left()


if __name__ == '__main__':
    run_tasks()
