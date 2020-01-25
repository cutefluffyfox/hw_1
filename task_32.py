#!/usr/bin/python3

from pyrob.api import *


def fill():
    global count
    while not wall_is_above():
        move_up()
        if not cell_is_filled():
            fill_cell()
        else:
            count += 1
    while not wall_is_beneath():
        move_down()


@task(delay=0.02)
def task_8_18():
    global count
    count = 0
    while wall_is_beneath():
        if wall_is_above():
            fill_cell()
        fill()
        move_right()
    mov("ax", count)


if __name__ == '__main__':
    run_tasks()
