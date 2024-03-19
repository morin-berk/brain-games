[![Maintainability](https://api.codeclimate.com/v1/badges/eab001b350e401ee7e57/maintainability)](https://codeclimate.com/github/morin-berk/brain-games/maintainability)

[![Actions Status](https://github.com/morin-berk/brain-games/workflows/hexlet-check/badge.svg)](https://github.com/morin-berk/brain-games/actions)

«Игры разума» — набор из пяти консольных игр, построенных по принципу популярных мобильных приложений для прокачки мозга. Каждая игра задает вопросы, на которые нужно дать правильные ответы. После трех правильных ответов считается, что игра пройдена. Неправильные ответы завершают игру и предлагают пройти ее заново. Игры:

- brain-calc. Арифметические выражения, которые необходимо вычислить
- brain-progression. Поиск пропущенных чисел в последовательности чисел
- brain-even. Определение четного числа
- brain-gcd. Определение наибольшего общего делителя
- brain-prime. Определение простого числа

## Минимальные требования
- Python > 3.6
- pip > 19.0
- Poetry > 1.2.0

## Установка и запуск
1. Склонируйте репозиторий локально.
2. Установите зависимости командой `make install`.
3. Запуск игр производится командой `make {game_name}`. Например, `make brain-even`. 
4. Чтобы выйти из игры, нажмите Ctrl + Z. 

## Примеры партий игр

Example of a brain-even session:
[![asciicast](https://asciinema.org/a/MYh0w0OS89fLj4S9xaHDf5GpX.svg)](https://asciinema.org/a/MYh0w0OS89fLj4S9xaHDf5GpX)

Example of a brain-calc session: 
[![asciicast](https://asciinema.org/a/Pbnj3n6dVwQgVToVzPCKhoODz.svg)](https://asciinema.org/a/Pbnj3n6dVwQgVToVzPCKhoODz)

Example of a brain-gcd session:
[![asciicast](https://asciinema.org/a/6lfus66SvJ7IkQ7GywETZY0EJ.svg)](https://asciinema.org/a/6lfus66SvJ7IkQ7GywETZY0EJ)

Example of a brain-progression session:
[![asciicast](https://asciinema.org/a/8YZdHmoAetAEpSTZL5L2gW66D.svg)](https://asciinema.org/a/8YZdHmoAetAEpSTZL5L2gW66D)

Example of a brain-prime session:
[![asciicast](https://asciinema.org/a/m2dWCQtRirPyAKqA0P98a8P7w.svg)](https://asciinema.org/a/m2dWCQtRirPyAKqA0P98a8P7w)
