import random

import pymysql
import datetime
from faker import Faker
from pymysql.cursors import DictCursor


# noinspection PyTypeChecker
class Dummy:
    def __init__(self, host: str, user: str, password: str, database: str):
        # Faker 객체 생성
        self.fake = Faker()

        # 데이터베이스 연결 설정
        self.connection = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            charset="utf8mb4",
            cursorclass=DictCursor,
        )

    def _execute(self, query, params=None):
        # 쿼리를 실행하는 헬퍼 메서드 (INSERT, UPDATE, DELETE)
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, params)
                self.connection.commit()
                if query.strip().upper().startswith("INSERT"):
                    return cursor.lastrowid
        except Exception as e:
            print(f"Query error: {e}")
            self.connection.rollback()

    def _fetch(self, query, params=None):
        # 조회 쿼리 실행 후 결과 반환하는 헬퍼 메서드
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, params)
                return cursor.fetchall()  # 결과를 리스트 형태로 반환
        except Exception as e:
            print(f"Query error: {e}")
            return []

    def create_user(self, count: int):
        # count 명의 더미 사용자 데이터 생성
        for _ in range(count):
            first_name = self.fake.first_name()
            last_name = self.fake.last_name()
            email = self.fake.unique.email()
            password = self.fake.password()
            address = self.fake.address()
            contact = self.fake.phone_number()
            gender = random.choice(["MALE", "FEMALE"])
            is_active = random.choice([True, False])

            query = """
            INSERT INTO 
            users (first_name, last_name, email, password, address, contact, gender, is_active) 
            VALUES 
            (%s, %s, %s, %s, %s, %s, %s, %s)
            """

            self._execute(
                query,
                (
                    first_name,
                    last_name,
                    email,
                    password,
                    address,
                    contact,
                    gender,
                    is_active,
                ),
            )

        print(f"Successfully created {count} users!")

    def create_raw_materials(self):
        # 원재료 생성
        raw_materials = [
            ("Flour", 1.76),
            ("Sugar", 2.00),
            ("Yeast", 0.50),
            ("Red Bean Paste", 4.50),
            ("Chocolate", 28.00),
            ("Cream", 4.50),
            ("Avocado", 11.40),
            ("Salt",1.00),
            ("acc",3.00),
            ("bun",2.50)
        ]

        query = "INSERT INTO raw_materials (name, price) VALUES (%s, %s)"

        for name, price in raw_materials:
            self._execute(query, (name, price))

        print(f"Successfully created {len(raw_materials)} raw materials!")

    def create_stores(self, count: int):
        # 더미 가맹점 데이터 생성
        for _ in range(count):
            address = self.fake.address()
            name = self.fake.country()
            contact = self.fake.phone_number()

            query = "INSERT INTO stores (address, name, contact) VALUES (%s, %s, %s)"

            self._execute(query, (address, name, contact))

        print(f'Successfully created {count} stores!')

    def create_suppliers(self, count: int):
        # 더미 공급업체 데이터 생성
        for _ in range(count):
            address = self.fake.address()
            name = self.fake.country()
            contact = self.fake.phone_number()

            query = "INSERT INTO suppliers (address, name, contact) VALUES (%s, %s, %s)"

            self._execute(query, (address, name, contact))

        print(f'Successfully created {count} suppliers!')

    def create_stocks(self):
    # 재고 생성
        raw_materials_query = "SELECT id FROM raw_materials"
        raw_material_ids = [row["id"] for row in self._fetch(raw_materials_query)]

        stores_query = "SELECT id FROM stores"
        store_ids = [row["id"] for row in self._fetch(stores_query)]

        query = "INSERT INTO stocks (raw_material_id, pre_quantity, quantity, change_type, store_id, create_at) VALUES (%s, %s, %s, %s, %s, %s)"

        for store_id in store_ids:
            for raw_material_id in raw_material_ids:
                # 랜덤으로 변경 될 재고 생성
                quantity = random.randint(50, 200)
                # 랜덤으로 IN, OUT 선택
                change_type = random.choice(["IN", "OUT"])

                # stocks 테이블에서 raw_material_id(쿼리문)가 raw_material_id(for문 내부변수)인 행의
                # quantity값의 리스트를 반환
                pre_quantity = self._fetch(
                    "select quantity FROM stocks WHERE raw_material_id = %s limit 1",
                    (raw_material_id,),
                )

                # 위에서 선언한 변수 pre_quantity가 빈배열(0)인지 확인
                pre_quantity = pre_quantity[0]["quantity"] if pre_quantity else 0

                # change_type이 IN일때 pre_quantity와 change_quantity 더해주고 아닐경우 빼준다.
                quantity = (
                    pre_quantity + quantity
                    if change_type == "IN"
                    else pre_quantity - quantity
                )
                
                # 랜덤한 날짜와 시간 생성 (예: 2020년 1월 1일부터 2023년 12월 31일까지)
                random_date = self.generate_random_datetime(start_year=2020, end_year=2023)

                # 생성된 random_date를 create_at에 넣기
                create_at = random_date

                # 쿼리 실행
                self._execute(query, (raw_material_id, pre_quantity, quantity, change_type, store_id, create_at))

        print(f"Successfully saved {len(raw_material_ids)} in stocks!")

# 랜덤 날짜 생성 함수
    def generate_random_datetime(self, start_year=2000, end_year=2024):
        year = random.randint(start_year, end_year)
        month = random.randint(1, 12)
        day = random.randint(1, 28)  # 28일을 기준으로 처리
        hour = random.randint(0, 23)
        minute = random.randint(0, 59)
        second = random.randint(0, 59)

        random_datetime = datetime.datetime(year, month, day, hour, minute, second)
        return random_datetime
    def create_products(self):
        # 제품 생성
        products = [
            ("Fish Bun", "A delicious fish-shaped bun.", 3.00),
            ("Red Bean Bun", "Sweet bun filled with red bean paste.", 2.50),
            ("Chocolate Bun", "Decadent chocolate-filled bun.", 3.50),
        ]

        query = "INSERT INTO products (name, description, price) VALUES (%s, %s, %s)"

        for name, description, price in products:
            self._execute(query, (name, description, price))

        print(f"Successfully created {len(products)} products!")

    def create_sales(self):
        # 각 유저 별 판매 기록 생성
        user_query = "SELECT id FROM users"
        user_ids = [row["id"] for row in self._fetch(user_query)]

        product_query = "SELECT id FROM products"
        product_ids = [row["id"] for row in self._fetch(product_query)]

        sales_query = "INSERT INTO sales_records (user_id, store_id) VALUES (%s, %s)"
        sales_item_query = "INSERT INTO sales_items (sales_record_id, product_id, quantity) VALUES (%s, %s, %s)"

        stores_query = "SELECT id FROM stores"
        store_ids = [row["id"] for row in self._fetch(stores_query)]

        for user_id in user_ids:
            user_name_query = "SELECT first_name FROM users WHERE id=%s"
            user_name = self._fetch(user_name_query, user_id)

            store_id = random.randint(store_ids[0], store_ids[-1])

            # 판매 기록 생성
            sales_record_id = self._execute(sales_query, (user_id, store_id))

            # 판매 항목 생성 (1~3개 상품)
            for product_id in product_ids:
                quantity = random.randint(1, 5)
                self._execute(sales_item_query, (sales_record_id, product_id, quantity))

            print(
                f"Successfully created sales and sales items for {user_name[0]['first_name']}!"
            )


    def close_connection(self):
        # 데이터베이스 연결 종료
        self.connection.close()
        print("Connection closed.")

    def create_all_tables(self, count: int):
        # 사용자 수를 기반으로 모든 쿼리 실행 시작
        print(f"Starting all queries with {count} users.")

        try:
            self.create_user(count)
        except Exception as e:
            print(f"Query error: {e}")

        try:
            self.create_stores(count)
        except Exception as e:
            print(f"Query error: {e}")

        try:
            self.create_suppliers(count)
        except Exception as e:
            print(f"Query error: {e}")

        try:
            self.create_raw_materials()
        except Exception as e:
            print(f"Query error: {e}")

        try:
            self.create_stocks()
        except Exception as e:
            print(f"Query error: {e}")

        try:
            self.create_products()
        except Exception as e:
            print(f"Query error: {e}")

        try:
            self.create_sales()
        except Exception as e:
            print(f"Query error: {e}")

        self.close_connection()


# # 예시 사용
if __name__ == "__main__":
    dummy = Dummy(
        host="localhost", user="root", password="1234", database="fishbread_db"
    )

#     # 10명의 사용자 생성
#     dummy.create_user(10)

    # 10개의 가맹점 생성
    # dummy.create_stores(10)

    # 10개의 공급업체 생성
    # dummy.create_suppliers(10)

    # 원재료 생성
    dummy.create_raw_materials()

    # 재고 항목 생성
    # dummy.create_stocks()

    # 제품 생성
    # dummy.create_products()

    # 사용자 별 판매 데이터 생성
    # dummy.create_sales()

    # 데이터베이스 연결 종료
    dummy.close_connection()