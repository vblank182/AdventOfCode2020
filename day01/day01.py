## Advent of Code 2020: Day 1
## https://adventofcode.com/2020/day/1
## Jesse Williams | github.com/vblank182
## Answers: [Part 1]: 980499, [Part 2]: 200637446

with open('day01_input.txt') as f:
    nums = f.readlines()
    nums = [int(n) for n in nums]

    ##################
    ###|  Part 1  |###
    ##################
    for num in nums:
        if (2020 - num) in nums:
            answer = [num, 2020 - num]
            break

    print(f'[Part 1] Entries {answer[0]} and {answer[1]} have a sum of 2020 and a product of {answer[0]*answer[1]}.')


    ##################
    ###|  Part 2  |###
    ##################
    for numA in nums:                               # super optimized algorithm. definitely not O(n^3).
        for numB in nums:
            for numC in nums:
                if (numA + numB + numC == 2020):
                    answer = [numA, numB, numC]
                    break

    print(f'[Part 2] Entries {answer[0]}, {answer[1]}, and {answer[2]} have a sum of 2020 and a product of {answer[0]*answer[1]*answer[2]}.')
