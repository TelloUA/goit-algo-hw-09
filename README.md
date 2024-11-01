# Висновки:

- Час виконання find_coins_greedy: 0.00002, значення 222
- Час виконання find_min_coins: 0.00150, значення 222
- Час виконання find_coins_greedy: 0.00014, значення 7777
- Час виконання find_min_coins: 0.06412, значення 7777
- Час виконання find_coins_greedy: 0.00102, значення 55555
- Час виконання find_min_coins: 0.45440, значення 55555
- Час виконання find_coins_greedy: 0.01127, значення 600000
- Час виконання find_min_coins: 5.03179, значення 600000

Жадібний алгоритм в цьому випадку працює набагато швидше, оскільки він бере завжди максимальну моменту, поки вона його влаштовує. Для поточного випадку функція майже не перебудовує купу, і основна кількість ітерації буде O(value/max_coin). Загалом для найкращого випадку поточний жадібний алгоритм має O(1), а в найгрішому O(value), враховуючи що available_coins не містить велику кількість значень.

Для динамічного програмування у нас завжди O(value), що в найгіршому випадку, що в найкращому, оскільки які б монети не були, ми завжди проходимо по повному усюму циклу, щоб побудувати таблицю з мінімальними значеннями. І це теж враховуючи що available_coins не містить велику кількість значень.

Конкретно в цій задачі, логіка динамічного програмування виглядає надлишковою, що як раз видно і по теоритичній частині, і по фактичним підрахункам.