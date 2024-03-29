from pyspark.sql import SparkSession
from pyspark.sql.functions import explode

# В датафреймах (pyspark.sql.DataFrame) заданы продукты, категории и связь между ними. Одному продукту может
# соответствовать много категорий, в одной категории может быть много продуктов. Напишите метод с помощью PySpark,
# который вернет все продукты с их категориями (датафрейм с набором всех пар «Имя продукта – Имя категории»).
# В результирующем датафрейме должны также присутствовать продукты, у которых нет категорий.

# Создаём сессию Spark с именем ProductCategoryPairs, которая представляет собой точку входа для любых операций с
# данными в Spark:
spark = SparkSession.builder \
    .appName('ProductCategoryPairs') \
    .getOrCreate()

# Затем создаём 2 DF: 'products_df' с информацией о продуктах и 'categories_df' с информацией о категориях.
# Мы хотим объединить эти данные, чтобы получить пары 'Имя продукта - Имя категории', включая продукты без категорий.
# Определяем примеры данных для продуктов и категорий:
products_data = [('Apple', [1, 2]),
                 ('Banana', [2, 3]),
                 ('Bread', [1, 3, 4]),
                 ('Cucumber', [])]  # Информация о продуктах и их связанных категориях.

for product_tuple in products_data:
    if not product_tuple[1]:
        product_tuple[1].append(-1)

categories_data = [(1, 'Fruits'),
                   (2, 'Snacks'),
                   (3, 'Desserts'),
                   (4, 'Bakery')]  # Информация о категориях, с уникальным идентификатором и названием.

# Мы создаем 2 DF (для продуктов и категорий), используя метод createDataFrame.
products_df = spark.createDataFrame(products_data, ['product_name', 'category_ids'])
categories_df = spark.createDataFrame(categories_data, ['category_id', 'category_name'])

# Функция explode разбивает массив идентификаторов категорий на отдельные строки,
# чтобы у каждого продукта была одна категория на строку.
products_df = products_df.withColumn('category_id', explode(products_df['category_ids']))

# Мы объединяем DF продукта с DF категории по полю category_id (LEFT JOIN, что позволит нам также включить продукты без
# категорий) и выбираем нужные столбцы: название продукта и название категории.
product_category_pairs = products_df \
    .join(categories_df, 'category_id', 'left') \
    .select('product_name', 'category_name')

# Выводим результат в консоль.
product_category_pairs.show()

# Закрываем сессию Spark.
spark.stop()

"""
Разберём конкретно работу метода createDataFrame():
createDataFrame(data, schema=None): Этот метод создает новый DataFrame на основе данных из data и 
указанной схемы (schema). В случае, если схема не указана (как в нашем случае), Spark постарается самостоятельно 
определить схему на основе данных.

data: Данные, из которых будет создан DataFrame. В нашем случае это products_data и categories_data.
schema: Опционально. Схема данных, которая представляет собой список объектов StructField, где каждый объект описывает 
имя столбца и тип данных.

products_data и categories_data: Это данные, представленные в формате вложенных кортежей в список, которые будут 
использоваться для создания DataFrame.

"product_name" и "category_ids" для products_data, "category_id" и "category_name" для categories_data: 
Это имена столбцов в создаваемых DataFrame. Первый элемент кортежа будет соответствовать "product_name" или 
"category_id", а второй - "category_ids" или "category_name".

Таким образом, методы createDataFrame позволяют создавать DataFrame на основе предоставленных данных и указанных имен 
столбцов. Схема может быть задана явно, но в данном случае она инферируется из данных.

Инференция в данном контексте означает автоматическое определение или выведение чего-то на основе имеющихся данных или 
правил. В случае с созданием DataFrame в Apache Spark, инференция схемы данных означает автоматическое определение типов 
данных для каждого столбца на основе предоставленных данных.
Когда мы создаем DataFrame без явного указания схемы, Spark проходит по предоставленным данным, анализирует типы и 
значения в каждом столбце и на основе этого определяет соответствующие типы данных для каждого столбца. Например, если 
первый элемент списка имеет тип str, Spark задает тип "строка" для соответствующего столбца.

Инференция удобна, когда вы не знаете заранее точные типы данных или не хотите тратить время на явное их определение. 
Однако в некоторых случаях бывает полезно явно указывать схему данных для обеспечения точности и контроля над типами 
данных в DataFrame.
"""
