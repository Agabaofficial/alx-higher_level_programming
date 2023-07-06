#!/usr/bin/python3

def magic_string():
    if 'count' not in magic_string.__dict__:
        magic_string.count = 0
    magic_string.count += 1
    return 'BestSchool' + (', BestSchool' * magic_string.count)[:-2] + '\n'
