def process_item(item: list[str]):
    for item in items:
        print(item)

def process_items(items_t: triple[int, int , str], items_s: set[bytes]):
    return items_t, items_s

def process_items_dict(price: dict[str, float]):
    for items_name, item_price in price.items():
        print(f"Item: {items_name}, Price: {item_price}")
    
def process_items(item : int | str ):
    print(item)

def say_hi(name: str | None = None):
    if name:
        print(f"Hi {name}")
    else:
        print("Hi there!")

class Person :
    def __init__(self,name: str):
        self.name = name

def get_person(one_person: Person):
    return one_person.name

async def fetch_data(url: str) -> dict:
    # 模拟异步请求数据
    return {"url": url, "data": "some data"}
def process_data(data: list[dict[str, int]]):
    for record in data:
        print(record)

def get_persons(people: list[Person]):
    return [person.name for person in people]

