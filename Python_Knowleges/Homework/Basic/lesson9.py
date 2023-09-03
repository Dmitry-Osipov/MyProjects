import pandas as pd
import seaborn as sns
import random

df = pd.read_csv('sample_data/california_housing_train.csv')
df.head()  # Чтение начала списка (первые 5 строчек)
df.tail(n=20)  # Чтение последних 20 строчек
print(df.shape)  # Кортеж, состоящий из количества строк и столбцов
df.isnull()  # Выводит все строки, где есть хотя бы один None
df.isnull().sum()  # Сумма по столбцам со значениями None
print(df.dtypes)  # Выводит типы данных (для строки - object)
print(df.columns)  # Список названий всех столбцов
print(df.latitude)  # Выводит все строки для столбца latitude
print(df[['latitude', 'population']])  # Выводит все строки для столбцов latitude и population

# Задача: вывести столбец total_rooms, у которого медианный возраст здания (housing_median_age) меньше 20:
print(df[df['housing_median_age'] < 20])

# Задача: вывести столбец total_rooms, для которого 10 < housing_median_age < 20:
print(df[(df['housing_median_age'] < 20) & (df['housing_median_age'] > 10)].total_rooms)

# Задача: вывести столбец total_rooms и housing_median_age, для которых 10 < housing_median_age < 20:
print(df[(df['housing_median_age'] < 20) & (df['housing_median_age'] > 10)][['total_rooms', 'housing_median_age']])

print(df['population'].max())
print(df['population'].min())
print(df['population'].mean())
print(df['population'].sum())
print(df[['population', 'total_rooms']].median())  # Выведет среднее для каждого столбца
df.describe()  # Выведет всю простую статистику для каждого столбца

# Задача: изобразить точки долготы по отношению к ширине:
sns.scatterplot(data=df, x='longitude', y='latitude')

# Отношение, чем выше кол-во семей, тем выше кол-во людей и комнат:
sns.scatterplot(data=df, x='households', y='population', hue='total_rooms')

sns.scatterplot(data=df, x='households', y='population', hue='total_rooms', size=10)  # Указываем другой размер точек

# Мы можем визуализировать сразу несколько отношений, используя класс PairGrid. Он принимает аргумент DataFrame и
# визуализирует все возможные отношения между ними, в соотвествии с выбранным типом графика
cols = ['population', 'median_income', 'housing_median_age', 'median_house_value']
g = sns.PairGrid(df[cols])
g.map(sns.scatterplot)

sns.relplot(x='latitude', y='median_house_value', kind='line', data=df)  # Выведет линейный график

sns.scatterplot(data=df, x='latitude', y='longitude', hue='median_house_value')  # Выведение местоположения домов с
# закрашиванием точек по параметру стоимости дома

sns.histplot(data=df, x="median_income")  # Выведет гистограмму

sns.histplot(data=df[df['housing_median_age'] > 50], x="median_income")  # Задали условие по возрасту жителей

# Задача: разбить на возрастные группы и получитб среднее значение:
df.loc[df['housing_median_age'] <= 20, 'age_group'] = 'Молодые'
df.loc[(df['housing_median_age'] > 20) & (df['housing_median_age'] <= 50), 'age_group'] = 'Ср. возраст'
df.loc[df['housing_median_age'] > 50, 'age_group'] = 'Пожилые'
df.groupby('age_group')['median_income'].mean().plot(kind='bar')

# Задать 2 группы, вывести статистику в гистограмме
df.loc[df['median_income'] > 6, 'income_group'] = 'rich'
df.loc[df['median_income'] < 6, 'income_group'] = 'everyone_else'
sns.displot(df, x="median_house_value", hue="income_group")

# ----------------------------------------------------------------------------------------------------------------------

# Семинар.
# Прочесть с помощью pandas файл california_housing_test.csv, который находится в папке sample_data Посмотреть сколько в
# нем строк и столбцов Определить какой тип данных имеют столбцы

df = pd.read_csv('sample_data/california_housing_test.csv', encoding='utf-8')
df.head(n=10)
df.tail(n=10)
print(df.shape)  # 3000 - строки, 9 - столбцы
print(df.dtypes)  # Типы данных для столбцов, тип данных для строк будет object

# Проверить есть ли в файле пустые значения

df.isnull().sum()

# Показать median_house_value где median_income < 2

print(df[df['median_income'] < 2]['median_house_value'])

# Показать данные в первых 2 столбцах

for column in df.columns[:2]:
    print(column)

# Выбрать данные где housing_median_age < 20 и median_house_value > 70000

print(df[(df['median_house_value'] > 70000) & (df['housing_median_age'] < 20)])

# Определить какое максимальное и минимальное значение median_house_value

print(df.median_house_value.min(), df.median_house_value.max())

# Показать максимальное median_house_value, где median_income = 3.1250

df[(df['median_income'] == 3.1250)]['median_house_value'].max()

# Узнать какая максимальная population в зоне минимального значения median_house_value
df[(df.median_house_value == df.median_house_value.min())]['population'].max()

# Создаём новый столбец руками:
df['total_result'] = 0
print(df)

df.loc[df['median_income'] > 5, 'total_result'] = 'rich'
df.loc[(df['median_income'] >= 2) & (df['median_income'] <= 5), 'total_result'] = 'middle_class'
df.loc[df['median_income'] < 2, 'total_result'] = 'poor'
print(df)

df['total_new'] = df['households'].apply(lambda x: x / 100)
print(df)


# Более простой способ:


def func_add_new(cell_value):
    if cell_value < 200:
        result = 0
    elif 200 <= cell_value < 500:
        result = 1
    else:
        result = 2

    return result


df['total_new'] = df['households'].apply(func_add_new)
print(df)

# Изобразите отношение households к population с помощью точечного графика

sns.scatterplot(data=df, x='households', y='population')

# Визуализировать longitude по отношения к median_house_value, используя линейный график

sns.relplot(data=df, x='longitude', y='median_house_value', kind='line')

# Представить гистограмму по housing_median_age

sns.histplot(data=df, x='housing_median_age')

# Изобразить гистограмму по median_house_value с оттенком housing_median_age

sns.displot(data=df, x="median_house_value", hue="housing_median_age")

# Написать EDA для датасета про пингвинов
# Необходимо:
# Использовать 2-3 точечных графика. Применить доп измерение в точечных графиках, используя аргументы hue, size, stile

penguins = sns.load_dataset('penguins')
penguins.head()

sns.scatterplot(data=penguins, x='body_mass_g', y='sex')
sns.scatterplot(data=penguins, x='bill_length_mm', y='bill_depth_mm', hue='sex')
sns.scatterplot(data=penguins, x='flipper_length_mm', y='body_mass_g', hue='sex', style='sex')

# Использовать PairGrid с типом графика на ваш выбор

cols = ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']
g = sns.PairGrid(penguins[cols])
g.map(sns.scatterplot)

# Изобразить Heatmap

penguins.loc[penguins['bill_length_mm'] > 38, 'flipper_length_mm'] = 'big'
penguins.loc[penguins['bill_length_mm'] < 38, 'flipper_length_mm'] = 'small'
sns.displot(penguins, x="bill_length_mm", hue="flipper_length_mm")
sns.heatmap(data=penguins.corr(), cmap='coolwarm', annot=True)

# Использовать 2-3 гистограммы

sns.histplot(data=penguins, x='bill_length_mm')
sns.histplot(data=penguins, x='body_mass_g', hue='sex')


# Создать новый столбец в таблице с пингвинами, который будет отвечать за показатель длины клюва пингвина.
# high - длинный(от 42)
# middle - средний(от 35 до 42)
# low - маленький(до 35)

def func_add_new(cell_value):
    if cell_value < 35:
        result = 'low'
    elif 35 <= cell_value < 42:
        result = 'middle'
    else:
        result = 'high'

    return result


penguins['beak_length'] = penguins['bill_length_mm'].apply(func_add_new)
print(penguins)

# Изобразить гистограмму по flipper_length_mm с оттенком height_group. Сделать анализ

sns.histplot(data=penguins, x='flipper_length_mm', hue='beak_length')

# ----------------------------------------------------------------------------------------------------------------------
# Домашнее задание.
# Задача 40: Работать с файлом california_housing_train.csv, который находится в папке sample_data. Определить среднюю
# стоимость дома, где кол-во людей от 0 до 500 (population).

df = pd.read_csv('sample_data/california_housing_train.csv')
df[(df['population'] < 500)].median_house_value.mean()

# Задача 42: Узнать какая максимальная households в зоне минимального значения population.

df[(df.population == df.population.min())].households.max()  # 8232 строчка

# Задание 44
#
# В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. Ваша задача перевести его в
# one hot вид. Сможете ли вы это сделать без get_dummies?
# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI'lst})
# data.head()

# Без метода get_dummies():

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

unique_types = data['whoAmI'].unique()
print(unique_types)

one_hot_type = pd.DataFrame(columns=unique_types)

for item in unique_types:
    one_hot_type[item] = data['whoAmI'].apply(lambda x: 1 if x == item else 0)

result_data = pd.concat([data, one_hot_type], axis=1)

# С методом get_dummies():
lst1 = ['robot'] * 10
lst1 += ['human'] * 10
random.shuffle(lst1)
df = pd.DataFrame({'whoAmI1': lst1})
one_hot = pd.get_dummies(df['whoAmI1'])  # Применяем get_dummies для столбца 'whoAmI'
result_df = pd.concat([df, one_hot], axis=1)  # Объединяем исходный DataFrame с one-hot кодированными значениями
