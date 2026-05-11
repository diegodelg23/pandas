import pandas as pd
pd.set_option("display.max_rows", 5)
reviews = pd.read_csv("data/winemag-data-130k-v2.csv", index_col=0)

median_points = reviews.points.median()

countries = reviews.country.unique()

reviews_per_country = reviews.country.value_counts()

review_price_mean = reviews.price.mean()
centered_price = reviews.price.map(lambda p: p - review_price_mean)

bargain_idx = (reviews.points / reviews.price).idxmax()
bargain_wine = reviews.loc[bargain_idx, 'title']


n_tropical = reviews.description.map(lambda string: "tropical" in string).sum()
n_fruity = reviews.description.map(lambda string: "fruity" in string).sum()

descriptor_counts = pd.Series([n_tropical, n_fruity], index=['tropical', 'fruity'])

def star_rating_assign(row):
    if row.points >= 95 or row.country == 'Canada':
        return 3
    elif row.points >= 85 and row.points < 95:
        return 2
    else:
        return 1


star_ratings = reviews.apply(star_rating_assign, axis='columns')