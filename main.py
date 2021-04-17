

from load_data import data , data_t
from recommender import algo


algo.fit(data)

prediction = algo.predict('E', 2)
print(prediction)
#print(prediction.est)

prediction = algo.test(data_t)

print(prediction)
print(prediction.est)
