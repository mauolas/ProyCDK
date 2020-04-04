#!/bin/python3

from cryptography.fernet import Fernet
import pyodbc
import json

params = (
  "DRIVER={PostgreSQL};"
  "DATABASE=tgpython;"
  "UID=tgurus_alumno;"
  "PWD=tg2019;"
  "SERVER=138.68.2.24;"
  "PORT=5432;"
)

def getRLineal(v_x, v_y, x_pos):
    #v_x = [2014, 2015, 2016, 2017, 2018, 2019]
    #v_y = [530, 560, 610, 690, 720, 830]
    #x_pos = 202_0
    n = len(v_x)
    x, y, xy, xx = [0.0 for _ in range(4)]
    for i in range(n):
        x += v_x[i]
        y += v_y[i]
        xy += v_x[i] * v_y[i]
        xx += v_x[i] ** 2
    m = ((n * xy) - (x * y)) / ((n * xx) - (x ** 2))
    b = (y - (m * x)) / n
    y_obj = (m * x_pos) + b
    return json.dumps({"status": "ok", "y_obj":y_obj})

def getSession(mail,passw):
    file = open('key.key', 'rb')
    key = file.read() # The key will be type bytes
    file.close()
    fernet = Fernet(key)
    # Consulta de user
    conn = pyodbc.connect(params)
    cursor = conn.cursor()
    cursor.execute("""
    select
	usuario, cont
    from
	public.users
    where
	correo = '{var}';
            """.format(var=mail))
    if(cursor.rowcount < 1):
        return json.dumps({"status": "error", "msj":"sin registro"})
    row = cursor.fetchone()
    decryptedPass = fernet.decrypt(row[1].encode())
    #Comparamos passw recibido con
    if(passw == decryptedPass.decode()):
        # se regresa json con validación y se inserta fecha de ingreso
        cursor.execute("""
        update
	    public.users
        set
	    uacceso = clock_timestamp()
        where
	    correo = '{var}';
            """.format(var=mail))
        conn.commit()
        return json.dumps({"status": "correcto", "user":row[0]})
    else:
        #se retorna acceso incorrecto
        return json.dumps({"status": "error", "msj":"contraseña invalida"})
