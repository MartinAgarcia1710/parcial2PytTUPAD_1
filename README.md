# 📚 Sistema de Gestión de Biblioteca Escolar

Este programa fue desarrollado originalmente por **Alberto Cortez** como parte de un ejercicio educativo para practicar **estructuras de control, manejo de listas paralelas y persistencia de datos** en Python.

Esta versión mantiene **toda la funcionalidad original**, pero se realizaron **ajustes en el manejo de variables globales**, reemplazándolas por **parámetros y valores de retorno**, con el fin de mejorar la claridad y las buenas prácticas de programación estructurada.

---

## 🧠 Objetivo del Proyecto

La biblioteca escolar necesita un sistema de gestión sencillo para registrar títulos y controlar la cantidad de ejemplares disponibles.
El programa permite realizar operaciones como agregar libros, actualizar stock, consultar disponibilidad, listar títulos agotados y mantener la información en un archivo CSV.

---

## ⚙️ Estructura del Código

El programa está contenido en un único archivo Python (`main.py` o `biblioteca.py`, según el entorno de ejecución).
También incluye un archivo CSV para almacenar los datos:

```markdown
biblioteca/
│
├── catalogo.csv      ← Archivo con los datos guardados
└── main.py           ← Código fuente principal
```

---

## 🧩 Funcionalidades Principales

1. **Ingresar títulos** → Carga inicial de libros en el sistema.
2. **Ingresar ejemplares** → Asocia una cantidad de copias a cada título.
3. **Mostrar catálogo** → Muestra todos los libros registrados y su stock actual.
4. **Consultar disponibilidad** → Permite buscar un libro por su nombre y ver cuántos ejemplares hay.
5. **Listar agotados** → Muestra los libros sin ejemplares disponibles.
6. **Agregar título** → Añade nuevos libros al catálogo con su cantidad inicial de ejemplares.
7. **Actualizar ejemplares (préstamo/devolución)** → Modifica el stock de un libro por préstamo o devolución.
8. **Salir** → Finaliza la ejecución del programa.

---

## 💾 Persistencia de Datos

Los títulos y ejemplares se guardan en el archivo `catalogo.csv`, manteniendo la información sincronizada entre ejecuciones.
Cada fila del CSV contiene dos valores:

```
Título, Cantidad de ejemplares
```

Ejemplo:

```
El Principito,5
1984,3
Matar un Ruiseñor,0
```

---

## 🚀 Ejecución del Programa

1. Clonar o descargar este repositorio.
2. Asegurarse de tener instalado **Python 3.10 o superior**.
3. Ejecutar el archivo principal con el siguiente comando:

```bash
python main.py
```

---

## 🧰 Cambios Realizados en Esta Versión

* Eliminación del uso de **variables globales**.
* Sustitución por **parámetros** en las funciones que manipulan las listas `titulos` y `ejemplares`.
* Las funciones retornan los valores actualizados, garantizando una estructura de datos controlada y clara.
* No se modificó la lógica ni el flujo del programa original.

---

## 👨‍🏫 Créditos

* **Código original:** Alberto Cortez
* **Adaptación sin variables globales:** [Martín Alejandro García]

