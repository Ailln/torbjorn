# Torbjorn

🔨 提供一些实用的 Python 装饰器～

`Torbjorn`（即托比昂）是守望先锋游戏中的英雄之一，他拥有一个强力输出的炮台。
俗话说「他强任他强，我用托比昂」，我希望本项目也能给你的 Python 代码提供强力的支持！

> ⚠️ v0.0.4 新版本介绍：
>
> 不知道你有没有这样的烦恼，跑了很久的代码，被自己一不小按了 `Ctrl C` 给终止掉了，
> 重新跑又需要大量的时间，试试 `@tbn.ctrl_c` 吧，交互式的终止验证可以让你摆脱这一烦恼！

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
import torbjorn as tbn


@tbn.run_time
@tbn.run_count
@tbn.ctrl_c
def calculate_million_numbers(num):
    number = 0
    for _ in range(num):
        number += 1


if __name__ == '__main__':
    for _ in range(10):
        calculate_million_numbers(1000000)
        
# output:
# >> [calculate_million_numbers] run count: 1
# >> [calculate_million_numbers] run time: 0:00:00.057086
# >> [calculate_million_numbers] run count: 2
# ^CAre you sure to quit? yes/no
# >> 123
# Are you sure to quit? yes/no
# >> no
# >> [calculate_million_numbers] run time: 0:00:00.100949
# >> [calculate_million_numbers] run count: 3
# >> [calculate_million_numbers] run time: 0:00:00.050162
# >> [calculate_million_numbers] run count: 4
# >> [calculate_million_numbers] run time: 0:00:00.049104
# >> [calculate_million_numbers] run count: 5
# >> [calculate_million_numbers] run time: 0:00:00.049974
# ^CAre you sure to quit? yes/no
# >> yes
# >> exit...
```

## 许可

[![](https://award.dovolopor.com?lt=License&rt=MIT&rbc=green)](./LICENSE)
