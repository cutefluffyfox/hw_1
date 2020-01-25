#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
    goal = 0
    now = 0
    move_right()
    fill_cell()
    while not wall_is_on_the_right():
        if now > goal:
            fill_cell()
            now = 0
            goal += 1
        now += 1
        move_right()


if __name__ == '__main__':
    run_tasks()
