已修复 [allocator.py](allocator.py)。问题出在实现忽略了已有的完整名单；现在使用当天名单，按字母排序后返回第一人，无人可用时返回空列表：

```python
def allocate(day, availability):
    return sorted(availability.get(day, []))[:1]
```

已运行 7 项测试，覆盖仅 B 可用、乱序名单、空名单、按指定日期选择、A 可用时的正确结果、输入不被修改及 `greeting` 原有行为。修复前 4 项失败，修复后 7 项全部通过。

已回读文件确认只修改了 `allocate` 的返回语句，接口、原注释及其他代码保持原样。真实测试命令和结果保存在 [execution.json](execution.json)。
