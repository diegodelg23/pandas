import pandas as pd
pd.set_option('display.max_columns', None)

# Your code goes here. Create a dataframe matching the above diagram and assign it to the variable fruits.
fruits = pd.DataFrame({'Apples': [30],
                       'Bananas': [21]})

# Check your answer
print(fruits)

fruit_sales = pd.DataFrame({'Apples': [35, 41],
                            'Bananas': [21, 34]},
                           index=['2017 Sales', '2018 Sales'])

print(fruit_sales)

ingredients = pd.Series(['4 cups', '1 cup', '2 large', '1 can'], index=['Flour', 'Milk', 'Eggs', 'Spam'], name='Dinner')

print(ingredients)

reviews = pd.read_csv("data/winemag-data_first150k.csv", index_col=0)

reviews.head()

animals = pd.DataFrame({'Cows': [12, 20], 'Goats': [22, 19]}, index=['Year 1', 'Year 2'])

animals.to_csv('data/cows_and_goats.csv')

# test