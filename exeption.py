try:
    a=[2,3,4,5]
    print(a[6])
except ZeroDivisionError:
    print("denominator cannot be 0.")
except IndexError:
    print("index out of bound.")
