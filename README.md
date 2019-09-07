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

```python
import torbjorn as tbn

# run_time 计算函数运行时间
@tbn.run_time
def calculate_million_numbers():
    number = 0
    for i in range(1000000):
        number += 1
        
# output:
# >> function "calculate_million_numbers" cost time: 0:00:00.059892
```

## 许可

[![](https://award.dovolopor.com?lt=License&rt=MIT&rbc=green)](./LICENSE)
