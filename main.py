"""
Subtitles reader
"""

import json


def indexsate(file):
    """Define start and end of chank"""
    indexes = []
    # Descriptor format
    start = 0
    end = 0
    i = 0
    for i, line in enumerate(file):
        # print(f'{i}: {line}')
        if line.startswith("1."):
            if start == 0:
                start = i + 1
            else:
                end = i - 1
                index = {"start": start, "end": end}
                indexes.append(index)
                start = i + 1
                end = -1

    if end == -1:
        print('no delemeter')
        end = i
        descr = {"start": start, "end": end}
        indexes.append(descr)
    return indexes


def read_file():
    "The function reads file"
    # Read the subtitile file
    with open ("subtitles/dolly_test.txt", "r") as f:
        lines = f.readlines()
        # Clean \n
        return [line.strip() for line in lines]


def main():
    """Main flow"""
    # refactor
    file = read_file()
    descr = indexsate(file)

    output_file = "metadata.json"

    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(descr, json_file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    main()
