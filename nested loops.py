for x in range(5):
    for y in range(3):
        print(f"{x} , {y}")

# while loop

number = 100
while number > 0:
    number //= 2


while True:
    command = input(">")
    print("echo" , command)
    if command == "quit":
        break

x = 0
for num in range(1,10):
    if num % 2 == 0:
        x+=1
        print(num, "even number")
print(f"we have {x} even numbers")

