# ForeverAlone
ForeverAlone es un lenguaje de programación imperativo creado para la clase de compiladores de febrero del 2020. ForeverAlone permite la declaración de variables de tipo int, float y char; declaración de funciones de tipo void, int float y char además de el uso de arreglos.


# Ejecución

Para utilizar ForeverAlone es necesario contar con todos los archivos disponibles en el branch de develop y ejecutar Python 3 junto con el archivo ForeverAlone.py y el archivo .txt donde se haya escrito el código. Para ver todos los requisitos y como ejecutar un HelloWorld puedes ingresar al siguiente video: https://drive.google.com/file/d/1j4pRJXtZsYcrXskHZKdtslpF1CjzaB1N/view?usp=sharing

# Características
La estructura básica de un programa elaborado con ForeverAlone es la siguiente:
```
program Nombre_prog;
var <tipo> <id>;

func <tipo>  <id> ( <tipo> <id> )
var <tipo> <id>;{
<Estatutos>;
return <id_de_varible>; #En caso de ser de tipo diferente a void
}

main(){
<Estatutos>;
}
```
## Declaración de variables

Al declarar las variables se necesita establecer que tipo de variable es (int, float o char) y solo se les puede asignar un valor dentro del cuerpo de alguna función. Igualmente las variables declaradas al principio del programa son consideradas globales y pueden ser accesadas en cualquier momento pero en caso de existir una variable local con el mismo nombre se le dará prioridad a esta última variable. Igualmente se pueden declarar arreglos unidimensionales en los mismos lugares donde puedes usar variables pero es necesario especificar el número de casillas que tendrá el arreglo.

## Declaración de funciones

En la declaración de funciones se necesita especificar el tipo de función al inicio (void, int, float o char) y en caso de ser diferente a void necesitará de un estatuto return o de lo contrario mostrará un error de compilación. Se pueden declarar variables locales al inicio de las funciones que solo podrán ser accesadas por esa función.

## Main

En la función main es donde se lleva a cabo la ejecución por lo que todo lo que quieras mostrar deberá realizarse dentro de este, ya sean asignaciones o llamadas a otras funciones. En main no es posible declarar variables por lo que deberás utilizar variables globales en caso de querer usar variables dentro del main.

## Asignaciones
A las variables se les puede asignar un valor que coincida con el tipo con el que fueron declarados o de lo contrario mostará un error en compilación.  Igualmente se pueden asignar valores a arreglos unidimensionales en los mismos lugares donde puedes usar variables pero es necesario especificar la casilla a indexar.

## Llamadas

Las funciones declaradas previamente pueden ser llamadas pero es necesario asegurar que la cantidad y tipos de los parametros sean iguales a los declarados en la función y que en caso de ser void no sea asignado y si es diferente a void su valor de retorno tiene que ser utilizado o se mostrará un error de compilación. Es posible crear funciones recursivas :). Ejemplo:
```
program Nombre_prog;

func void pruebaVoid(){
	print("Probando void");
}

func int suma(int x, int y){
	return(x+y);
}
main(){
	pruebaVoid(); #Uso correcto
	print(pruebaVoid()); #Incorrecto

	print(suma(3,2.5)); #Correcto
	suma(3, 2.5); #Incorrecto
}
```


## Print

La función print permite mostrar en consola los parametros que se le pasen, ya sea una variable, una llamada a una función o un string escrito entre " ". Es importante notar que print muestra cada parametro en una nueva linea por lo que es mejor escribir los strings lo más juntos posible.

## Read

La función read permite al usuario ingresar por medio de la consola un valor que será asignado a la variable que se utilizo como parámetro, es importante asegurar que el valor ingresado sea del mismo tipo que la variable declarado o de lo contrario se mostrará un mensaje de error.