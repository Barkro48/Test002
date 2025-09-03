
def add_numbers(a, b):
    return a + b
from myfunc import add_numbers

def main():
    a = int(input("กรุณากรอกค่า A: "))
    b = int(input("กรุณากรอกค่า B: "))

    result = add_numbers(a, b)

    print("ผลลัพธ์ของ A + B คือ:", result)

if __name__ == "__main__":
    main()
