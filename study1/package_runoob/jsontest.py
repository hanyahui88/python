import json

dir(json)
data = {
    'no': 1,
    'age': 12
}

json_str = json.dumps(data)
print("Python 原始数据：", repr(data))
print("JSON 对象：", json_str)

data2 = json.loads(json_str)
print("data2['no']: ", data2['no'])
print("data2['age']: ", data2['age'])

# 写入 JSON 数据
with open('data.json', 'w') as f:
    json.dump(data, f)

# 读取数据
with open('data.json', 'r') as f:
    data = json.load(f)
