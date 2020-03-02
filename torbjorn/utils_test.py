import torbjorn as tbn


@tbn.run_time
@tbn.run_count
@tbn.ctrl_c
def calculate_million_numbers(num):
    number = 0
    for _ in range(num):
        number += 1


if __name__ == '__main__':
    for _ in range(100):
        calculate_million_numbers(10000000)

