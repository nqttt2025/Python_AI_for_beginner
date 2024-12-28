############################# hàm head() trong data frame pandas #############################
import pandas
<!-- create data frame basic -->
data = {'name': ['Alice', 'Bob', 'Charlie],
        'age': [25, 30, 35]}
df = pd.DataFrame(data)
<!-- display specified number of rows, string from the top, default 5 rows if number is not specified -->
print(df.head(8)) #display 8 rows from the first
<!-- summarise: dataframe.head() is a convenient method to quickly check the values in a DataFrame, allowing you easiy inspect its structure and content.
by default, it displays the first five rows, helping you verify the data format and understand the dataset at a glance. -->
############################# hàm head() trong data frame pandas #############################


############################# function get_dummies() trong data frame pandas #############################



############################# function get_dummies() trong data frame pandas #############################

sudo apt install python3-pydot graphviz