CREATE TABLE `rooms` (
  `roomId` int(11) PRIMARY KEY AUTOINCREMENT,
  `number` int(11) NOT NULL,
  `maxSeats` int(11) NOT NULL,
  `location` varchar(45) DEFAULT NULL,

