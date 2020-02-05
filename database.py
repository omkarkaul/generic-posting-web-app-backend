import pymysql

class Database:
    def __init__(self):
        host = '127.0.0.1'
        user = 'root'
        password = ''
        db = 'beating_chester'

        self.con = pymysql.connect(host, user, password, db, cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.con.cursor()
    
    def get_all_posts(self):
        self.cur.execute("SELECT * FROM posts")
        result = self.cur.fetchall()

        return result
    
    def get_comments_for_post(self, post):
        self.cur.execute(f"SELECT comment FROM comments WHERE post_name = {post}")
        result = self.cur.fetchall()

        return result