



CREATE TABLE `movies` (
  `movieId` int(11) PRIMARY KEY AUTOINCREMENT,
  `name` varchar(45) NOT NULL,
  `category` varchar(45) NOT NULL,
  `durationInMinutes` int(11) NOT NULL,
  `description` varchar(255) NOT NULL,

