import os
import sys
from sklearn import tree
import pandas as pd

# t = tree.DecisionTreeClassifier(criterion="entropy")
# t = t.fit(train_attributes, train_lables)
student_por = "/home/ziuteng/Python_AI_for_beginner/student-por.csv"
student_por_csv = "/home/ziuteng/Python_AI_for_beginner/student_por_test.csv"
student_por_csv_1 = "/home/ziuteng/Python_AI_for_beginner/student_por_test_1.csv"

def save_data_frame_to_csv(data_frame:pd.DataFrame, filename:str) ->None:
    data_frame.to_csv(filename)

def load_dataset(path_of_file: str):
    """load data set (ex student portuguese scores)
    using pandas
    Args:
        path_of_file (str): path of file need to load data
    Return:
        d: data set
    """
    d = pd.read_csv(path_of_file, sep=";")
    return d

def rule_decision_tree(d: pd.DataFrame):
    d['pass'] = d.apply(lambda row: 1 if (row['G1'] + row['G2'] + row['G3'] >= 35)  else 0, axis=1)
    d = d.drop(columns=['G1', 'G2', 'G3'], axis =1) # using drop to remove column have tag G1, G2 and G3 with syntax look like this
    print(d.head(10))
    # print(d)

if __name__ == "__main__":
    d = load_dataset(student_por)
    # print(d)
    save_data_frame_to_csv(d, student_por_csv)
    rule_decision_tree(d)
    save_data_frame_to_csv(d, student_por_csv_1)
