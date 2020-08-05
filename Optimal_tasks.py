# greedy algorith
def optimal_task(tasks):
    tasks.sort()
    for i in range(len(tasks) // 2):
        print(tasks[i], tasks[~i])


tasks = [12, 3, 5, 1, 6, 7]
optimal_task(tasks)
