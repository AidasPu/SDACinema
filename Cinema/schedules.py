CREATE TABLE `schedules` (
  `scheduleId` int(11) PRIMARY KEY AUTOINCREMENT,
  `startTime` datetime NOT NULL,
  `movieId` int(11) NOT NULL,
  `roomId` int(11) NOT NULL,