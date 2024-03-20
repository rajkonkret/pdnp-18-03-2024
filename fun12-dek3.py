import time
import numpy as np  # np to alias


def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Czas wykonania funkcji {func.__name__}: {execution_time}")
        return result

    return wrapper


@measure_time
def my_wait():
    time.sleep(2)  # poczekaj 2 sekundy


@measure_time
def my_for_sum():
    suma = 0
    for i in range(15_000_000):
        suma += i
    print("Sum is:", suma)


@measure_time
def my_sum_without_for():
    total = sum(range(15_000_000))
    print('Sum is:', total)


@measure_time
def my_sum_np():
    total = np.sum(np.arange(15_000_000), dtype=np.int64)
    print("Sum is:", total)


my_wait()  # Czas wykonania funkcji my_wait: 2.0037410259246826
my_for_sum()  # Czas wykonania funkcji my_for_sum: 0.9140093326568604
my_sum_without_for()  # Czas wykonania funkcji my_sum_without_for: 0.6284403800964355
my_sum_np()  # Czas wykonania funkcji my_sum_np: 0.03899669647216797  # 15x szybciej
