import sqlparse

sql = "SELECT * FROM users WHERE age > 21;"
parsed_sql = sqlparse.parse(sql)
print(parsed_sql)
