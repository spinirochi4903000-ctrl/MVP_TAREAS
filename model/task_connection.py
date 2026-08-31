import psycopg2 

class TaskConnection:
    conn = None

    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                host="localhost",
                database="mvp_tareas",
                user="postgres",
                password="Sena1234",
                port="5432",
            )
        except psycopg2.OperationalError as err:
            print(err)
            self.conn.close()

    def write(self, data):
        with self.conn.cursor() as cur:
            cur.execute(
                """INSERT INTO "tareas" (id_tarea, id_tipo_tarea, fecha_hora, descripcion, fecha_vencimiento, prioridad, estado) VALUES (%(id_tarea)s, %(id_tipo_tarea)s, %(fecha_hora)s, %(descripcion)s, %(fecha_vencimiento)s, %(prioridad)s, %(estado)s)""", data
            )

            self.conn.commit()

    def __def__(self):
        if self.conn:
            self.conn.close()
