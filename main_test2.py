import psycopg2 # postgresql Connect Module
from datetime import datetime, timedelta # Date Module

def connect_db():
    conn = None  # conn의 기본값 선언
    count = 3  # count의 기본값 선언
    while count > 0:  # count값이 0이 보다 클때까지 반복
        print("-" * 10)
        print("please enter your username :")
        username = input() or "lus"  # ID 입력란
        print("-" * 10)
        print("please enter your password :")
        user_password = input() or "tiger"  # PW 입력란
        count = count - 1  # 입력마다 count 감소 -1
        try:
            # 연결 함수가 성공해서 반환값을 주면, conn은 더 이상 None이 아님
            conn = psycopg2.connect(dbname='DVD Rental',
                                    host='localhost',
                                    port='5432',
                                    user=username,  # 입력된 ID가 작성되는곳
                                    password=user_password)  # 입력된 PW가 작성되는곳
            print("-" * 10)
            print("connection established")  # 연결 성공시 출력
            break  # 연결 성공시 while 탈출
        except:  # 실패시
            print("Not Connect")  # 실패시 출력
    if count == 0 and conn is None:  # Count값 0 , conn값 None 시
        print("ID / PW Error")  # 출력
    return conn

def check_customers(conn):
    cursor = conn.cursor()
    scan = 1
    while scan > 0:
        print("-" * 10)
        print("Scan customer ID or Quit > 'q'")
        customer = input().strip()  # 입력란에 strip()를 추가하여 앞뒤 공백 제거하고 제출
        if customer == 'q':  # 쿼리값 존재시
            return None, None
        try:
            cursor.execute("select * from customer where customer_id = %s", (customer,))  # DB에 질의 전송 , customer_id 존재여부
            customer_data = cursor.fetchone()  # 결과 데이터 가져오기 cursor.fetchone()
            if customer_data:  # 쿼리값 존재시
                return customer, customer_data
            else:  # 쿼리값 미존재시
                print("-" * 10)
                print(f"Not Customer ID {customer}")
        except Exception as e:  # 에러 체크
            print(f"Error: {e}")
            conn.rollback()  # 에러 발생시 롤백
            print("---Rolled Back---")
    return None, None

def process_return(conn,customer):
    cursor = conn.cursor()
    cursor.execute("select * from rental where customer_id = %s and return_date is null",(customer,))  # 조회된 customer_id의 return_date 여부 조회
    rental_data = cursor.fetchone()
    if rental_data:  # return_date is null
        today = datetime.now().date()
        print("-" * 10)
        print("Please Return DVD")
        cursor.execute("""
                       select 
                           r.customer_id, f.title, r.rental_date, f.rental_rate
                       from rental r
                       inner join inventory i
                            on r.inventory_id = i.inventory_id
                       inner join film f
                            on i.film_id = f.film_id
                       where customer_id = %s
                         and r.return_date is null
                       """, (customer,))
        return_dvd = cursor.fetchall()
        total_rate = 0
        for barcode in return_dvd:
            return_date = barcode[2].date()
            all_rate = float((today - return_date).days * barcode[3]) * float(1.1)
            total_rate += all_rate  # 전체값 누적
            print(
                f"Customer Id : {barcode[0]} | "
                f"Title : {barcode[1]} | "
                f"Rental Date : {(today - return_date).days} days | "
                f"Over Rate : {all_rate:.2f}")  # 소수점 2번째 자리까지만 출력 :.2f
        print(f"Total Rate : {total_rate:.2f}")
        print("-" * 10)
        return True
    else:
        return False

conn = connect_db() # DB 접속

while True:
    customer, customer_data = check_customers(conn) # 고객정보 호출 (기본화면)
    if customer is None:
        break
    is_return = process_return(conn, customer) # 고객의 미반납 이력 확인
    if is_return:
        input("Total Rental Rate : (Enter)")
    else:
        print("-" * 10)
        print("Please DVD Barcode")

conn.close()