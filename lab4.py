import random

def main():
    # Размер массива
    n: int = 10
    
    # Создание случайного массива от 1 до 100
    arr: list[int] = [random.randint(1, 100) for _ in range(n)]
    
    print("Исходный массив:")
    print(arr)
    
    # Сортировка пузырьком
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                # Обмен элементов
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
    print("\nМассив после сортировки (по возрастанию):")
    print(arr)

if __name__ == "__main__":
    main()
