CREATE TABLE LoginTable (
    UserId INT PRIMARY KEY,
    UserName VARCHAR(20),
    AccessType INT
);

CREATE TABLE OrderTable (
    UserName VARCHAR(20),
    StockName VARCHAR(20),
    order_quantity INT,
    price INT, 
    order_date DATE
);

CREATE TABLE TransactionTable (
    TransId INT PRIMARY KEY,
    Price INT,
    Quantity INT,
    TypeOfTransaction INT,
    StatusOfTransaction INT,
    DateOfTransaction DATE
);

CREATE TABLE UserOrderDetails (
    UserId INT,
    UserName VARCHAR(20),
    orderid INT,
    PRIMARY KEY(UserId, OrderId)
);