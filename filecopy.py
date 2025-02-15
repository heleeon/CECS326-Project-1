#!/usr/bin/env python3

def file_copy(src_file, dest_file):
    with open(src_file, 'r') as source:
        data = source.read()

    with open(dest_file, 'w') as dest:
        dest.write(data)


def main():
    src_file = input("Please type the file name you want to read from: " )
    dest_file = input("Please type the file name you want to write to: ")

    file_copy(src_file, dest_file)

main()