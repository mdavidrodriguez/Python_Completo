
import mysql.connector

midb = mysql.connector.connect(
    host='localhost',
    user = 'chanchitofeliz',
    password = '1234',
    database = 'prueba'
)

cursor = midb.cursor()

# fetchall devuelve todas las instancias de la base de datos que encontro a la variable que tenemos asignada
# fetchone solo devueleve el primer elemento que este ha encontrado

# ================================================
#  Listar datos
# ================================================

# cursor.execute('select * from Usuario')
# resultado = cursor.fetchall()
# # resultado = cursor.fetchone()
# print(resultado)

# cursor.execute('show create table Usuario') 


# ================================================
#  Insertar datos
# ================================================

# sql = 'insert into Usuario (email, username, edad) values (%s, %s, %s)'
# values = ('micorreo@gmail.com','nombreusuario',45)
# cursor.execute(sql, values) 
# midb.commit()
# print(cursor.rowcount)


# ================================================
#  Actualizar datos
# ================================================
# sql = 'update Usuario set email = %s where id = %s'
# values = (' micorreo@gmail.com',4)
# cursor.execute(sql, values) 
# midb.commit()


# ================================================
#  Eliminar Datos
# ================================================

# sql = 'delete from Usuario where id = %s'
# values = (4, )
# cursor.execute(sql,values)
# midb.commit()


# ================================================
#  Limitar las consultas
# ================================================

# cursor.execute('select * from Usuario limit 3')
# resultado = cursor.fetchall()
# print(resultado)










