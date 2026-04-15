import random
import time
from multiprocessing import Process, Queue

def worker(sub_data, target, q, offset):
    for local_index, value in enumerate(sub_data):
        if value == target:
            global_index = offset + local_index
            q.put(global_index)
            return
    q.put(-1)

def parallel_search(data, target, num_processes=4):
    chunk_size = len(data) // num_processes
    chunks = []
    offsets = []

    for i in range(0, len(data), chunk_size):
        chunks.append(data[i : i + chunk_size])
        offsets.append(i)

    q = Queue()
    processes = []

    for chunk, offset in zip(chunks, offsets):
        p = Process(target=worker, args=(chunk, target, q, offset))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    results = []
    while not q.empty():
        results.append(q.get())

    hits = [r for r in results if r != -1]
    return min(hits) if hits else -1

def run_parallel_search(data, target, label="", num_processes=4):
    print(f"\n[Parallel Search – {num_processes} processes] {label}")
    print(f"  Searching for : {target}")
    start = time.time()
    result = parallel_search(data, target, num_processes)
    end = time.time()
    elapsed = end - start

    if result != -1:
        print(f"  Found at index : {result} (value = {data[result]})")
    else:
        print(f"  Result : Target not found")

    print(f"  Elements : {len(data):,}")
    print(f"  Time     : {elapsed:.4f} seconds")
    return result, elapsed

if __name__ == "__main__":
    sizes = {
        "Small  (1,000)"     : 1_000,
        "Medium (100,000)"   : 100_000,
        "Large  (1,000,000)" : 1_000_000,
    }

    for label, n in sizes.items():
        data = [random.randint(1, 1_000_000) for _ in range(n)]
        target = data[random.randint(0, n - 1)]
        run_parallel_search(data, target, label + " (target exists)")
        run_parallel_search(data, -999, label + " (target missing)")

    data_sorted = list(range(1, 10_001))
    run_parallel_search(data_sorted, 7500, "Already-Sorted (10,000)")

    data_reverse = list(range(10_000, 0, -1))
    run_parallel_search(data_reverse, 2500, "Reverse-Sorted (10,000)")
