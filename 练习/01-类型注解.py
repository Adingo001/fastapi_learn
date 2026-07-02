"""
类型注解（Type Hints）入门
==========================

一句话解释：给变量和函数"贴标签"，说明它应该是什么类型。

重要认知：类型注解只是"标签"，Python 运行时并不强制检查！
写错了类型程序照样能跑（但编辑器会画波浪线提醒你）。
那为什么 FastAPI 离不开它？因为 FastAPI 会读取这些标签，
自动帮你做参数校验、类型转换、生成接口文档——标签就是配置。

先看懂下面的例子，然后完成底部的练习。
"""

# ── 1. 变量注解 ──────────────────────────────────────
name: str = "小明"        # name 应该是字符串
age: int = 18             # age 应该是整数
price: float = 9.9        # 小数
is_vip: bool = True       # 布尔值（True/False）


# ── 2. 函数注解（最常用！）─────────────────────────
# 参数冒号后面写参数类型，-> 后面写返回值类型
def add(a: int, b: int) -> int:
    return a + b


def greet(name: str) -> str:
    return f"你好，{name}"


# 没有返回值的函数，返回类型写 None
def say_hello(name: str) -> None:
    print(f"Hello, {name}")


# ── 3. 容器类型：列表、字典 ─────────────────────────
# list[里面装什么]   dict[键的类型, 值的类型]
scores: list[int] = [90, 85, 77]
student: dict[str, str] = {"name": "小明", "city": "北京"}

# 列表里装字典（记账程序会用到这个结构！）
records: list[dict] = [
    {"item": "午饭", "amount": 25.0},
    {"item": "地铁", "amount": 4.0},
]


# ── 4. 可能为空：Optional ───────────────────────────
# "str | None" 表示：可能是字符串，也可能是 None（没有值）
def find_user(user_id: int) -> dict | None:
    users = {1: {"name": "小明"}, 2: {"name": "小红"}}
    return users.get(user_id)  # 找不到时 get 返回 None


# ── 5. 默认值 + 注解（FastAPI 里到处都是这种写法）──
def query_items(keyword: str, limit: int = 10, skip: int = 0) -> list:
    print(f"搜索 {keyword}，跳过 {skip} 条，最多返回 {limit} 条")
    return []


# ═══════════════════════════════════════════════════
#  练习：给下面的函数补上类型注解（参数 + 返回值）
#  改完后运行本文件，全部通过会打印 "🎉 全部正确"
# ═══════════════════════════════════════════════════

# 练习 1：计算总价。price 是小数，count 是整数，返回小数
def total_price(price: float, count: int) -> float:
    return price * count


# 练习 2：判断是否成年。age 是整数，返回 True 或 False
def is_adult(age : int) -> bool:
    return age >= 18


# 练习 3：把名字列表拼成一句欢迎语。names 是字符串列表，返回字符串
def welcome_all(names : list[str]) -> str:
    return "欢迎：" + "、".join(names)


# 练习 4：按名字查电话，可能查不到。
# phonebook 是"字符串→字符串"的字典，name 是字符串
# 返回值可能是字符串，也可能是 None
def find_phone(phonebook : dict[str, str], name : str) -> str | None:
    return phonebook.get(name)


# ── 自动检查（不用看懂这段，运行就行）────────────────
if __name__ == "__main__":
    import inspect

    expected = {
        total_price: ({"price": float, "count": int}, float),
        is_adult: ({"age": int}, bool),
        welcome_all: ({"names": list[str]}, str),
        find_phone: ({"phonebook": dict[str, str], "name": str}, str | None),
    }
    ok = True
    for func, (params, ret) in expected.items():
        hints = inspect.get_annotations(func)
        for p, t in params.items():
            if hints.get(p) != t:
                print(f"❌ {func.__name__} 的参数 {p} 注解应为 {t}，当前是 {hints.get(p)}")
                ok = False
        if hints.get("return") != ret:
            print(f"❌ {func.__name__} 的返回值注解应为 {ret}，当前是 {hints.get('return')}")
            ok = False
    if ok:
        print("🎉 全部正确！类型注解你已经会了")
