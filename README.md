# alx-backend-storage
ALX Backend Storage is a simple Flask web application that provides a RESTful API for file storage and retrieval. It allows users to upload, download, and delete files using HTTP requests.

## Installation
- Clone the repository:
```
git clone https://github.com/queensk/alx-backend-storage.git
```
- Navigate to the project directory:
```
cd alx-backend-storage
```
## Usage
Once the application is running, you can interact with it using HTTP requests. The following endpoints are available:

```
$ service mysql start
 * MySQL Community Server 5.7.30 is started
$
$ cat 0-list_databases.sql | mysql -uroot -p my_database
Enter password: 
Database
information_schema
mysql
performance_schema
sys
$
```

## Configuration
How to import a SQL dump:

```
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password: 
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
$
```

Please make sure to update tests as appropriate.

## License
[MIT](./LICENSE)