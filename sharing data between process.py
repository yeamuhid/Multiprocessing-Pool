import multiprocessing

def calc_square(numbers,result, v):
    v.value = 5.66
    for idx,n  in enumerate(numbers):
        result[idx] = n*n

if __name__ == '__main__':
    numbers=[1,2,3,4,5,6,7,8,9]
    result= multiprocessing.Array('i', 9)
    v = multiprocessing.Value('d',0.0)
    P= multiprocessing.Process(target=calc_square, args=(numbers,result,v))

    P.start()
    P.join()
    print(v.value)