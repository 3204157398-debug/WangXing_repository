def add(a, b):
    return a + b


def greet(name):
    print(f"你好，{name}！")


if __name__ == "__main__":
    name = input("请输入你的名字: ")
    try:
        a = int(input("请输入第一个整数: "))
        b = int(input("请输入第二个整数: "))
    except ValueError:
        print("输入无效，请输入整数。")
    else:
        greet(name)
        print(f"{a} + {b} = {add(a, b)}")
