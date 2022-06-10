# Torbjorn

[![Pypi](https://img.shields.io/pypi/v/torbjorn.svg)](https://pypi.org/project/torbjorn/)
[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/Ailln/torbjorn/blob/master/LICENSE)
[![stars](https://img.shields.io/github/stars/Ailln/torbjorn.svg)](https://github.com/Ailln/torbjorn/stargazers)
[![build](https://img.shields.io/github/workflow/status/Ailln/torbjorn/build)](https://github.com/Ailln/torbjorn/actions?query=workflow%3Abuild)

🔨 提供一些实用的 Python 装饰器～

`Torbjorn`（即托比昂）是守望先锋游戏中的英雄之一，他拥有一个强力输出的炮台。
俗话说「他强任他强，我用托比昂」，我希望本项目也能给你的 Python 代码提供强力的支持！

> 🎈️ v0.1.1：
>
> 使用 `time.perf_counter` 计算时间，以提高精准度。

## 安装

```bash
# pip 安装
pip install torbjorn

# or 源码安装
git clone https://github.com/Ailln/torbjorn.git
cd torbjorn && python setup.py install
```

## 使用

- `run_time`: 计算运行时间
- `run_count`: 计算运行次数
- `ctrl_c`: 程序终止验证

```python
import logging

import torbjorn as tbn


logger = logging.getLogger(__name__)


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


if __name__ == '__main__':
    for _ in range(10):
        calculate_million_numbers(1000000)
        
# output:
# [calculate_million_numbers] run count(t): 1
# [test_count] run count(t): 1
# [test_count] run count(t): 1
# [test_time] run time(s): 0.074010
# [test_time] run time(s): 0.074463
# [calculate_million_numbers] run time(s): 0.074512
# [calculate_million_numbers] run count(t): 2
# [test_count] run count(t): 2
# [test_count] run count(t): 2
# [test_time] run time(s): 0.074386
# [test_time] run time(s): 0.074522
# [calculate_million_numbers] run time(s): 0.074556
# ^CAre you sure to quit? (yes|y) / (no|n)
# >> 123
# ^CAre you sure to quit? (yes|y) / (no|n)
# >> no
# [calculate_million_numbers] run count(t): 3
# [test_count] run count(t): 3
# [test_count] run count(t): 3
# [test_time] run time(s): 0.072722
# [test_time] run time(s): 0.072863
# [calculate_million_numbers] run time(s): 0.072897
# ^CAre you sure to quit? (yes|y) / (no|n)
# >> yes
# >> exit...
```

## 许可

[![](https://award.dovolopor.com?lt=License&rt=MIT&rbc=green)](./LICENSE)
