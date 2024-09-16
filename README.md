# Tensorflow Apuntes

### Vectores 

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
```

