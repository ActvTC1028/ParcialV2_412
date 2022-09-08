![Tec de Monterrey](../../images/logotecmty.png)
# Ejercicio 2 del examen parcial AD2021
Ciclos - Suma de números entre -100 y 100 que nos proporciona el usuario

Escribe un programa que reciba n números positivos y negativos, deberá sumar sólo aquellos que estén entre -100 y 100 (límites inclusive). 

El programa debe preguntar cuántos números va a recibir del usuario, si la cantidad de números es 0 o menor deberá mandar el mensaje *La cantidad de números debe ser mayor a 0* de lo contrario recibe los números y suma aquellos que estén entre -100 y 100 (límites inclusive) y despliega el resultado de la suma (ve el ejemplo). 

En el ejemplo observa que la solicitud de los números está numerada (Número 1: , Número 2, etc...) Así debe ser el mensaje de ingreso de datos.


Modifica el programa que se encuentra en la carpeta `src` que se llama
`exercise.py` y que contiene el siguiente código:

```python
def main():
    #escribe todo tu código abajo de esta línea, no es necesario una función

if __name__ == '__main__':
    main()
```

**Ejemplo de corrida:**

```
Cantidad de números: 5
Número 1: -65
Número 2: 100
Número 3: -10
Número 4: 1200
Número 5: 50
La suma de números entre -100 y 100 es: 75
```

**Otro ejemplo**
```
Cantidad de números: 0
La cantidad de números debe ser mayor a 0
```


**Nota:** Por favor no quites nada de lo que ya tienes, simplemente agrega el código 
necesario dentro de la función main.   
`if __name__ == '__main__':` debe quedarse en tu código para que las pruebas puedan 
ejecutarse adecuadamente.

Una vez que termines tu actividad, si te da tiempo prueba con
`pytest`, si no, simplemente súbela a tu repositorio en GitHub, con el proceso de commit + push.
Debe ser enviada antes de las 13:00 que se cierra el ejercicio.
