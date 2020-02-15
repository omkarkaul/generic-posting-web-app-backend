# Generic Posting Web Application

This is the backend for the generic posting web app, written in Python with the Flask web mini-framework.

Dependencies:
- Python 3.7
- Flask
- PyMySQL

## DB Tables

#### 'Posts' table (SQL: DESCRIBE posts;)
| Field     |    Type     | Null | Key | Default |
|-----------|-------------|------|-----|---------|
| post      | varchar(255)| NO   |PRI  | NULL    |
| timestamp | varchar(12) | NO   |     | NULL    | 

#### 'Comments table (SQL: DESCRIBE comments;)
| Field     |    Type     | Null | Key | Default |
|-----------|-------------|------|-----|---------|
| comment   | varchar(512)| NO   | PRI | NULL    |
| post_name | varchar(255)| NO   | MUL | NULL    |
| timestamp | varchar(12) | NO   |     | NULL    | 