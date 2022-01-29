CREATE TABLE order_booking.`order_table` (
  order_id int primary key not null,
  `User_name` varchar(45) DEFAULT NULL,
  `Stock_name` varchar(45) DEFAULT NULL,
  `Order_quantity` int DEFAULT NULL,
  `Price` double DEFAULT NULL,
  `Order_date` datetime DEFAULT NULL
  
)
