Create Table order_booking.userorder_details(
username varchar(45) not null,
order_id int ,
foreign key (order_id) references order_booking.order_table(order_id)
);

