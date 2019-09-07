# Torbjorn

🔨 提供一些实用的 Python 装饰器～

## 安装

```bash
pip install torbjorn
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
