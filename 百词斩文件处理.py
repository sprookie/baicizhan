import sqlite3
import pandas as pd
connet = sqlite3.connect("baicizhandoexampleinfo.db")
words = pd.read_sql_query("SELECT * FROM tb_collect_words", connet)
# print(words.head())

words_new = words.iloc[:, 1:4]
words_new.to_csv('words.csv')
