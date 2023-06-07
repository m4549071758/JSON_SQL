import json
import mysql.connector

# JSONファイルのパス
json_file_path = ["", ""]

# MySQL接続情報
mysql_host = ""
mysql_user = ""
mysql_password = ""
mysql_database = ""
mysql_port = ""

# MySQLに接続
db = mysql.connector.connect(
    host=mysql_host,
    user=mysql_user,
    password=mysql_password,
    database=mysql_database,
    port=mysql_port
)
cursor = db.cursor()

# JSONファイルを読み込む
for path in json_file_path:
    with open(path, 'r') as f:
        stream = f.readlines()
        for raw_data in stream:
            data = json.loads(raw_data)
            
            time = data["time"].replace("T", " ").strip("+09:00")
            client = data["client"]

            # MySQLに挿入するクエリを作成
            query = "INSERT INTO TABLENAME (columns, columns) VALUES (%s, %s)"
            values = (0, time, client)
            cursor.execute(query, values)
# 変更をコミットして接続を閉じる
db.commit()
cursor.close()
db.close()
