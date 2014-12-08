import sqlite3

def create_table(db_name,table_name,sql):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor = cursor.execute("select name from sqlite_master where name=?",(table_name,))
        result = cursor.fetchall()
        keep_table = True
        if len(result) == 1:
            valid = False
            while not valid:
                response = input("The table {0} already exists, do you wish to recreate it? (y/n): ".format(table_name))
                response = response.lower()[0]
                if response == "y":
                    valid = True
                    keep_table = False
                    print("The {0} table willl be recreated, all existing data will be lost".format(table_name))
                    cursor.execute("drop table if exists {0}".format(table_name))
                    db.commit()
                elif response == "n":
                    valid = True
                    print("The existing table was kept")
                else:
                    Valid = False
                    print("Please select a valid option")
        else:
            keep_table = False
        if not keep_table:
            cursor.execute(sql)
            db.commit()
        
if __name__ == "__main__":
    db_name = "cineworld_kit_list.db"
    sql = """create table Kit_List
             (ItemID integer,
             Item text,
             Type text,
             Price real,
             Quantity integer,
             Total real,
             primary key(ItemID))"""
    create_table(db_name,"Kit_List",sql)