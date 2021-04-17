
import pandas as pd
from surprise import Dataset
from surprise import Reader
from surprise.model_selection import train_test_split
# This is the same data that was plotted for similarity earlier
# with one new user "E" who has rated only movie 1
ratings_dict = {
    "item": [1, 2, 1, 2, 1, 2, 1, 2, 1 , 3],
    "user": ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'E' , 'A'],
    "rating": [1, 2, 2, 4, 2.5, 4, 4.5, 5, 3 , 4],
}
ratings_dict_t= {
    "item": [3],
    "user": ['A'],
    "rating": [1],
}


df = pd.DataFrame(ratings_dict)
reader = Reader(rating_scale=(1, 5))
# Loads Pandas dataframe
data = Dataset.load_from_df(df[["user", "item", "rating"]], reader)
data_tr , data_t=train_test_split(data, test_size=0.2)


# Loads the builtin Movielens-100k data
movielens = Dataset.load_builtin('ml-100k')
