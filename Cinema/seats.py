CREATE TABLE `seats` (
  `seatId` int(11) PRIMARY KEY AUTOINCREMENT,
  `row` int(11) NOT NULL,
  `number` int(11) NOT NULL,
  `roomId` int(11) NOT NULL,