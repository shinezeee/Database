import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",  # 사용자 이름
    password="1234",  # 비밀번호
    database="fishbread_db", # db 이름
    charset="utf8mb4"
)


cursor = connection.cursor()

# # 새로운 사용자 “8ki joa”를 추가해주세요.

# sql = "INSERT INTO Users (first_name, last_name, email, password, address, contact, gender) VALUES (%s,%s,%s,%s,%s,%s,%s)"
# values = ("8ki","Joa","oz08@oz.com","1234","seoul sinsa","01008082222","FEMALE")

# cursor.execute(sql,values)

# # 사용자 “8ki joa”의 주소를 변경해주세요.

# change_adr = "UPDATE Users SET address = %s WHERE first_name =%s AND last_name =%s "
# n_adr = ("Asan","8ki","Joa")

# cursor.execute(change_adr,n_adr)

# 1번 store에서 사용자 “8ki joa”의 주문을 생성해주세요.
# (팥 붕어빵 3개, 크림 붕어빵 2개, 시그니처 메뉴 5개)\

first_name = "8ki"
last_name = "Joa"
cursor.execute ( "SELECT id FROM Users WHERE first_name =%s AND last_name =%s", (first_name,last_name))
store_id =1
user =cursor.fetchone()

orders = [ ("Red Bean Bun",3),("Cream bun",2),("HJ fish",5)]

cursor.execute ("""
        INSERT INTO order_recodes ()
                """)


# sql = "INSERT INTO order_redcode () "

# order_records 테이블에 발주이력을 3건 생성해주세요.

# tocks 테이블에 원재료 사용이력을 3건 추가하고, 최근 사용이력 3건을 조회해주세요.

# 유저 “8ki joa”가 주문한 내역을 조회해주세요.단, 비싼 금액의 상품순으로 나열

connection.commit()