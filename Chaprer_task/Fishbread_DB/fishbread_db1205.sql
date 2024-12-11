USE fishbread_db;

CREATE TABLE Users (
	id INT AUTO_INCREMENT PRIMARY KEY, -- 사용자 인덱스 
    first_name VARCHAR(50), -- 이름 
    last_name VARCHAR(50), -- 성 
    email VARCHAR(50) NOT NULL UNIQUE, -- 이메일
	password VARCHAR(255) NOT NULL, -- 비밀번호
	address VARCHAR(255), -- 주소
	contact VARCHAR(50), -- 전화번호
	gender ENUM('MALE', 'FEMALE') NOT NULL, -- 성별
	is_active BOOLEAN NOT NULL DEFAULT TRUE, -- 활성화된 계정인지 확인하는 컬럼
	is_staff BOOLEAN NOT NULL DEFAULT FALSE -- 직원인지 확인하는 컬럼
);

CREATE TABLE stores(
	id INT AUTO_INCREMENT PRIMARY KEY, -- 인덱싱
	name VARCHAR(50) NOT NULL, -- 가맹점 이름
	address VARCHAR(255), -- 주소
	contact VARCHAR(50), -- 전화번호
	is_active BOOLEAN NOT NULL DEFAULT TRUE -- 활성화된 상점인지 확인하는 컬럼
);

CREATE TABLE employees(
	id INT AUTO_INCREMENT PRIMARY KEY, -- 인덱싱
	code INT NOT NULL UNIQUE, -- 사원 번호
	type ENUM('STAFF', 'MANAGER') NOT NULL, -- 직급
	user_id INT, -- users 테이블의 id
	store_id INT, -- stores 테이블의 id
	is_active BOOLEAN NOT NULL DEFAULT TRUE, -- 활성화된 계정인지 확인하는 컬럼
	FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE, 
	FOREIGN KEY (store_id) REFERENCES stores(id) ON DELETE CASCADE
);

CREATE TABLE suppliers(
	id INT AUTO_INCREMENT PRIMARY KEY, -- 인덱싱
	name VARCHAR(50) NOt NULL, -- 공급업체 이름
	address VARCHAR(255), -- 주소
	contact VARCHAR(50), -- 전화번호
	is_active BOOLEAN NOT NULL DEFAULT TRUE -- 활성화된 공급처인지 확인하는 컬럼
);

CREATE TABLE raw_materials (
	id INT AUTO_INCREMENT PRIMARY KEY, -- 인덱싱
	name VARCHAR(50) NOT NULL, -- 원재료 이름
	price DECIMAL(10, 2) NOT NULL -- 원재료 가격
);

CREATE TABLE products(
	id INT AUTO_INCREMENT PRIMARY KEY, -- 상품 고유번호
	name VARCHAR(50) NOT NULL, -- 상품 이름
	description TEXT, -- 상품 설명
	price DECIMAL(7, 2) NOT NULL -- 상품 가격
);

CREATE TABLE stocks (
id INT AUTO_INCREMENT PRIMARY KEY, -- 인덱싱
	raw_material_id INT NOT NULL, -- 원재료 id
	pre_quantity INT NOT NULL, -- 이전 재고
	quantity INT NOT NULL, -- 수량
	change_type ENUM('IN', 'OUT', 'RETURNED', 'DISCARDED'), -- 입고(IN) 출고(OUT) 반품(RETURNED) 폐기(DISCARDED)
	store_id INT NOT NULL, -- stors 테이블의 id
	create_at DATETIME DEFAULT CURRENT_TIMESTAMP, -- 생성된 시간
	FOREIGN KEY (raw_material_id) REFERENCES raw_materials(id),
	FOREIGN KEY (store_id) REFERENCES stores(id)
);

CREATE TABLE order_records(
	id INT AUTO_INCREMENT PRIMARY KEY, -- 인덱싱
	employee_id INT, -- users 테이블의 id
	supplier_id INT, -- suppliers 테이블의 id
	change_date DATETIME DEFAULT CURRENT_TIMESTAMP, -- 변경된 시간
	raw_material_id INT, -- raw_material 테이블의 id
	quantity INT NOT NULL, -- 수량
	create_at DATETIME DEFAULT CURRENT_TIMESTAMP, -- 생성된 시간
	FOREIGN KEY (employee_id) REFERENCES employees(id),
	FOREIGN KEY (raw_material_id) REFERENCES raw_materials(id),
	FOREIGN KEY (supplier_id) REFERENCES suppliers(id)
);

CREATE TABLE sales_records(
	id INT AUTO_INCREMENT PRIMARY KEY, -- 인덱싱
	user_id INT, -- users 테이블의 id,
	store_id INT, -- stores 테이블의 id
	is_refund BOOL DEFAULT FALSE, -- 반품하는 것인지 확인하는 컬럼
	created_at DATETIME DEFAULT CURRENT_TIMESTAMP, -- 생성된 시간
	FOREIGN KEY (user_id) REFERENCES users(id),
	FOREIGN KEY (store_id) REFERENCES stores(id)
);

CREATE TABLE sales_items(
	id INT AUTO_INCREMENT PRIMARY KEY, -- 인덱싱
	sales_record_id INT, -- sales_records 테이블의 id
	product_id INT, -- products의 id
	quantity INT NOT NULL, -- 수량
	created_at DATETIME DEFAULT CURRENT_TIMESTAMP, -- 생성된 시간
	FOREIGN KEY (sales_record_id) REFERENCES sales_records(id),
	FOREIGN KEY (product_id) REFERENCES products(id)
);