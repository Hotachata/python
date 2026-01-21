import pandas as pd # type: ignore
pd.set_option('display.max_rows', 5)

wine_reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)
print(wine_reviews.shape)
# print(wine_reviews.head())
print(wine_reviews)