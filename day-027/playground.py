def add(*args) -> int:
    return sum(args)


print(add(1, 2, 3, 4, 5, 6))


def calculate(n, **kwargs):
    print(kwargs)

    # for key, value in kwargs.items():
    #     print(f"key => {key}\t value => {value}")

    # print(kwargs["add"])

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kw) -> None:
        # self.make = kw["make"]
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")


# my_car = Car(make="Nissan", model="GT-R")
my_car = Car(make="Nissan")
print(my_car.model)
