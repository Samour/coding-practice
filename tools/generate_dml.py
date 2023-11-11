#!/usr/bin/env python3

from faker import Faker
import random


ROW_SPECS = {
    'teacher': 5,
    'student': 50,
    'class': 15,
    'students_per_class': 30,
}


class_types = [
    'Maths',
    'Science',
    'English',
    'Geography',
    'History',
]

class_letters = ['A', 'B', 'C']


fake = Faker()


def emit_rows(count, row_fn):
    row_count = 0
    def construct_row():
        nonlocal row_count
        row_count += 1
        return '({})'.format(', '.join(row_fn(row_count)))

    if count == 0:
        return '()'
    
    if count == 1:
        return '{}'.format(construct_row())
        
    result = '{}\n'.format(construct_row())
    for i in range(count - 2):
        result += '    {},\n'.format(construct_row())
    return '{}    {}'.format(result, construct_row())


def emit_teacher_rows():
    return 'insert into teacher (id, "name")\n' + \
        '    values {};'.format(
            emit_rows(
                ROW_SPECS['teacher'],
                lambda i: ['{}'.format(i), '\'{} {}\''.format(fake.first_name(), fake.last_name())],
            )
        )


def emit_student_rows():
    return 'insert into student (id, "name")\n' + \
        '    values {};'.format(
            emit_rows(
                ROW_SPECS['student'],
                lambda i: ['{}'.format(i), '\'{} {}\''.format(fake.first_name(), fake.last_name())],
            )
        )


def emit_class_rows():
    def row_generator(i):
        year = random.randint(7, 12)
        name = random.choice(class_types)
        code = '\'{}{}{}\''.format(year, name, random.choice(class_letters))
        teacher_id = '{}'.format(random.randint(1, ROW_SPECS['teacher']))

        return ['{}'.format(i), code, '\'{}\''.format(year), '\'{}\''.format(name), teacher_id]

    return 'insert into school_class (id, code, "year", "name", teacher_id)\n' + \
        '    values {};'.format(
            emit_rows(ROW_SPECS['class'], row_generator)
        )


def emit_student_memberships():
    class_assignments = {}
    for i in range(1, ROW_SPECS['class'] + 1):
        student_ids = [ j for j in range(1, ROW_SPECS['student'] + 1) ]
        random.shuffle(student_ids)
        class_assignments[i] = student_ids[:ROW_SPECS['students_per_class']]

    def row_generator(i):
        class_id = ((i - 1) // ROW_SPECS['students_per_class']) + 1
        student_id = class_assignments[class_id][i % ROW_SPECS['students_per_class']]
        return ['{}'.format(class_id), '{}'.format(student_id)]

    return 'insert into school_class_student (class_id, student_id)\n' + \
        '    values {};'.format(
            emit_rows(ROW_SPECS['class'] * ROW_SPECS['students_per_class'], row_generator)
        )


def main():
    print(emit_teacher_rows())
    print()
    print(emit_student_rows())
    print()
    print(emit_class_rows())
    print()
    print(emit_student_memberships())


if __name__ == '__main__':
    main()
