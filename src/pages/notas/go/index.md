---
title: Svelte con Express & Prisma
description: Lorem ipsum
layout: ../../../layouts/BlogLayout.astro
---

<br/>

# Aprendiendo GO

Estas son mis notas que hago mientras veo un [curso](https://youtube.com/playlist?list=PLt1J5u9LpM5-L-Ps8jjr91pKhFxAnxKJp&si=wf10AsZLJSnjjoHK) de Go desde 0, la idea es aprenderlo para usarlo de `backend`

- Es necesario tener ya conocimientos sobre algun tipo de lenguaje ya que hay partes que no se explican al 100% porque son conceptos que comparten todos los lenguajes
- Mi opinion de `Go`, es lo mejor de C y Python

## Hola Mundo

```go
// Con esto le decimos a GO que es el inicio
package main

// Esta libreria es la que nos permite imprimir cosas en pantalla
import "fmt"

// Creamos la funcion principal
func main() {
    /*
    Llamamos a fmt y usamos su metodo Println (esto hace un salto de linea
    automatico) y le pasamos la string que queremos imprimir
    */
    fmt.Println("Hola Mundo!")
}
```

Para ejecutar un archivo en go hacemos

```sh
go run main.go

# Salida
# Hola Mundo!
```

Para hacer un ejecutable de nuestro archivo hacemos

```sh
go build main.go
```

Esto nos creara un ejecutable que hara lo que hayamos escrito dentro del code

```sh
# Ejecutamos el ejecutable
./main

# Salida
# Hola Mundo!
```

## Tipos de datos

1. Enteros
2. Flotantes
3. Cadena de texto
4. Booleanos
5. Derivados
    - Punteros
    - Arreglos
    - Estructuras
    - Uniones
    - Funciones
    - Slices
    - Interfaces
    - Maps
    - Channels

### Rango de valores de enteros

```md
|   Nomenclatura   |   Bits   |   Alcance                                   |
|------------------|----------|---------------------------------------------|
| uint8            | 8        | 0  a  255                                   |
| uint16           | 16       | 0  a  65535                                 |
| uint32           | 32       | 0  a  4294967295                            |
| uint64           | 64       | 0  a  18446744073709551615                  |
| int8             | 8        | -128  a  127                                |
| int16            | 16       | -32768  a  32767                            |
| int32            | 32       | -2147483648  a  2147483647                  |
| int64            | 64       | -9223372036854775808  a  9223372036854775807|
```

<br>

### Rango de valores flotantes

- float32
- float64
- complex64
- complex128

### Otra forma de tipos de datos

```md
|   Nomenclatura   |   Bits   |   Alcance                  |
|------------------|----------|----------------------------|
| byte             | 8        | 0 a 255                    |
| rune             | 32       | -2147483648  a  2147483647 |
| uint             | 32 o 64  |                            |
| int              | 32 o 64  |                            |
```

<br>

```go
package main

import "fmt"

func main() {
    fmt.Println("Hola Mundo!") // string
    fmt.Println(25)            // int
    fmt.Println(2.5)           // float64 o float32
    
    // Booleanos
    fmt.Println(true)
    fmt.Println(false)
}

/*
>> Salida <<

Hola Mundo!
25
2.5
true
false

*/
```

## Variables y constantes

Las variables que se declaren tienen que ser usadas, GO no te dejara seguir si tienes variables sin usar

```go
package main

import "fmt"

func main() {
    // VARIABLES

    // esto es declarar una variable
    var nombre string

    // esto es darle valor a una variable
    nombre = "Wilovy"

    // Imprirmir en consola
    fmt.Println("Hola " + nombre)

    // Declarar variables en una sola linea
    var a, b int = 1, 2

    var c,d int
    c = 3
    d = 4

    fmt.Println(a, b, c, d)

    // declarar varias variables de distintos tipos
    var (
        pi float64
        booleano bool
        
        // En automatico se le asigna el valor string
        cadena = "Texto"
        // En automatico se le asigna el valor int
        edad   = 25
    )

    pi = 3.14
    booleano = true

    fmt.Println(pi, booleano, cadena, edad)


    /*
        Podemos definir variables sin decir que tipo de dato es usando ':='
        y en automatico se le asigna el tipo de dato que se le asigno
        en este caso es  int
    */
    v1 := 1

    // Esto es para cambiar su valor
    v1 = 10

    fmt.Println(v1)

    // CONSTANTES
    // Podemos definirlos fuera de la funcion main y asignarle un tipo de dato
    // Igual que en las variables, solo que no se pueden cambiar su valor
    const n = 25

    fmt.Println(n)
}

/*
    SALIDA

$ go run main.go
 
 Hola Wilovy
 1 2 3 4
 3.14 true Texto 25
 10
 25
*/
```

## Palabras reservadas

- break
- default
- funct
- interface
- select
- defer
- go
- chan
- struct
- map
- case
- for
- if
- else
- goto
- package
- switch
- var
- const
- fallthrough
- range
- type
- continue
- import
- return

## Salida y entrada de datos

- `\n` es una salto de linea
- `\t` es una tabulacion
- `%s` para mostrar datos tipo string
- `%d` para mostrar datos tipo entero
- `%f` para mostrar datos tipo flotante

```go
package main

import "fmt"

func main() {
    // Print no tiene salto de linea automatico
    // \n es un salto de linea
    fmt.Print("Hola Mundo\n")
    // \t es un tabulador
    fmt.Print("\tHola Mundo\n")

    nombre := "Wilovy"
    edad := 21
    pi := 3.141592

    // Println tiene salto de linea automatico
    fmt.Println("\nSin formato\nNombre: ", nombre, "\nEdad: ", edad, "\nPI: ", pi)
    // Printf permite formatear la salida
    fmt.Printf("\nFotmateado\nNombre: %s\nEdad: %d\nPI: %.2f\n", nombre, edad, pi)
}
```

### Entrada de datos

```go
package main

import "fmt"

func main() {

    var(
        nombre string
        edad int
        pi float64
    )

    // Pedimos los datos
    fmt.Print("Ingrese su nombre: ")
    // Scanf le decimos que tipo de dato espera y lo guarda en la variable
    // usamos un '&' para indicarle en que variable debe guardar el dato
    fmt.Scanf("%s", &nombre)

    fmt.Print("Ingrese su edad: ")
    fmt.Scanf("%d", &edad)

    fmt.Print("Ingrese el valor de PI: ")
    // Scanln lee el dato y lo guarda en la variable
    fmt.Scanln(&pi)

    fmt.Printf("\nFotmateado\nNombre: %s\nEdad: %d\nPI: %.2f\n", nombre, edad, pi)
}
```

## Operadores aritmeticos

```md
|   Operador   |   Descripcion                     |
|--------------|-----------------------------------|
| +            | Sumar                             |
| -            | Restar                            |
| *            | Multiplicar                       |
| /            | Dividir                           |
| %            | Calcular el modulo de la division |
```

<br>

```go
package main

import "fmt"

func main() {
    var a,b int

    fmt.Print("Numero 01: ")
    fmt.Scanln(&a)

    fmt.Print("Numero 02: ")
    fmt.Scanln(&b)

    suma := a + b
    resta := a - b

    fmt.Println("Suma: ", suma)
    fmt.Println("Resta: ", resta)
    fmt.Println("Multiplicacion: ", a*b)
    fmt.Println("Division: ", a/b)
    fmt.Println("Modulo: ", a%b)
}
```

## Operadores relacionales

a = 2

b = 10

```md
|   Operador   |   Descripcion     |   Ejemplo             |
|--------------|-------------------|-----------------------|
| ==           | Igualdad          | a == b devuelve false |
| !=           | Distintos         | a != b devuelve true  |
| >            | Mayor que         | a > b devuelve false  |
| <            | Menor que         | a < b devuelve true   |
| >=           | Mayor o igual que | a >= b devuelve false |
| <=           | Menor o igual que | a <=b devuelve false  |
```

<br>

```go
package main

import "fmt"

func main() {
    var a,b int

    fmt.Print("Numero 01: ")
    fmt.Scanln(&a)

    fmt.Print("Numero 02: ")
    fmt.Scanln(&b)

    fmt.Println("Iguales: ", a == b)
    fmt.Println("Diferentes: ", a != b)
    fmt.Println("A es mayor: ", a > b)
    fmt.Println("A es menor: ", a < b)
    fmt.Println("A es mayor o igual: ", a >= b)
    fmt.Println("A es menor o igual: ", a <= b)
}
```

## Condicionales

- if
- else if
- else

```go
package main

import "fmt"

func main() {

    if false {
        fmt.Println("Es true")
    } else {
        fmt.Println("Es false")
    }
}
```

Ejercicio 1:

Haz un programa que te diga si un numero es par, impar o neutro

```go
package main

import "fmt"

func main() {

    var n int

    fmt.Print("Numero 01: ")
    fmt.Scan(&n)

    if n == 0{
        fmt.Println("Neutro")  
    }else if n % 2 == 0 {
        fmt.Println("Par")
    } else {
        fmt.Println("Impar")
    }
}
```

## Operadores logicos

Lo que hacen es comparar dos valores booleanos

### NOT (!)

Lo que hace es negar su valor, si es true se vuelve false y si es false se vuelve true

```go
fmt.println(! true)
/*
    SALIDA
false
*/

fmt.println(! false)
/*
    SALIDA
true
*/
```

### AND (&&)

Lo que hace es comparar dos valores booleanos y devuelve otro valor booleano, solo cuando ambos valores a comparar true

```go
fmt.println(true && true)
/*
    SALIDA
true
*/

fmt.println(true && false)
/*
    SALIDA
false
*/
```

### OR (||)

Lo que hace es comparar dos valores booleanos y devuelve otro valor booleando, en este caso ambos o al menos uno tiene que ser true para devolver true

```go
fmt.println(true || false)
/*
    SALIDA
true
*/

fmt.println(true || true)
/*
    SALIDA
true
*/

fmt.println(false || true)
/*
    SALIDA
true
*/

fmt.println(false || false)
/*
    SALIDA
false
*/
```

## Casos

`Switch`

Ejercicio 2:

Realizar un sistema que pida ingresar un numero de 1 a 5 y devuelva ese numero pero escrito

```txt
# Ejemplo
Ingrese un numero: 3

# Salida
# TRES
```

```go
package main

import "fmt"

func main() {
    var (
        n int
        salida string
    )

    fmt.Print("Ingrese un numero: ")
    fmt.Scan(&n)

    switch n {
        case 1:
            salida = "UNO"
        case 2:
            salida = "DOS"
        case 3:
            salida = "TRES"
        case 4:
            salida = "CUATRO"
        case 5:
            salida = "CINCO"

        // Este caso se ejecuta cuando no se cumple ninguno de los anteriores
        default:
            salida = "Numero no valido, ingrese un numero entre 1 y 5"
        }
    fmt.Println(salida)
}
```

## Operadores en asignacion

```md
|   Operador   |   Descripcion                |   Ejemplo           |
|--------------|------------------------------|---------------------|
| =            | Asignar un valor             | a = 5               |
| +=           | Suma en asignacion           | a = a + 3 => a += 3 |
| -=           | Resta en asignacion          | a -=3               |
| *=           | Multiplicacion en asignacion | a *=3               |
| /=           | Division en asignacion       | a /=3               |
| %=           | Modulo en asignacion         | a %=3               |
| ++           | Incrementa su valor en 1     |                     |
| --           | Decrementa su valor en 1     |                     |
```

<br>

```go
package main

import "fmt"

func main() {
    a := 2

    a = a + 3

    fmt.Println(a) // 5

    // Suma en asignación
    a += 3
    fmt.Println(a) // 8


    // ++
    b := 1
    b++
    fmt.Println(b)

    // --
    c := 2
    c--
    fmt.Println(c)
}
```

## Bucle for

En `Go` no existe `while` o `do while`

```go
package main

import "fmt"

func main() {

    // Contador
    fmt.Println("Contador")

    contador := 1
    for contador <= 5 {
        fmt.Println(contador)
        contador++
    }

    // For
    fmt.Println("For")
    for i := 1; i <= 5; i++ {
        fmt.Println(i)
    }
}
```

### Break

`break` termina la ejecucion del codigo en ese punto

```go
package main

import "fmt"

func main() {

    for i := 1; i < 10; i++ {
        if i == 5 {
            fmt.Println("Estamos en la ejecucion 5")
            break
        }
        fmt.Println(i)
    }
}
```

### Continue

`continue` hace un salto en el codigo

```go
package main

import "fmt"

func main() {

    for i := 1; i < 10; i++ {
        if i == 5 {
            fmt.Println("Estamos en la ejecucion 5")
            continue // se salta hasta las sig lineas de codigo
            fmt.Println("Esto no se ejecuta") // Esto no se ejecuta
        }
        fmt.Println(i)
    }
    fmt.Println("Saltado")
}
```

## WIP

<style>
    h1{
        margin: 2rem 0;
        font-weight: 800;
        text-align: center;
        font-size: 2.25rem/* 36px */;
        line-height: 2.5rem/* 40px */;
    }
    h2{
        margin: 2rem 0;
        font-weight: 800;
        text-align: center;
        font-size: 2.25rem/* 36px */;
        line-height: 2.5rem/* 40px */;
    }
    h3{
        margin: 2rem 0;
        font-weight: 800;
        text-align: center;
        font-size: 2.25rem/* 36px */;
        line-height: 2.5rem/* 40px */;
    }
    p{
        margin: 1rem 0;
    }
    li{
        margin: 0.5rem 0;
    }
    pre{
        padding: 2rem
    }
</style>
