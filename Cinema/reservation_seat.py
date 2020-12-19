CREATE TABLE `reservation_seat` (
  `reservationSeatId` int(11) PRIMARY KEY AUTOINCREMENT,
  `reservationId` int(11) NOT NULL,
  `seatId` int(11) NOT NULL,
FOREIGN KEY (reservationId) REFERENCES reservations (reservationId) ON DELETE NO ACTION ON UPDATE NO ACTION,
FOREIGN KEY (seatId) REFERENCES seats (seatId) ON DELETE NO ACTION ON UPDATE NO ACTION
