# 유저 10명 생성 
INSERT INTO Users (first_name, last_name, email, password, address, contact, gender)
VALUES
  ('John', 'Doe', 'john.doe@example.com', 'password123', '1234 Elm Street, Springfield', '555-1234', 'MALE'),
  ('Jane', 'Smith', 'jane.smith@example.com', 'password123', '5678 Oak Avenue, Springfield', '555-5678', 'FEMALE'),
  ('Alice', 'Johnson', 'alice.johnson@example.com', 'password123', '9101 Pine Road, Springfield', '555-9101', 'FEMALE'),
  ('Bob', 'Brown', 'bob.brown@example.com', 'password123', '1122 Maple Drive, Springfield', '555-1122', 'MALE'),
  ('Charlie', 'Davis', 'charlie.davis@example.com', 'password123', '3344 Birch Lane, Springfield', '555-3344', 'MALE'),
  ('David', 'Martinez', 'david.martinez@example.com', 'password123', '5566 Cedar Boulevard, Springfield', '555-5566', 'MALE'),
  ('Emily', 'Gonzalez', 'emily.gonzalez@example.com', 'password123', '7788 Fir Circle, Springfield', '555-7788', 'FEMALE'),
  ('Frank', 'Wilson', 'frank.wilson@example.com', 'password123', '9900 Redwood Way, Springfield', '555-9900', 'MALE'),
  ('Grace', 'Lee', 'grace.lee@example.com', 'password123', '1234 Willow Road, Springfield', '555-1234', 'FEMALE'),
  ('Henry', 'Perez', 'henry.perez@example.com', 'password123', '5678 Pine Street, Springfield', '555-5678', 'MALE');


# 재고변동이력 10개 생성 #
INSERT INTO stocks (raw_material_id, pre_quantity, quantity, change_type, store_id, create_at) 
VALUES
(1, 100, 20, 'IN', 1,now()),
    (2, 50, 30, 'OUt', 2,now()),
    (3, 200, 100, 'OUT', 3,now()),
    (4, 60, 20, 'IN', 4,now()),
    (5, 10, 50, 'IN', 5,now()),
    (6, 40, 10, 'DISCARDED', 6,now()),
    (7, 30, 20, 'IN', 7,now()),
    (8, 100, 90, 'OUT', 8,now()),
    (9, 40, 50, 'IN', 9,now()),
    (10, 60, 10, 'RETURNED', 10,now());
    
# sales_items 데이터 추가 #
INSERT INTO sales_items (sales_record_id, product_id, quantity)
VALUES (1, 1, 3)
 
# product 시그니처 메뉴 추가 #
INSERT INTO products (name, description, price)
VALUES ('HJ fish', "HJ's signature fishbread", 6.99);

# user1,user2를 각매장 id 5,7에  직원,매니저로 변경 #
UPDATE employees
SET type = "STAFF" , store_id =5
WHERE user_id =1;

UPDATE employees
SET type = "MANAGER" , store_id =7
WHERE user_id =2;