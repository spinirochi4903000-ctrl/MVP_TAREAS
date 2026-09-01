import psycopg2
import psycopg2.extras


class TaskConnection:
    conn = None

    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                host="localhost",
                database="mvp_SAID",
                user="postgres",
                password="admin",
                port="5432",
            )
        except psycopg2.OperationalError as err:
            print(err)
            self.conn = None

    def write(self, data):
        # id_tarea es autogenerado, nunca se inserta
        with self.conn.cursor() as cur:
            cur.execute(
                """INSERT INTO "tareas" (id_tipo_tarea, fecha_hora, descripcion, fecha_vencimiento, prioridad, estado)
                VALUES (%(id_tipo_tarea)s, %(fecha_hora)s, %(descripcion)s, %(fecha_vencimiento)s, %(prioridad)s, %(estado)s)""",
                data,
            )
            self.conn.commit()

    def get_all(self):
        with self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute('SELECT * FROM "tareas" ORDER BY fecha_hora')
            return cur.fetchall()

    def get_by_date(self, date):
        # date en formato "YYYY-MM-DD"; compara solo la parte de fecha de fecha_hora
        with self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute(
                'SELECT * FROM "tareas" WHERE DATE(fecha_hora) = %s ORDER BY fecha_hora',
                (date,),
            )
            return cur.fetchall()

    def get_by_id(self, id_tarea):
        with self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute('SELECT * FROM "tareas" WHERE id_tarea = %s', (id_tarea,))
            return cur.fetchone()

    def update(self, id_tarea, updated_fields: dict):
        if not updated_fields:
            return

        set_clause = ", ".join(f"{key} = %({key})s" for key in updated_fields)
        updated_fields["id_tarea"] = id_tarea

        with self.conn.cursor() as cur:
            cur.execute(
                f'UPDATE "tareas" SET {set_clause} WHERE id_tarea = %(id_tarea)s',
                updated_fields,
            )
            self.conn.commit()

    def delete(self, id_tarea):
        with self.conn.cursor() as cur:
            cur.execute('DELETE FROM "tareas" WHERE id_tarea = %s', (id_tarea,))
            self.conn.commit()