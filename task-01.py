import heapq
import timeit

available_coins = [50, 25, 10, 5, 2, 1]

def find_coins_greedy(value):
    result = {}
    finalvalue = 0
    coins = [-coin for coin in available_coins]
    heapq.heapify(coins)

    while finalvalue < value:
        coin = -coins[0]
        if finalvalue + coin <= value:
            finalvalue += coin
            result[coin] = result.get(coin, 0) + 1
        else:
            heapq.heappop(coins)

    return result

def find_min_coins(value):
    # формуємо початковий масив, для кожного значення від 0 до value
    min_coins = [float('inf')] * (value + 1)
    min_coins[0] = 0
    
    # тепер треба заповнити масив значенням мінімальної кількості монет для отримання такої суми
    for x in range(1, value + 1):
        for coin in available_coins:
            # якщо х >= coin, значить такою монетою можна отримувати цю суму
            if x >= coin:
                # prev = min_coins[x]

                # що менше
                # поточна мінімальна кількість монет 
                # чи кількість монет для суми без цієї монети, з але додаванням цієї моменти в кількість?
                # наприклад:
                # для x=9, навіть не важливо в якому порядку буде оброблюватись
                # coin: 1, min_coins[x - coin] = min_coins[8] = 3
                # coin: 5, min_coins[x - coin] = min_coins[4] = 2
                # отже 5 нам дозволяє зібрати швидше потрібну суму, тому на цьому етапі буде збереженне 2+1
                # і так від мінімальної суми до потрібної
                min_coins[x] = min(min_coins[x], min_coins[x - coin] + 1)

                # print(f"x: {x}, coin: {coin}, prev: {prev}, now: {min_coins[x]}, ")

    
    # збираємо результуючий словник
    result = {}
    while value > 0:
        for coin in available_coins:
            # якщо монета підходить для суми (не занадто велика)
            # та саме за рахунок неї формувалось мінімальне значення монет в таблиці
            if value >= coin and min_coins[value] == min_coins[value - coin] + 1:
                # тоді записуємо цю монету
                result[coin] = result.get(coin, 0) + 1
                # prev = value
                value -= coin

                # print(f"start: {prev}, finish: {value}, coin: {coin}, min_coins: {min_coins[value]}, min_coins_minus: {min_coins[value - coin]}")
                break
    
    return result


values = [222, 7777, 55555, 600_000]

def wrapper(func, value):
    func(value)

for value in values:
    execution_time = timeit.timeit(lambda: wrapper(find_coins_greedy, value), number=10)
    print(f"Час виконання find_coins_greedy: {execution_time:.5f}, значення {value}")

    execution_time = timeit.timeit(lambda: wrapper(find_min_coins, value), number=10)
    print(f"Час виконання find_min_coins: {execution_time:.5f}, значення {value}")
