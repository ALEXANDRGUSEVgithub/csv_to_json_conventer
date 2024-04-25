# Конвертер CSV в JSON

Простой конвертер, который преобразует данные из CSV файла в формат JSON. Этот скрипт принимает CSV файл, в котором данные разделены запятыми, и преобразует его в JSON файл с удобным форматированием.

## Зависимости

Python 3

## Использование

1. Установите Python, если у вас его нет.
2. Подготовьте CSV файл с данными, которые вы хотите преобразовать. Убедитесь, что данные в CSV файле имеют формат как в этом примере, а название файла mbl_players.csv:

```csv
"Name","Team","Height(inches)","Weight(ibs)","Age"
"Alexandr","A","70","190 ","31.1"
"Ivan","B","67 ","",""
"Oleg","A ","54","210","43.5"
" Vladimir   ","D","","200","27.9"
" Dmitry  ","A"," 55 "," 195","18.7"
```

Обратите внимание, что значения разделены запятыми. В некоторых строчках пропущены значения или добавлены
лишние пробелы это необходимо для тестирования функционала.

3. Запустите скрипт.
4. После выполнения скрипта будет создан JSON файл с преобразованными данными.

## Пояснения к коду

- `convert_inches_to_sm`: Функция для преобразования высоты из дюймов в сантиметры.
- `convert_ibs_to_kg`: Функция для преобразования веса из фунтов в килограммы.
- `csv_to_json`: Основная функция, которая читает данные из CSV файла, преобразует их в нужный формат и сохраняет в JSON файл.
- Внутри `csv_to_json` функции:
- Сначала данные читаются из CSV файла с использованием модуля `csv`.
- Затем каждая строка данных преобразуется в словарь ключ-значение.
- Удаляются строки в который отсутствует хотя бы одно значение.
- Удаляются пробелы и' " ' в ключах и значениях.
- Удаляется ключ "Team" и все связанные с ним значения.
- Высота преобразуется из дюймов в сантиметры и строка переименовывается из 'Height(inches)' в 'Height'.
- Вес преобразуется из фунтов в килограммы и строка переименовывается из 'Weight(lbs)' в 'Weight'.
- Возраст преобразуется в целое число.
- После этого данные сохраняются в JSON файл с помощью модуля `json`.


## Результат работы
```json
[
 {
  "Name": "Alexandr",
  "Age": 31,
  "Height": 178,
  "Weight": 86
 },
 {
  "Name": "Oleg",
  "Age": 43,
  "Height": 137,
  "Weight": 95
 },
 {
  "Name": "Dmitry",
  "Age": 18,
  "Height": 140,
  "Weight": 88
 }
]
```
