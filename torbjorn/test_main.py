import logging
import torbjorn as tbn


logger = logging.getLogger(__name__)


def test_main():
    @tbn.run_time
    @tbn.run_time(name="test_time")
    @tbn.run_time(logger=logger, name="test_time")
    @tbn.run_count
    @tbn.run_count(name="test_count")
    @tbn.run_count(logger=logger, name="test_count")
    @tbn.ctrl_c
    def calculate_million_numbers(num):
        number = 0
        for _ in range(num):
            number += 1

    for index in range(10):
        calculate_million_numbers(1000000)


if __name__ == '__main__':
    test_main()
