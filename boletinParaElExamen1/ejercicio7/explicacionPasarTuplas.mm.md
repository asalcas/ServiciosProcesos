# Explicación del código

## Línea 1: `idProceso, num1, num2 = map(int, linea.strip().split())`

### `linea.strip()`
- Elimina espacios en blanco al inicio y final de la línea.
- Elimina caracteres como saltos de línea (`\n`).

### `.split()`
- Divide la línea en fragmentos usando espacios como separador.
- Devuelve una lista de cadenas.

#### Ejemplo:
- Entrada: `" 1 10 20\n"`
- `linea.strip()` -> `"1 10 20"`
- `.split()` -> `["1", "10", "20"]`

### `map(int, ...)`
- Convierte cada elemento de la lista en un entero.
- Devuelve un objeto que contiene los números convertidos.

#### Ejemplo:
- Entrada: `["1", "10", "20"]`
- Resultado: `[1, 10, 20]`

### `idProceso, num1, num2 = ...`
- Desempaqueta los valores de la lista y los asigna a las variables.

#### Ejemplo:
- Entrada: `[1, 10, 20]`
- Resultado:
  - `idProceso = 1`
  - `num1 = 10`
  - `num2 = 20`

---

## Línea 2: `cola.put((idProceso, num1, num2))`

### `(idProceso, num1, num2)`
- Agrupa los valores en una **tupla**.
- Una tupla es una estructura inmutable que almacena varios elementos.

#### Ejemplo:
- Entrada: `idProceso = 1, num1 = 10, num2 = 20`
- Resultado: `(1, 10, 20)`

### `cola.put(...)`
- Agrega el valor (la tupla) a una **cola** de tipo `Queue`.
- Las colas se usan para compartir datos entre procesos en Python.
- Funciona como una fila (FIFO: *First In, First Out*).

#### Ejemplo:
- Antes: `cola = []`
- Operación: `cola.put((1, 10, 20))`
- Después: `cola = [(1, 10, 20)]`

---

## Ejemplo completo

### Línea del archivo:
```plaintext
1 10 20
