import sqlite3

conn = sqlite3.connect('Asset/tmp.db', check_same_thread=False)

def create_table():
    conn.execute("""CREATE TABLE IF NOT EXISTS tweet_cleaning (id INTEGER PRIMARY KEY AUTOINCREMENT, previous_tweet char(1000), cleaned_new_tweet char(1000))""")
    conn.commit()

def insert_to_table(value_1,value_2):
    value_1 = value_1.encode('utf-8')
    value_2 = value_2.encode('utf-8')
    query = f"INSERT INTO tweet_cleaning (previous_tweet, cleaned_new_tweet) VALUES (?, ?);"
    conn.execute(query, (value_1, value_2))
    conn.commit()
   

def read_table(target_index=None,table_name=None):
    if target_index == None:
        results = conn.execute(f'select previous_tweet, cleaned_new_tweet FROM {table_name};')
        results = [(result[0].decode('utf-8'), result[1].decode('utf-8')) for result in results]
        return results
    else:
        results = conn.execute(f'select previous_tweet, cleaned_new_tweet FROM {table_name} WHERE id = {target_index};')
        results = [(result[0].decode('utf-8'), result[1].decode('utf-8')) for result in results]
        return results[0]