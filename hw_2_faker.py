import sqlite3
from faker import Faker

db = 'hw_2.db'


def create_tb_persons():
    con = sqlite3.connect(db)
    cur = con.cursor()
    sql = '''
    CREATE TABLE IF NOT EXISTS persons(
    presonid INTEGER NOT Null PRIMARY KEY,
    first_name varchar(128),
    last_name varchar(128),
    Address varchar(1024),
    job varchar(128),
    Age INREGER 
    )
    '''
    cur.execute(sql)
    con.close()

def ins_data():
    fake = Faker(['en_US'])
    for _ in range(10):
        f_n = fake.first_name()
        l_n = fake.last_name()
        job = fake.job()
        adr = fake.address()
        age = fake.random_int(18, 60)
        con = sqlite3.connect(db)
        cur = con.cursor()
        sql = f'''   
            INSERT INTO persons (first_name, last_name, Address, job, Age)
            VALUES       
                ('{f_n}', '{l_n}','{job}', '{adr}', '{age}')
                
        '''
        cur.execute(sql)
        con.commit()
    con.close()

def prn_persons_by_age():
    con = sqlite3.connect(db)
    cur = con.cursor()
    sql = 'SELECT  Age,  first_name, last_name, Address, job, presonid FROM persons ORDER BY Age DESC'
    for row in cur.execute(sql):
        print(row)
    con.close()

def update_persons():
    con = sqlite3.connect(db)
    cur = con.cursor()
    sql = '''   
    UPDATE persons
    SET  last_name = 'Adams'
    WHERE Age <= 30
    '''
    cur.execute(sql)
    con.commit()
    con.close()

def del_person():
    con = sqlite3.connect(db)
    cur = con.cursor()
    sql = "DELETE FROM persons WHERE first_name = 'David'"
    cur.execute(sql)
    con.commit()
    con.close()

if __name__ == '__main__':
    create_tb_persons()
    ins_data()
    del_person()
    update_persons()
    prn_persons_by_age()

