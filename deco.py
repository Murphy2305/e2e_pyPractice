from datetime import datetime

def execution_time_decorator(org_fun):
    def wrapper():
        start_time = datetime.now() 
        org_fun()
        end_time = datetime.now()
        duration = end_time - start_time
        print("Execution time of function is:", duration)
    return wrapper  

def log_time_decorator(org_fun):
    def wrapper():

        with open('logFile.txt', "a") as f:
            f.write("Log In time: " + datetime.now().strftime("[%Y-%m-%d %H:%M:%S]") + "\n")
        
        org_fun()

        with open('logFile.txt', "a") as f:
            f.write("Log Out time: " + datetime.now().strftime("[%Y-%m-%d %H:%M:%S]") + "\n")

    return wrapper

@execution_time_decorator
@log_time_decorator
def some_long_fun():
    c = 0
    for i in range(10**8):
        c += 1

some_long_fun()
