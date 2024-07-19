# Registro-de-vehiculo
examen final optativa software básico hecho en Python 

Sistema de Registro de Vehículos
Este proyecto es una aplicación de escritorio desarrollada en Python utilizando Tkinter. Permite registrar la entrada y salida de vehículos en un parqueadero, además de visualizar, modificar y eliminar registros almacenados en un archivo CSV.

Requisitos
Python 3.x
Librerías de Python:
tkinter
csv
datetime

Funcionalidades
Registrar Entrada: Ingresa la placa, el nombre del conductor y la cédula, y presiona "Registrar Entrada". El registro se almacenará en el archivo CSV con un sello de tiempo.

Registrar Salida: Ingresa la placa del vehículo y presiona "Registrar Salida". Si el vehículo tiene una entrada registrada, se actualizará el registro con la salida y el sello de tiempo correspondiente.

Mostrar Registros: Muestra todos los registros almacenados. Desde esta vista, puedes seleccionar un registro para modificar o eliminar.

Modificar Registro: Permite modificar la placa, el nombre y la cédula de un registro existente.
Eliminar Registro: Permite eliminar un registro específico.

Archivos
registro_vehiculos.py: El archivo principal que contiene toda la lógica y la interfaz de la aplicación.
registro_vehiculos.csv: Archivo CSV donde se almacenan los registros de vehículos.

Contribuir
Si deseas contribuir a este proyecto, por favor sigue los siguientes pasos:
Haz un fork del repositorio.
Crea una nueva rama (git checkout -b feature/nueva-funcionalidad).
Realiza tus cambios y haz commit (git commit -am 'Agrega nueva funcionalidad').
Haz push a la rama (git push origin feature/nueva-funcionalidad).
Abre un Pull Request.
