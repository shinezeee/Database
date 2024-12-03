-- USE classicmodels;


-- (1) **`customers`** 테이블에 새 고객을 추가하세요.
INSERT INTO customers (customerNumber,customerName,phone,city,country)
VALUES (574,'Hyeji','+82 1044444444','Seoul','Korea');

-- (2) **`products`** 테이블에 새 제품을 추가하세요.
INSERT INTO products 
SET productCode='DB_1203', productName = '2024 OZ 08',buyPrice=100.99;

-- (3) **`employees`** 테이블에 새 직원을 추가하세요.
INSERT INTO employees
SET employeeNumber=0, lastName='Hyeji',firstName='Shin', email='shz0130@n.com';

-- (4) **`offices`** 테이블에 새 사무실을 추가하세요.
INSERT INTO offices
SET officeCode='DB_1203', city='Tokyo', phone='+81 111 2233', country='Japan';

-- (5) **`orders`** 테이블에 새 주문을 추가하세요.
INSERT INTO orders
SET orderNumber=57400,orderDate=date;

-- (6) **`orderdetails`** 테이블에 주문 상세 정보를 추가하세요.
INSERT INTO orderdetails
SET orderNumber=57400,productCode='DB_1203',quantityOrdered=3,priceEach=22.3,orderLineNumber=1;

-- (7) **`payments`** 테이블에 지불 정보를 추가하세요.
INSERT payments
SET 
-- (8) **`productlines`** 테이블에 제품 라인을 추가하세요.
INSERT INTO productlines

-- (9) **`customers`** 테이블에 다른 지역의 고객을 추가하세요.
INSERT INTO customers

-- (10) **`products`** 테이블에 다른 카테고리의 제품을 추가하세요.
INSERT INTO products