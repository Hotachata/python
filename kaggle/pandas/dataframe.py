import pandas as pd # type: ignore
pd.set_option('display.max_rows', 5)

df = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])
print(df)

fruits = pd.DataFrame({"Apples": [30], "Bananas": [21]})
print(fruits)

fruit_sales = pd.DataFrame({"Apples": [35, 41],
                           "Bananas": [21, 34]},
                          index=["2017 Sales", "2018 Sales"])
print(fruit_sales)

#* fruits.to_csv("fruit_sales.csv")