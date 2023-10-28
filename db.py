import sqlite3

class DB:
    #Schema phone_number, session_string, password(if exist)
    def __init__(self):
        self.con = sqlite3.connect("accounts.sqlite3")
        self.c = self.con.cursor()
        self._check_table()
    
    def _check_table(self):
        self.c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='accounts'")
        tables = self.c.fetchone()
        if tables is None:
            self._create_table()
    
    def _create_table(self):
        self.c.execute("CREATE TABLE accounts (phone_number text,session_string text,password text)")
        self.con.commit()

    def check_exist(self, phone_number):
        self.c.execute("SELECT * FROM accounts")
        items = self.c.fetchall()
        for item in items:
            if phone_number == item[0]:
                return True
        return False
    
    def add_account(self, phone_number, session_string, password=""):
        if not self.check_exist(phone_number):
            self.c.execute("INSERT INTO VALUES (?,?,?)", [phone_number, session_string, password])
            self.con.commit()
            return True
        else:
            return False
    
    def delete_account(self, phone_number):
        if self.check_exist(phone_number):
            self.c.execute("DELETE FROM accounts WHERE phone_number=(?)", [phone_number])
            self.con.commit()
            return True
        else:
            return False

