"""命令行记账小程序 —— 骨架代码

按 README.md 的 5 步计划，把 TODO 一个个填掉。
函数签名（参数和返回值的类型注解）都写好了，正好复习 01-类型注解.py 学的内容。
"""

import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "records.json"


def load_records() -> list[dict]:
    """从 JSON 文件读取所有记录；文件不存在时返回空列表。（第 3 步）"""
    if not DATA_FILE.exists():
        return []
    else:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    # TODO: 如果 DATA_FILE 不存在，返回 []1
    #       否则用 open() + json.load() 读出来并返回
    #       提示：DATA_FILE.exists() 可以判断文件是否存在
    
    return []


def save_records(records: list[dict]) -> None:
    """把所有记录写回 JSON 文件。（第 3 步）"""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)
    # TODO: 用 open(..., "w", encoding="utf-8") + json.dump() 写入
    #       json.dump 加上 ensure_ascii=False, indent=2 参数，文件里的中文才好看
    pass


def add_record(records: list[dict]) -> None:
    """记一笔：问用户项目名和金额，加进列表。（第 2 步）"""
    item = input("请输入项目名: ")
    amount = float(input("请输入金额: "))
    id = max([r["id"] for r in records], default=0) + 1
    records.append({"id": id, "item": item, "amount": amount})
    # TODO: 1. input() 读项目名
    #       2. input() 读金额，用 float() 转成小数
    #       3. 计算新 id：现有记录里最大的 id + 1（列表为空时 id 为 1）
    #       4. 组装字典 {"id": ..., "item": ..., "amount": ...} 并 append
    pass


def show_records(records: list[dict]) -> None:
    """打印所有记录和总支出。（第 2 步）"""
    if not records:
        print("还没有记录")
    else:
        for r in records:
            print(f"{r['id']}. {r['item']} - {r['amount']}")
        total = sum(r["amount"] for r in records)
        print(f"总支出: {total}")
    # TODO: 列表为空时提示"还没有记录"
    #       否则逐条打印，最后打印总金额（用 sum() 试试）
    pass


def delete_record(records: list[dict]) -> None:
    """按 id 删除一条记录。（第 4 步）"""
    input_id = int(input("请输入要删除的记录 id: "))
    record_to_delete = next((r for r in records if r["id"] == input_id), None)
    if record_to_delete:
        records.remove(record_to_delete)
        print("记录已删除")
    else:
        print("未找到该记录")

    # TODO: 1. input() 读 id，用 int() 转换
    #       2. 在列表里找到 id 相同的那条，用 records.remove(...) 删掉
    #       3. 找不到时打印提示，不要报错
    pass


def update_record(records: list[dict]) -> None:
    """按 id 修改一条记录的项目名和金额。（第 4 步）"""
    input_id = int(input("请输入要修改的记录 id: "))
    record_to_update = next((r for r in records if r["id"] == input_id), None)
    if record_to_update:
        new_item = input("请输入新的项目名: ")
        new_amount = float(input("请输入新的金额: "))
        record_to_update["item"] = new_item
        record_to_update["amount"] = new_amount
        print("记录已更新")
    # TODO: 找到对应记录后，重新 input() 项目名和金额，直接改字典的值
    pass


def main() -> None:
    """程序入口：菜单循环。（第 1 步，从这里开始写！）"""
    records = load_records()

    while True:
        print()
        print("===== 记账本 =====")
        print("1. 记一笔")
        print("2. 查看所有记录")
        print("3. 删除一条记录")
        print("4. 修改一条记录")
        print("0. 退出")
        choice = input("请选择: ")

        # TODO: 根据 choice 调用上面对应的函数
        #       增、删、改之后记得调用 save_records(records)
        #       choice 是 "0" 时 break
        #       无效输入时给个提示
        while True:
            if choice == "1":
                print("记一笔")
                add_record(records)
                save_records(records)
                break
            elif choice == "2":
                print("查看所有记录")
                show_records(records)
                break           
            elif choice == "3":
                print("删除一条记录")
                delete_record(records)
                save_records(records)
                break
            elif choice == "4":
                print("修改一条记录")
                update_record(records)
                save_records(records)
                break
            elif choice == "0":
                print("退出程序")
                return
            else:
                print("无效输入，请重新选择")
                break
        


if __name__ == "__main__":
    main()
