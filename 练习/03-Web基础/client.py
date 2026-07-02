"""模拟"前端"：用代码向服务器发 HTTP 请求

先在另一个终端运行 mini_server.py，再运行本文件：python client.py

浏览器地址栏只能发 GET，用代码可以发任何方法——
这就是前端 JavaScript 调用后端 API 时干的事，今天我们用 Python 模拟。
"""

import json
import urllib.request

BASE_URL = "http://127.0.0.1:8000"


def get_records() -> list[dict]:
    """发 GET 请求，获取所有记录"""
    resp = urllib.request.urlopen(f"{BASE_URL}/records")
    print("状态码:", resp.status)                          # 应该是 200
    print("响应头 Content-Type:", resp.headers["Content-Type"])
    return json.loads(resp.read())                         # 响应体：JSON 文本 → Python 列表


def add_record(item: str, amount: float) -> dict:
    """发 POST 请求，新增一条记录"""
    payload = json.dumps({"item": item, "amount": amount}).encode("utf-8")
    req = urllib.request.Request(
        f"{BASE_URL}/records",
        data=payload,                                      # 请求体
        headers={"Content-Type": "application/json"},      # 请求头：声明发的是 JSON
        method="POST",                                     # 请求方法
    )
    resp = urllib.request.urlopen(req)
    print("状态码:", resp.status)                          # 应该是 201（Created）
    return json.loads(resp.read())


if __name__ == "__main__":
    print("── ① GET /records：查看现有记录 ──")
    records = get_records()
    for r in records:
        print("  ", r)

    print()
    print("── ② POST /records：新增一条记录 ──")
    new = add_record("奶茶", 15.0)
    print("服务器返回的新记录:", new)

    print()
    print("── ③ 再 GET 一次，确认新记录已存在 ──")
    # TODO 1: 调用上面已有的函数，再次获取并打印所有记录
    #         确认"奶茶"出现在列表里

    print()
    print("── ④ 制造一个 404 ──")
    # TODO 2: 向一个不存在的路径（比如 /xxx）发 GET 请求，观察报错
    #         提示：直接写 urllib.request.urlopen(f"{BASE_URL}/xxx")
    #         程序会抛 HTTPError 异常——异常信息里就有状态码 404。
    #         进阶：用 try/except 接住它，优雅地打印状态码（复习记账程序第 5 步的技能）
