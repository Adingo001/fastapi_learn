"""阶段 2 毕业项目：把你的记账程序改造成 REST API

这就是你在阶段 1 毕业检验第 4 题里设计的那套接口：
    GET    /records        → 查看所有记录
    GET    /records/{id}   → 查看一条
    POST   /records        → 记一笔
    PUT    /records/{id}   → 修改一条
    DELETE /records/{id}   → 删除一条

和 02-记账小程序/main.py 的对应关系：
    菜单循环 + input()  →  没有了！HTTP 请求就是"用户输入"
    print() 输出        →  没有了！返回值就是"输出"
    增删查改的核心逻辑  →  原样保留，从你的 main.py 里搬过来改

启动：conda activate fastapi_env 后运行  fastapi dev 记账API.py
测试：全程在 /docs 里点，不用写任何客户端代码

先照着 hello.py 的第 4、5 节把 TODO 填完，数据先存内存；
全部跑通后再挑战底部的"进阶任务"。
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="记账本 API")

# 数据先放内存（进阶任务再改成 JSON 文件）
records: list[dict] = [
    {"id": 1, "item": "午饭", "amount": 25.0},
]


class RecordIn(BaseModel):
    """客户端提交的数据：只有项目名和金额，id 由服务器分配"""
    item: str
    amount: float


# ── 示例：第一个接口我帮你写好了 ──────────────────────
@app.get("/records")
def list_records():
    return records


# ── 下面 4 个接口自己写 ──────────────────────────────

@app.get("/records/{record_id}")
def get_record(record_id: int):
    # TODO: 在 records 里找到 id 等于 record_id 的那条并返回
    #       找不到就 raise HTTPException(status_code=404, detail="记录不存在")
    #       提示：你在 main.py 里写过一模一样的查找逻辑（next + 生成器表达式）
    pass


@app.post("/records", status_code=201)
def create_record(data: RecordIn):
    # TODO: 1. 算新 id（你的 max(..., default=0) + 1 写法直接搬过来）
    #       2. 组装字典：{"id": ..., "item": data.item, "amount": data.amount}
    #       3. append 进 records，并把新记录返回
    pass


@app.put("/records/{record_id}")
def update_record(record_id: int, data: RecordIn):
    # TODO: 找到对应记录（找不到 404），更新 item 和 amount，返回更新后的记录
    pass


@app.delete("/records/{record_id}")
def delete_record(record_id: int):
    # TODO: 找到对应记录（找不到 404），从列表移除，返回 {"deleted": record_id}
    pass


# ═══════════════════════════════════════════════════
# 进阶任务（全部接口在 /docs 里测试通过后再做）：
#
# 1. 加一个统计接口 GET /records/summary，返回 {"count": 条数, "total": 总金额}
#    ⚠️ 坑预警：这个路由必须定义在 GET /records/{record_id} **之前**，
#    否则 "summary" 会被当成 record_id 解析成 int 而报 422。
#    （路由按定义顺序匹配——踩一次这个坑印象会很深）
#
# 2. 数据持久化：把 02-记账小程序 里的 load_records / save_records
#    搬过来，启动时读文件，每次增删改后存文件。
#    做完后重启服务器，数据还在——你就拥有一个真正能用的后端了。
# ═══════════════════════════════════════════════════
