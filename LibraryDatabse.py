import mysql.connector

class Database:
    conn = mysql.connector.connect(
    host = "localhost",
    user= "root",
    password = "Mysql0109@",
    database = "Library")
    crsr = conn.cursor()
    table = input("Enter the table name to manipulate : ")
    print("Connected to databse")
    def createTable(self):
        table = self.table
        sql = f"""CREATE TABLE IF NOT EXISTS {table} (id INT PRIMARY KEY NOT NULL, 
                    subscriber_id INTEGER,
                    book_id INTEGER,
                    borrowed_date TEXT,
                    return_date TEXT,
                    FOREIGN KEY (subscriber_id) REFERENCES Subscriber(id),
                    FOREIGN KEY (book_id) REFERENCES Books(id));"""
        self.crsr.execute(sql)
        self.conn.commit()
    def insertData(self):
        table = self.table
        sql = f"INSERT INTO {table}(id , BookName , AuthorName,ISBN) VALUES (?,?, ?, ?)"
        values = (2,"C++","Bjarne Straoustrap","1234567890")
        self.crsr.execute(sql , values)
        self.conn.commit()
    def readData(self):
        table = self.table
        read = f"SELECT * FROM {table}"
        self.crsr.execute(read)
        rows = self.crsr.fetchall()
        print(rows)
    def tableStructure(self):
        self.crsr.execute(f"DESCRIBE {self.table}")
        table_schema = self.crsr.fetchall()
        print("Column Name".center(10),"|","Data Type".center(10),"| Nullable".center(10),"| Default Value".center(10), "| Primary Key".center(10))
        for column in table_schema:
            col_name = column[1].center(10)
            dataType = column[2].center(7)
            is_nullable =str(column[3]).center(5)
            default_value = str(column[4]).center(10)
            primary_key = "Yes" if column[5]==1 else "No"
            print(f"{col_name}\t{dataType}\t{is_nullable}\t{default_value}\t\t{primary_key.center(10)}")
            print()
    def dropTable(self):
        sql = f"DROP TABLE IF EXISTS {self.table}"
        self.crsr.execute(sql)
        self.conn.commit()
    def addColumns(self):
        columns = input("Enter column name and data type seperated with space : ").split()
        for i in range(0,len(columns),2):
            print(columns[i],columns[i+1])
            sql = f"ALTER TABLE {self.table} ADD COLUMN {columns[i]} {columns[i+1]}"
            self.crsr.execute(sql)
        self.conn.commit()
    def dropDatabase(self):
        sql = f"SELECT name FROM sqlite_master WHERE type='table'"
        self.crsr.execute(sql)
        tables = self.crsr.fetchall()
        print(tables)
    
db = Database()
#db.createTable()
db.tableStructure()
#db.dropTable()
#db.tableStructure()
#db.dropDatabase()
