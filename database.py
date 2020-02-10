import pymysql
import time

class Database:
    def __init__(self):
        host = '127.0.0.1'
        user = 'root'
        password = ''
        db = 'beating_chester'

        self.con = pymysql.connect(host, user, password, db, cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.con.cursor()
    
    def get_all_posts(self):
        self.cur.execute("SELECT * FROM posts ORDER BY timestamp DESC")
        result = self.cur.fetchall()

        return result
    
    def get_comments_for_post(self, post):
        self.cur.execute(f"SELECT comment, timestamp FROM comments WHERE post_name = '{post}' ORDER BY timestamp ASC")
        result = self.cur.fetchall()

        return result

    def add_new_post(self, post):
        try:
            timestamp = int(time.time())
            self.cur.execute(f"INSERT INTO posts (value, timestamp) values ('{post}', '{timestamp}')")
            self.con.commit() # required for committing the query to the db

            return 1 # Successfully posted {post} into the database!
        except pymysql.MySQLError as e:
            if e.args[0] == 1062:
                print('Duplicate entry!')
                return 2

    def add_new_comment(self, post, comment):
        try:
            timestamp = int(time.time())
            self.cur.execute(f"INSERT INTO comments (comment, post_name, timestamp) values ('{comment}', '{post}', '{timestamp}')")
            self.con.commit() # required for committing the query to the db

            return 1

        except pymysql.MySQLError as e:
            if e.args[0] == 1452:
                print("Provided post_name doesn't exist!")
                return 2