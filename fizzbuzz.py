def fizzbuzz(n):
    for i in range(n):
        i += 1
        result = ""
        if i % 3 == 0:
            result += "fizz"
        if i % 5 == 0:
            result += "buzz"
        if result == "":
            result = i
        print result

fizzbuzz(15)
