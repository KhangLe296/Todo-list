import datetime

def merge(arr1, arr2):
    i = j = 0
    n1 = len(arr1)
    n2 = len(arr2)
    arr = []
    while i < n1 and j < n2:
        if arr1[i].deadline > arr2[j].deadline:
            arr.append(arr2[j])
            j += 1
        elif arr1[i].deadline < arr2[j].deadline:
            arr.append(arr1[i])
            i += 1
        elif arr1[i].deadline == arr2[j].deadline:
            arr.append(arr1[i])
            arr.append(arr2[j])
            i += 1
            j += 1
    for _ in range(n2 - j):
        arr.append(arr2[j])
        j += 1
    for _ in range(n1 - i):
        arr.append(arr1[i])
        i += 1
    return arr

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    n = len(arr) // 2
    L = arr[:n]
    R = arr[n:]
    L = merge_sort(L)
    R = merge_sort(R)
    return merge(L, R)

class Task:
    def __init__(self, name, deadline):
        self.name = name
        self.deadline = deadline

    def __str__(self):
        return self.name + " " + str(self.deadline.date())
        
class TodoList:
    def __init__(self):
        self.task_list = []
    
    def add_task(self, task:Task):
        self.task_list.append(task)
    
    def remove_task(self, id):
        self.task_list.pop(id)

    def show(self):
        print('----------- TODO_LIST -----------')

        for i in range(len(self.task_list)):
            print(i, str(self.task_list[i]))

    def sort(self):
        merge_sort(self.task_list)

def print_commands():
    print('1: add a new task \n2: remove a task\n3: finish ')


def add_task():
    while True:
        print("ADDING A NEW TASK...")
        name = input("Enter task name: ")
        deadline = input("Enter deadline (yyyymmdd): ")

        while True:
            try:
                deadline = datetime.datetime(int(deadline[:4]), int(deadline[4:6]), int(deadline[6:]))
                break
            except:
                deadline = input("Enter a valid deadline (yyyymmdd): ")

        new_task = Task(name, deadline)
        to_do_list.add_task(new_task)
        to_do_list.sort()
        to_do_list.show()
        answer = input("Continue? (Y/N) ").strip()
        if answer.upper() == "N":
            break

def remove_task():
    while True:
        print("DELETING A TASK...")
        while True:
            try:
                id = int(input("Enter task order: "))
                to_do_list.remove_task(id)
                break
            except:
                id = int(input("Enter a valid order: "))
        to_do_list.show()

        answer = input("Continue? (Y/N) ").strip()
        if answer.upper() == "N":
            break


to_do_list = TodoList()

while True:
    print_commands()
    command = input("Choose your command: ").strip()
    if command == "1":
        add_task()
    elif command == "2":
        remove_task()
    elif command == "3":
        answer = input("Exit? (Y/N) ").strip()
        if answer.upper() == "Y":
            break





