def main():
    i = 0
    print("let's fizzbuzz")
    while i < 100:
        i += 1
        if i % 3 == 0:
            print(str(i) + " Fizz")
            if i % 5 == 0:
                print(str(i) + " FizzBuzz")
        elif i % 5 == 0:
            print(str(i) + " Buzz")


if __name__ == "__main__":
        main()

