# Torbjorn

🔨 提供一些实用的 Python 装饰器～

> Torbjorn（即`托比昂`），他是守望先锋里的一个英雄，托比昂有一个强力输出的炮台。
俗话说`他强任他强，我用托比昂`，我希望本项目也能给你的 Python 代码提供强力的支持！

## 安装

```bash
# pip 安装
pip install torbjorn

# or 源码安装
git clone https://github.com/HaveTwoBrush/torbjorn.git
cd torbjorn && python setup.py install
```

## 使用

- `run_time`: 计算运行时间
- `run_count`: 计算运行次数

```python
import torbjorn as tbn


@tbn.run_time
@tbn.run_count
def calculate_million_numbers(num):
    number = 0
    for _ in range(num):
        number += 1


if __name__ == '__main__':
    for _ in range(5):
        calculate_million_numbers(1000000)
        
# output:
# >> [calculate_million_numbers] run count: 1
# >> [calculate_million_numbers] run time: 0:00:00.057086
# >> [calculate_million_numbers] run count: 2
# >> [calculate_million_numbers] run time: 0:00:00.050949
# >> [calculate_million_numbers] run count: 3
# >> [calculate_million_numbers] run time: 0:00:00.050162
# >> [calculate_million_numbers] run count: 4
# >> [calculate_million_numbers] run time: 0:00:00.049104
# >> [calculate_million_numbers] run count: 5
# >> [calculate_million_numbers] run time: 0:00:00.049974
```

## 许可

[![](https://award.dovolopor.com?lt=License&rt=MIT&rbc=green)](./LICENSE)
