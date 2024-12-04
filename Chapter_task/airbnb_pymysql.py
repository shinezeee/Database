import pymysql

conn = pymysql.connect(
    host='localhost',  # 데이터베이스 서버 주소
    user='root',       # 데이터베이스 사용자 이름
    password='1234',  # 데이터베이스 비밀번호
    db='airbnb',       # 데이터베이스 이름
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)
try : 
    with conn.cursor() as cursor:
    #     # 1. 새로운 제품 추가 
    #     sql = "INSERT INTO Products(productName, price, stockQuantity) VALUES (%s, %s, %s)"
    #     cursor.execute(sql, ('Python Book', 12000, 100))
    #     conn.commit()
        
    #     # 2. 고객 목록 조회
    #     cursor.execute("SELECT * FROM Customers")
    #     for list in cursor.fetchall():
    #         print(list)
        
    #     # 3. 제품 재고 업데이트
    #     sql = "UPDATE products SET stockQuantity = stockQuantity - %s WHERE productsID = %s "
    #     cursor.execute(sql, (1,1))
    #     conn.commit()
        
    #     # 4. 고객별 총 주문 금액 계산
    #     sql = "DELETE FROM Orders WHERE orderID = %s"
    #     cursor.execute(sql)
    #     total = cursor.fetchall()
    #     print(total)
            
    #     # 5. 고객 이메일 업데이트
    #     customer_id = input("업데이트할 고객 ID 를 입력하세요 : ")
    #     new_email = input("새 이매일 주소를 입력하세요 : ")
    #     sql = "UPDATE Customers SET email = %s WHERE customersID = %s"
    #     cursor.execute(sql,(new_email,customer_id))
    #     conn.commit()
        
    #     # 6. 주문 취소
    #     order_id = input("취소할 주문 ID를 입력하세요 : ")
    #     sql = "DELETE FROM Orders WHERE orderID =%s"
    #     cursor.execute(sql,(order_id,))
    #     conn.commit()               
        
    #     # 7. 특정 제품 검색
    #     product_name = input("검색할 제품 이름을 입력하세요 : ")
    #     sql =" SELECT * FROM Products WHERE productName LIKE %s"
    #     cursor.execute(sql, (f"%{product_name}%"))
    #     result = cursor.fetchall()
    #     for product in result :
    #         print (product)
    
    #     # 8. 특정 고객의 모든 주문 조회
    #     customer_id = input("조회할 고객 ID를 입력하세요 : ")
    #     sql = "SELECT * FROM Orders WHERE customerID =%s"
    #     cursor.execute(sql,(customer_id))
    #     orders = cursor.fetchall()
    #     for order in orders:
    #         print (order)
    #         print (f"총 {len(order)}건")
   
    #     # 9. 가장 많이 주문한 고객
    #     sql =  "SELECT customerID , COUNT(*) as orderCount FROM Orders GROUP BY customerID ORDER BY orderCount DESC LIMIT 1"
    #     cursor.execute(sql)
    #     top_customer = cursor.fetchone()
    #     print (top_customer)
    

finally :
    cursor.close()