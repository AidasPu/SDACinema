from Cinema import DatabaseContextManager, DB_NAME



CREATE TABLE clients (
  clientId int(11) PRIMARY KEY AUTOINCREMENT,
  firstName varchar(45) NOT NULL,
  lastName varchar(45) NOT NULL,
  email varchar(45) NOT NULL,
  dateOfBirth date NOT NULL,

