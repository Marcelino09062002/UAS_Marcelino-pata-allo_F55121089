import time


def bubble_sort(arr):
    n = len(arr)
    start_time = time.time()

    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    end_time = time.time()
    execution_time = end_time - start_time
    return arr, execution_time


def insertion_sort(arr):
    n = len(arr)
    start_time = time.time()

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    end_time = time.time()
    execution_time = end_time - start_time
    return arr, execution_time


def print_iteration(iteration, arr):
    print(f"Iteration {iteration}: {arr}")


def print_computation_time(time):
    print(f"Computation time: {time} seconds")


def print_before_after(before, after):
    print(f"Before sorting: {before}")
    print(f"After sorting: {after}")


# List yang diberikan
lst = [12, 99, 62, 15, 20, 95, 39, 48, 3, 24, 8, 43, 74, 19, 97, 33, 49, 68, 55, 33, 90, 90, 7,
       26, 85, 46, 39, 40, 9, 36, 60, 64, 89, 31, 25, 71, 21, 23, 63, 84, 32, 5, 3, 44, 21, 10, 21,
       17, 50, 2, 36, 53, 79, 54, 19, 88, 1, 32, 31, 15, 6, 3, 1, 40, 22, 43, 18, 1, 77, 9, 59,
       40, 7, 41, 81]

# Memilih metode pengurutan dari pengguna
print("Pilih metode pengurutan:")
print("1. Bubble Sort")
print("2. Insertion Sort")
choice = input("Masukkan pilihan (1/2): ")

if choice == '1':
    sorted_lst, time_taken = bubble_sort(lst)
elif choice == '2':
    sorted_lst, time_taken = insertion_sort(lst)
else:
    print("Pilihan tidak valid.")
    exit()

# Menampilkan hasil 5 iterasi pertama dan terakhir
print("\nHasil 5 iterasi pertama:")
for i in range(5):
    print_iteration(i + 1, sorted_lst)
print("\nHasil 5 iterasi terakhir:")
for i in range(len(sorted_lst) - 5, len(sorted_lst)):
    print_iteration(i + 1, sorted_lst)

# Men