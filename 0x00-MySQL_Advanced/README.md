# 0x00-MySQL_Advanced
This repository contains solutions to advanced MySQL problems for the ALX Software Engineering program.

## Topics Covered
Some of the topics covered in this project include:

- Indexing
- Query Optimization
- Full-text search
- Stored procedures
- Triggers
- Views
- Transactions
- Replication

## Requirements
- MySQL Server
- MySQL Client

## Usage
1. Clone the repository:
```
git clone https://github.com/<username>/0x00-MySQL_Advanced.git
```
2. Connect to a MySQL server:
```
mysql -h <hostname> -u <username> -p
```
3. Create a new database:
```
CREATE DATABASE <database_name>;
```
4. Import the schema and data:
```
USE <database_name>;
SOURCE path/to/schema.sql;
SOURCE path/to/data.sql;
```
5. Run the queries in the queries directory:
```
USE <database_name>;
SOURCE path/to/queries/<filename>.sql;
```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](../LICENSE)