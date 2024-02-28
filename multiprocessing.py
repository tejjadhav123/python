from multiprocessing import Process

def a():
    print(10*24)
def b():
    for i in range(5):
        print('b class')

if '__name__' == '__main__':
    p1=Process(target=a)
    p2=Process(target=b)
    p1.start()
    p2.start()
    p1.join()
    p2.join()


