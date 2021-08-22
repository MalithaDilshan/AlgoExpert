import time


def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(func.__name__ + " has taken " + str((end_time - start_time) * 1000) + "ms")
        return result
    return wrapper


@measure_time
def calc_square(numbers):
    result = []
    for value in numbers:
        result.append(value * value)
    return result


@measure_time
def calc_cube(numbers):
    result = []
    for value in numbers:
        result.append(value * value * value)
    return result


number_array = range(1, 1000000)
square_result = calc_square(number_array)
cube_result = calc_cube(number_array)
