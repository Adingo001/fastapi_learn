"""最原始的记账本 HTTP 服务器（只用 Python 标准库）

运行：python mini_server.py
然后浏览器访问 http://127.0.0.1:8000/records

⚠️ 这个文件只要求"读懂大意"，不要求会写！
读的时候重点感受：路径要自己判断、状态码要自己设、JSON 要自己转、
请求体要自己读——每一步都是手工活。
阶段 2 学 FastAPI 时回头看这个文件，你会体会到框架帮你省了多少事。
"""

import json
from http.server import BaseHTTPRequestHandler, HTTPServer

# 数据就放内存里（重启就没了，这里只为演示 HTTP）
records: list[dict] = [
    {"id": 1, "item": "午饭", "amount": 25.0},
    {"id": 2, "item": "地铁", "amount": 4.0},
]


class Handler(BaseHTTPRequestHandler):

    def send_json(self, status_code: int, data) -> None:
        """组装一个 JSON 响应：状态码 + 响应头 + 响应体"""
        body = json.dumps(data, ensure_ascii=False).encode("utf-8")
        self.send_response(status_code)                              # ← 状态行
        self.send_header("Content-Type", "application/json; charset=utf-8")  # ← 响应头
        self.end_headers()
        self.wfile.write(body)                                       # ← 响应体

    def do_GET(self):
        """浏览器/客户端发来 GET 请求时，这个方法被调用"""
        if self.path == "/records":
            self.send_json(200, records)
        else:
            # 没有这个路径 → 404，是客户端的锅
            self.send_json(404, {"error": f"路径 {self.path} 不存在"})

    def do_POST(self):
        """收到 POST 请求：从请求体里读出 JSON，新增一条记录"""
        if self.path != "/records":
            self.send_json(404, {"error": f"路径 {self.path} 不存在"})
            return

        # 手工读请求体：先看请求头里声明的长度，再读那么多字节，再解析 JSON
        length = int(self.headers.get("Content-Length", 0))
        raw = self.rfile.read(length)
        data = json.loads(raw)

        new_record = {
            "id": max((r["id"] for r in records), default=0) + 1,
            "item": data["item"],
            "amount": data["amount"],
        }
        records.append(new_record)
        self.send_json(201, new_record)   # 201 = Created，新增成功


if __name__ == "__main__":
    server = HTTPServer(("127.0.0.1", 8000), Handler)
    print("服务器已启动：http://127.0.0.1:8000/records")
    print("按 Ctrl+C 停止")
    server.serve_forever()
