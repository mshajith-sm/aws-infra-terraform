from psycopg import connect


def save_employee(data):

    with connect(
        host="postgres-db",
        port=5432,
        dbname="employee_db",
        user="admin",
        password="Password123"
    ) as conn:

        with conn.cursor() as cur:

            cur.execute("""
                INSERT INTO employees
                (
                    employee_name,
                    dob,
                    total_experience,
                    relevant_experience,
                    employer_name,
                    notice_period,
                    serving_notice,
                    last_working_day,
                    email,
                    phone
                )

                VALUES
                (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """,
            (
                data["employee_name"],
                data["dob"],
                data["total_experience"],
                data["relevant_experience"],
                data["employer_name"],
                data["notice_period"],
                data["serving_notice"],
                data["last_working_day"],
                data["email"],
                data["phone"]
            ))

            conn.commit()