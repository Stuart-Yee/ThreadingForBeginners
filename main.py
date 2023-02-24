from concurrent.futures import ThreadPoolExecutor
import threading
import time
from datetime import datetime

def service_call(input=None):
    # Simulates a service call to an external endpont taking approximately 2 seconds
    time.sleep(2)
    print("Service finished at " + str(datetime.now()) + "\n")
    return str(datetime.now()) + " service completed for " + str(input)

def integraton_hook():
    print("Standard hook begins " + str(datetime.now()))
    # A synchronous call of 4 services
    res1 = service_call(1)
    res2 = service_call(2)
    res3 = service_call(3)
    res4 = service_call(4)
    print("End of hook " + str(datetime.now()))

def threaded_integration_hook():
    print("Threaded Hook begins " + str(datetime.now()))
    # basic threading to execute each function
    # Each thread is instantiated
    t1 = threading.Thread(target=service_call)
    t2 = threading.Thread(target=service_call)
    t3 = threading.Thread(target=service_call)
    t4 = threading.Thread(target=service_call)
    # Each thread is started and will run concurrently
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    # this print statement will be executed next
    # which may be before the preceding threads
    # finish making its message misleading
    print("End of hook " + str(datetime.now()))

    # The disadvantage is that this pattern doesn't
    # work if subsequent lines of code depend on the
    # outcome of any given thread

def threadpool_integration_hook():
    # The ThreadPool approach is used to manage
    # the outcome of each thread (such as an HTTP
    # response)

    print("ThreadPool Hook begins " + str(datetime.now()))

    # with as context manager used to automatically
    # shut down the Threadpool when the threads are
    # completed to free those resources
    with ThreadPoolExecutor() as executor:
        future1 = executor.submit(service_call, 1)
        future2 = executor.submit(service_call, 2)
        future3 = executor.submit(service_call, 3)
        future4 = executor.submit(service_call, 4)
        res1 = future1.result()
        res2 = future2.result()
        res3 = future3.result()
        res4 = future4.result()

    # The following print statement (and any lines of
    # code) will execute only after the ThreadPool
    # shuts down so we can write code dependent on
    # their outcome

    print("End of ThreadPool")

    print("response: " + res1)
    print("response: " + res2)
    print("response: " + res3)
    print("response: " + res4)



    print("Hook ends " + str(datetime.now()))




if __name__ == '__main__':
    integraton_hook()
    threaded_integration_hook()
    threadpool_integration_hook()

