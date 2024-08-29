import multiprocessing

import multiprococessing
def calc_square(numbers,q):
    for n in numbers:
        q.put(n*n)

if __name__ == '__main__':
    numbers =[2,3,4,5]

    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=calc_square, args=(numbers,q))

    p.start()
    p.join()

    while not q.empty():
        print(q.get())