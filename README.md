# Tensorflow Apuntes

## Vectores 

### Crear un vector 

Creamos tensores de rango 0 es decir de solo un valor 

```
cadena = tf.Variable('Cadena de texto', tf.string)
number = tf.Variable(23,tf.int16)
floating = tf.Variable(23.3333,tf.float)
```

Para ver el rango de un tensor usamos el siguiente método __tf.rank__, el rango se refiere al numero de dimensiones que tiene un tensor

```
tensor1 = tf.Variable([[1,2],[2,5]])
tf.rank(tensor1)
```

El método __shape__ se usa para saber el número de elementos en cada dimensión 

```
tensor1.shape
```

Para cambiar el tamaño de un tensor se usa el método __reshape__

```
tensor2 = tf.reshape(tensor1, [2,3,1])

Esto significa que se redimensionara a:
-2 listas
-3 listas por cada lista
-1 elemento por cada lista

tensor3 = tf.reshape(tensor1 [3, -1])

Ese -1 significa que automaticamente calcula en cuantas filas se reordena el vector
```
*Util*

``tf.zeros(1,1) (para crear un vector de todo ceros)``


Tipos de tensores 
+ Variable
+ Constante
+ Placeholder
+ Sparse Tensor

Seleccionar solo algunas filas del tensor 

```
# Now lets select some different rows and columns from our tensor

three = tensor[0,2]  # selects the 3rd element from the 1st row
print(three)  # -> 3

row1 = tensor[0]  # selects the first row
print(row1)

column1 = tensor[:, 0]  # selects the first column
print(column1)

row_2_and_4 = tensor[1::2]  # selects second and fourth row
print(row2and4)
```

### Crear sesión

Para usar un tensor es necesario crear una sesion 

```
with tf.Session() as sess:
  tensor.eval()
```

## Learning Algorithms

### Linear Regresion (sklearn)




