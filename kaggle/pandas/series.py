import pandas as pd # type: ignore

sr = pd.Series([30, 35, 40], 
               index=['2015 Sales', '2016 Sales', '2017 Sales'], 
               name='Product A')
print("\nIt's helpful to think of a DataFrame as actually being just a bunch of Series \"glued together\"\n")
print(sr)

ingredients = pd.Series(['4 cups', '1 cup', '2 large', '1 can'],
                       index = ['Flour', 'Milk', 'Eggs', 'Spam'],
                       name = 'Dinner')
print(ingredients)