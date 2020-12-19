CREATE TABLE `reservations` (
  `reservationId` int(11) PRIMARY KEY AUTOINCREMENT,
  `isPaid` int(11) NOT NULL,
  `clientId` int(11) NOT NULL,
  `scheduleId` int(11) NOT NULL,
