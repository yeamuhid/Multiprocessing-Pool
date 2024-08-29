import time
import multiprocessing
square_results = []

def calc_square(numbers):
    global square_results
    for n in numbers:
        print('square ' + str(n*n))
        square_results.append(n*n)
    print (square_results)


if __name__ == "__main__":
    arr = [2,3,8]
    p1 = multiprocessing.Process(target=calc_square, args=(arr,))

    p1.start()
    p1.join()

    print('result' + str(square_results))
    print("Done!")