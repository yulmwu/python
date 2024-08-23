import os
import random

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()

def display_staff_line(line_index, line_width, show_note=False):
    staff_lines = [
        ['', 0, '솔'],
        ['|' + '-' * 65, 1, '파'],
        ['|' + '', 0, '미'],
        ['|' + '-' * 65, 1, '레'],
        ['|' + '', 0, '도'],
        ['|' + '-' * 65, 1, '시'],
        ['|' + '', 0, '라'],
        ['|' + '-' * 65, 1, '솔'],
        ['|' + '', 0, '파'],
        ['|' + '-' * 65, 1, '미'],
        ['', 0, '레'],
    ]

    line_type = staff_lines[line_index][1]
    note = staff_lines[line_index][2]

    prefix = '|'
    if line_index == 0 or line_index == 10:
        prefix = ''

    if line_type == 0:
        staff_lines[line_index][0] = prefix + ' ' * line_width + 'O'
    else:
        staff_lines[line_index][0] = prefix + '-' * line_width + 'O' + '-' * (64 - line_width)

    def format_line(line):
        note = ''
        if show_note:
            note = line[2]
        formatted_line = line[0] + ' ' * 3 + note
        if line[1] == 0:
            formatted_line = line[0] + (' ' * (66 - len(line[0]))) + ' ' + note
        return formatted_line

    print('\n'.join(map(format_line, staff_lines)))

    return note

def practice_round():
    line_index = random.randint(0, 9)
    line_width = random.randint(1, 65)

    correct_note = display_staff_line(line_index, line_width)

    user_input = input('>> ')

    clear_screen()

    display_staff_line(line_index, line_width, True)

    if user_input == correct_note:
        print('정답입니다.')
    else:
        print(f'틀렸습니다. 정답은 \'{correct_note}\' 이였습니다.')

    input('\'엔터\' 키를 눌러 다음으로 넘어가거나 \'Ctrl + C\'로 종료하세요.')

while True:
    practice_round()
    clear_screen()
