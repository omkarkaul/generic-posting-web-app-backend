# Generic Posting Web Application

This is the backend for the generic posting web app, written in Python with the Flask web mini-framework.

Dependencies:
- Python 3.7
- Flask
- PyMySQL

## DB Tables

#### 'posts' table
| Field     |    Type     | Null | Key | Default |
|-----------|-------------|------|-----|---------|
| post      | varchar(255)| NO   |PRI  | NULL    |
| timestamp | varchar(12) | NO   |     | NULL    |

```sql
CREATE TABLE posts ( post VARCHAR(255) NOT NULL PRIMARY KEY, timestamp VARCHAR(12) NOT NULL );
```


#### 'comments' table
| Field     |    Type     | Null | Key | Default |
|-----------|-------------|------|-----|---------|
| comment   | varchar(512)| NO   | PRI | NULL    |
| post_name | varchar(255)| NO   | MUL | NULL    |
| timestamp | varchar(12) | NO   |     | NULL    | 

```sql
CREATE TABLE comments ( comment VARCHAR(512) NOT NULL PRIMARY KEY, post_name VARCHAR(255) NOT NULL, timestamp VARCHAR(12) NOT NULL, FOREIGN KEY (post_name) REFERENCES posts(post));
```