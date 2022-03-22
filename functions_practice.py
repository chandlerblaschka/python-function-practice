def hello():
    print("hello user")

hello()

def pack(a, b, c):
    return [a, b, c]

print(pack("bread", "soda", "fruit"))

def eat_lunch(list):
    if len(list) == 0:
        print("My lunchbox is empty!")
    else:
        for i in range(len(list)):
            if i == 0:
                print(f"First I eat {list[0]}")
            else:
                print(f"Next I eat {list[i]}")

eat_lunch(["taco", "sandwich", "fruit", "salad"])