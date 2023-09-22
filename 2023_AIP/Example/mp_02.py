from multiprocessing import Pool

def work(x):
    print(x)

if __name__ == "__main__":
    pool = Pool(4)  # 일꾼 4개
    data = range(1, 100)    # 시킬 일 100개
    pool.map(work, data)