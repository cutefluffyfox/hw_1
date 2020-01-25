#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_7():
    count = int(cell_is_filled())
    while not wall_is_on_the_right() and count < 3:
        move_right()
        count = count + 1 if cell_is_filled() else 0


if __name__ == '__main__':
    run_tasks()
