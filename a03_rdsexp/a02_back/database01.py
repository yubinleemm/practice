import pymysql

def get_db_conn():
    return pymysql.connect(
        host="mariadb01.cx8o2w4kajbm.ap-southeast-2.rds.amazonaws.com",
        user="admin",
        password="11111111",
        database="hrms_db",
        port=3306,
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

def select_heros(hero_name: str = "", job_class: str = ""):
    conn = get_db_conn()
    try:
        with conn.cursor() as cursor:
            # 전달받은 검색어 파라미터를 LIKE 검색용으로 구성
            sql = """
                SELECT id, hero_name, job_class, skill_name, skill_level, power_score, element_type 
                FROM user_skills 
                WHERE hero_name LIKE %s AND job_class LIKE %s
            """
            cursor.execute(sql, (f"%{hero_name}%", f"%{job_class}%"))
            result = cursor.fetchall()
            return result
    except Exception as e:
        print("DB 조회 중 에러 발생:", e)
        return []
    finally:
        conn.close()