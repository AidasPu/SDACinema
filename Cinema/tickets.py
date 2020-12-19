CREATE TABLE `tickets` (
  `ticketId` int(11) PRIMARY KEY AUTOINCREMENT,
  `scheduleId` int(11) NOT NULL,
  `seatId` int(11) NOT NULL,
  `categoryId` int(11) NOT NULL,