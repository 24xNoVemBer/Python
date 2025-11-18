def solve(N: int, arr: list):
    for i in range(N - 1):
        min_idx = i
        for j in range(i + 1, N):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            step_number = i + 1
            output_line = f"Buoc {step_number}: " + " ".join(map(str, arr))
            print(output_line)


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    solve(n, arr)
main()
import sys


def solve(N: int, arr: list):
    # Logic thuật toán (đã đúng)
    for i in range(N - 1):
        min_idx = i
        for j in range(i + 1, N):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Chỉ in ra khi có hoán đổi
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            step_number = i + 1

            # Sử dụng định dạng theo Ví dụ (không có ngoặc vuông)
            output_line = f"Buoc {step_number}: " + " ".join(map(str, arr))
            print(output_line)


def main():
    try:
        N_line = sys.stdin.readline().strip()
        if not N_line: return
        n = int(N_line)

        arr_line = sys.stdin.readline().strip()
        if not arr_line: return
        arr = list(map(int, arr_line.split()))
        solve(len(arr), arr)

    except Exception:
        pass

main()