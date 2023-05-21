import sqlite3

conexion = sqlite3.connect('Ejercicio3.db')
c= conexion.cursor()
c.execute('''CREATE TABLE registro (fecha text, operacion text, simbolo text, cantidad real, precio real)''')

c.execute("INSERT INTO registro VALUES('1/dic/2020','compra','INV', 100, 15.43)")
c.execute("INSERT INTO registro VALUES('14/nov/2021','venta','INV', 22, 16.43)")
c.execute("INSERT INTO registro VALUES('23/abr/2022','compra','INV', 33, 17.43)")
c.execute("INSERT INTO registro VALUES('02/ene/2023','venta','INV', 44, 18.43)")
c.execute("INSERT INTO registro VALUES('1/feb/2019','compra','INV', 50, 19.43)")

conexion.commit()

c.execute("SELECT * FROM registro")

registros = c.fetchall()


for registro in registros:
    print(registro)


conexion.close()
