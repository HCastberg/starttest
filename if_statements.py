#if statement = a block of code that will execute of it,s condition is true.

age = int(input("How old are you?: "))


if age == 100:
    print("You are a century old human!")
elif age >= 25:
    print("You are an adult!")
elif age < 0:
    print("You haven't been born yet!")
else:
    print("You are a kid!")