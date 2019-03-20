import pandas 
import matplotlib.pyplot as graph
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

# Constants
FILE_DIRECTORY = 'csv'
FILE_NAME = 'labs.csv'

# Reading the file
data = pandas.read_csv(FILE_DIRECTORY + '/' + FILE_NAME)
train_data = data[['URXUMA','URDACT']]
clean_train_data = train_data.dropna(thresh=2)

# regression between URXUMA and URDACT
regression_model = make_pipeline(PolynomialFeatures(2), Ridge())
regression_model.fit(clean_train_data[['URXUMA']],clean_train_data[['URDACT']])

graph.xlabel("URXUMA")
graph.ylabel("URDACT")
graph.scatter(clean_train_data.URXUMA,clean_train_data.URDACT,
              s=30, alpha=0.15, marker='o')
graph.plot(clean_train_data.URXUMA,
           regression_model.predict(clean_train_data[['URXUMA']]),
           'ro', alpha=0.15)
graph.show()
