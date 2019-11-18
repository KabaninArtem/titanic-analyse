import pandas as pd
import re

# 1. Какое количество мужчин и женщин ехало на корабле? В качестве ответа приведите два числа через пробел.
# 2. Какой части пассажиров удалось выжить? Посчитайте долю выживших пассажиров.
# 3. Какую долю пассажиры первого класса составляли среди всех пассажиров?
# 4. Какого возраста были пассажиры? Посчитайте среднее и медиану возраста пассажиров.
# 5. Коррелируют ли число братьев/сестер с числом родителей/детей?
# 6. Какое самое популярное женское имя на корабле? Извлеките из полного имени пассажира (колонка Name)

data = pd.read_csv('titanic.csv', index_col='PassengerId')
data['Pclass'] = data['Pclass'].astype(object)

sex = data['Sex'].value_counts()
survived_c = data['Survived'].value_counts()
survived_p = 100.0 * survived_c[1] / survived_c.sum()

pclass_c = data['Pclass'].value_counts()
first_class_p = 100.0 * pclass_c[1] / pclass_c.sum()

ages = data['Age'].dropna()
corr = data['SibSp'].corr(data['Parch'])


def clean_name(name):
    ln = re.search('^[^,]+, (.*)', name)
    if ln:
        name = ln.group(1)

    n = re.search('\(([^)]+)\)', name)
    if n:
        name = n.group(1)

    name = re.sub('(Miss\. |Mrs\. |Ms\. )', '', name)
    name = name.split(' ')[0].replace('"', '')
    return name


names = data[data['Sex'] == 'female']['Name'].map(clean_name)
name_counts = names.value_counts()

print(1, '{} {}'.format(sex['male'], sex['female']))
print(2, "{:0.2f}".format(survived_p))
print(3, "{:0.2f}".format(first_class_p))
print(4, "{:0.2f} {:0.2f}".format(ages.mean(), ages.median()))
print(5, "{:0.2f}".format(corr))
print(6, name_counts.head(1).index.values[0])
