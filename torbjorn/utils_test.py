import torbjorn as tbn


@tbn.run_time
def calculate_million_numbers():
    number = 0
    for i in range(1000000):
        number += 1


if __name__ == '__main__':
    calculate_million_numbers()
