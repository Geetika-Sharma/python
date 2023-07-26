import time

def calculate_time(func):
    def wrapper():
        t1 = time.time()
        func()
        t2 = time.time()-t1
        print(f"{func.__name__} ran in" \
              f"{t2} seconds")
    return wrapper

@calculate_time
def do_this():
    time.sleep(1.3)

@calculate_time
def do_that():
    time.sleep(1.5)


do_that()
do_this()
print('Done')