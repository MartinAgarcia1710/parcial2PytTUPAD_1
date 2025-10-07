# Historias de Usuario - Sistema de Gestión de Biblioteca Escolar

## Información del Proyecto

**Nombre del Sistema:** Sistema de Gestión de Biblioteca Escolar (SegPar)
**Versión:** 1.0
**Fecha:** Octubre 2025
**Tipo de Proyecto:** Sistema educativo de gestión de catálogo bibliotecario

---

## Descripción General

Este documento describe las historias de usuario para el Sistema de Gestión de Biblioteca Escolar, un software diseñado para gestionar el catálogo de libros y el control de ejemplares disponibles mediante una interfaz basada en menú.

El sistema utiliza listas paralelas (`titulos[]` y `ejemplares[]`) para mantener sincronizada la información de los libros y sus copias disponibles, persistiendo los datos en formato CSV.

---

## Roles de Usuario

- **Bibliotecario:** Usuario principal que gestiona el catálogo, registra préstamos y devoluciones
- **Personal Administrativo:** Usuario que consulta disponibilidad y genera reportes básicos

---

## Historias de Usuario

### HU-001: Ingresar Títulos Iniciales

**Como** bibliotecario
**Quiero** poder ingresar múltiples títulos de libros al sistema de manera inicial
**Para** crear el catálogo base de la biblioteca con los libros disponibles

#### Criterios de Aceptación

1. El sistema debe solicitar la cantidad de títulos a ingresar
2. El sistema debe validar que la cantidad sea un número válido (entero positivo)
3. El sistema debe permitir ingresar cada título de forma individual
4. El sistema debe validar que los títulos no estén vacíos
5. Cada título debe inicializarse con 0 ejemplares disponibles
6. Los datos deben guardarse automáticamente en el archivo CSV
7. El sistema debe mostrar un mensaje de confirmación con el número de títulos agregados

#### Escenarios de Prueba

**Escenario 1: Ingreso exitoso de títulos**
- **Dado** que el catálogo está vacío
- **Cuando** el usuario ingresa 3 títulos válidos
- **Entonces** el sistema debe agregar los 3 títulos con 0 ejemplares cada uno
- **Y** debe mostrar "3 título(s) agregado(s) exitosamente"

**Escenario 2: Cantidad inválida**
- **Dado** que el usuario está en la opción de ingresar títulos
- **Cuando** el usuario ingresa "abc" como cantidad
- **Entonces** el sistema debe mostrar "Error: Debe ingresar un número válido"
- **Y** debe regresar al menú principal

**Escenario 3: Título vacío**
- **Dado** que el usuario está ingresando títulos
- **Cuando** el usuario presiona Enter sin ingresar texto
- **Entonces** el sistema debe mostrar "Error: El título no puede estar vacío"
- **Y** debe continuar con el siguiente título

#### Prioridad
**Alta** - Es la funcionalidad base para inicializar el sistema

---

### HU-002: Ingresar Ejemplares a Títulos Existentes

**Como** bibliotecario
**Quiero** agregar o actualizar la cantidad de ejemplares de un título específico
**Para** mantener actualizado el inventario cuando llegan nuevas copias de libros

#### Criterios de Aceptación

1. El sistema debe verificar que existan títulos registrados antes de permitir esta operación
2. El sistema debe mostrar una lista numerada de todos los títulos con sus ejemplares actuales
3. El usuario debe poder seleccionar un título por su número
4. El sistema debe validar que el número seleccionado sea válido
5. El sistema debe validar que la cantidad de ejemplares a agregar sea un número válido
6. La cantidad de ejemplares debe sumarse al total actual (no reemplazarlo)
7. Los datos actualizados deben guardarse en el archivo CSV
8. El sistema debe mostrar el nuevo total de ejemplares

#### Escenarios de Prueba

**Escenario 1: Agregar ejemplares exitosamente**
- **Dado** que existe el título "El Quijote" con 5 ejemplares
- **Cuando** el usuario selecciona ese título y agrega 3 ejemplares
- **Entonces** el sistema debe actualizar a 8 ejemplares
- **Y** debe mostrar "Ejemplares actualizados. Total ahora: 8"

**Escenario 2: Catálogo vacío**
- **Dado** que no hay títulos registrados
- **Cuando** el usuario selecciona la opción de ingresar ejemplares
- **Entonces** el sistema debe mostrar "No hay títulos registrados. Primero ingrese títulos."
- **Y** debe regresar al menú principal

**Escenario 3: Número de título inválido**
- **Dado** que hay 5 títulos registrados
- **Cuando** el usuario ingresa el número 10
- **Entonces** el sistema debe mostrar "Error: Número de título inválido"
- **Y** debe regresar al menú principal

#### Prioridad
**Alta** - Necesaria para gestionar el inventario real de libros

---

### HU-003: Mostrar Catálogo Completo

**Como** bibliotecario o personal administrativo
**Quiero** visualizar todos los libros del catálogo con sus ejemplares disponibles
**Para** conocer el estado completo del inventario de la biblioteca

#### Criterios de Aceptación

1. El sistema debe mostrar todos los títulos registrados en una tabla formateada
2. La tabla debe incluir: número de índice, título y cantidad de ejemplares
3. La información debe mostrarse ordenada por orden de ingreso
4. El formato debe ser legible con columnas alineadas
5. Si el catálogo está vacío, debe mostrar un mensaje informativo
6. No se requiere paginación (se muestran todos los registros)

#### Escenarios de Prueba

**Escenario 1: Visualización de catálogo con datos**
- **Dado** que hay 5 libros registrados en el catálogo
- **Cuando** el usuario selecciona la opción de mostrar catálogo
- **Entonces** el sistema debe mostrar una tabla con los 5 libros
- **Y** debe incluir encabezados "#", "Título" y "Ejemplares"
- **Y** debe tener línea separadora bajo los encabezados

**Escenario 2: Catálogo vacío**
- **Dado** que no hay libros registrados
- **Cuando** el usuario selecciona mostrar catálogo
- **Entonces** el sistema debe mostrar "El catálogo está vacío"

#### Prioridad
**Media** - Importante para consulta general del inventario

---

### HU-004: Consultar Disponibilidad por Título

**Como** bibliotecario
**Quiero** buscar libros por título o parte del título
**Para** verificar rápidamente la disponibilidad de un libro específico

#### Criterios de Aceptación

1. El sistema debe permitir búsquedas por coincidencia parcial del título
2. La búsqueda debe ser insensible a mayúsculas/minúsculas (case-insensitive)
3. El sistema debe mostrar todos los libros que coincidan con la búsqueda
4. Para cada coincidencia debe mostrar: título completo y ejemplares disponibles
5. Si no hay coincidencias, debe mostrar un mensaje informativo
6. Si el catálogo está vacío, debe informarlo

#### Escenarios de Prueba

**Escenario 1: Búsqueda exitosa con una coincidencia**
- **Dado** que existe "El Señor de los Anillos" con 5 ejemplares
- **Cuando** el usuario busca "señor"
- **Entonces** el sistema debe mostrar el título completo y "Ejemplares disponibles: 5"

**Escenario 2: Búsqueda con múltiples coincidencias**
- **Dado** que existen "El Quijote" y "El Principito"
- **Cuando** el usuario busca "el"
- **Entonces** el sistema debe mostrar ambos libros con sus ejemplares

**Escenario 3: Sin coincidencias**
- **Dado** que hay libros en el catálogo
- **Cuando** el usuario busca "Transformers"
- **Entonces** el sistema debe mostrar "No se encontró ningún título con ese nombre"

**Escenario 4: Búsqueda case-insensitive**
- **Dado** que existe "Don Quijote de la Mancha"
- **Cuando** el usuario busca "QUIJOTE"
- **Entonces** el sistema debe encontrar el libro correctamente

#### Prioridad
**Alta** - Funcionalidad crítica para la operación diaria

---

### HU-005: Listar Libros Agotados

**Como** bibliotecario
**Quiero** ver una lista de todos los libros que tienen 0 ejemplares disponibles
**Para** identificar qué libros necesitan reposición o están completamente prestados

#### Criterios de Aceptación

1. El sistema debe filtrar y mostrar solo los títulos con 0 ejemplares
2. La lista debe incluir únicamente los nombres de los títulos
3. Si no hay libros agotados, debe mostrar un mensaje informativo
4. Si el catálogo está vacío, debe informarlo
5. Los títulos deben mostrarse en una lista con viñetas (-)

#### Escenarios de Prueba

**Escenario 1: Existen libros agotados**
- **Dado** que hay 5 libros, de los cuales 2 tienen 0 ejemplares
- **Cuando** el usuario selecciona listar agotados
- **Entonces** el sistema debe mostrar solo los 2 títulos agotados
- **Y** debe usar el formato "- [Título]"

**Escenario 2: No hay libros agotados**
- **Dado** que todos los libros tienen al menos 1 ejemplar
- **Cuando** el usuario selecciona listar agotados
- **Entonces** el sistema debe mostrar "No hay títulos agotados"

**Escenario 3: Catálogo vacío**
- **Dado** que no hay libros registrados
- **Cuando** el usuario selecciona listar agotados
- **Entonces** el sistema debe mostrar "El catálogo está vacío"

#### Prioridad
**Media** - Útil para gestión de inventario y planificación de compras

---

### HU-006: Agregar Nuevo Título al Catálogo

**Como** bibliotecario
**Quiero** agregar un nuevo libro al catálogo especificando su título y ejemplares iniciales
**Para** incorporar nuevas adquisiciones al sistema de manera completa

#### Criterios de Aceptación

1. El sistema debe solicitar el título del libro
2. El sistema debe validar que el título no esté vacío
3. El sistema debe solicitar la cantidad inicial de ejemplares
4. El sistema debe validar que la cantidad sea un número válido (entero no negativo)
5. El título y ejemplares deben agregarse a las listas paralelas manteniendo la sincronización
6. Los datos deben guardarse automáticamente en el archivo CSV
7. El sistema debe mostrar un mensaje de confirmación con el título y cantidad agregados

#### Escenarios de Prueba

**Escenario 1: Agregar título exitosamente**
- **Dado** que el usuario está en la opción de agregar título
- **Cuando** ingresa "Cien Años de Soledad" con 4 ejemplares
- **Entonces** el sistema debe agregar el libro al catálogo
- **Y** debe mantener la sincronización entre listas paralelas
- **Y** debe mostrar "Título 'Cien Años de Soledad' agregado con 4 ejemplar(es)"

**Escenario 2: Título vacío**
- **Dado** que el usuario está agregando un título
- **Cuando** presiona Enter sin ingresar texto
- **Entonces** el sistema debe mostrar "Error: El título no puede estar vacío"
- **Y** debe regresar al menú principal

**Escenario 3: Cantidad inválida**
- **Dado** que el usuario ingresó un título válido
- **Cuando** ingresa "abc" como cantidad de ejemplares
- **Entonces** el sistema debe mostrar "Error: Debe ingresar un número válido"
- **Y** debe regresar al menú principal sin agregar el libro

#### Prioridad
**Alta** - Necesaria para crecimiento del catálogo

---

### HU-007: Actualizar Ejemplares (Préstamo/Devolución)

**Como** bibliotecario
**Quiero** registrar préstamos y devoluciones de libros actualizando la cantidad de ejemplares
**Para** mantener el control preciso del inventario en tiempo real

#### Criterios de Aceptación

**Funcionalidad General:**
1. El sistema debe verificar que existan títulos antes de permitir la operación
2. El sistema debe mostrar una lista numerada de títulos con sus ejemplares actuales
3. El usuario debe poder seleccionar un título por su número
4. El sistema debe validar que el número seleccionado sea válido
5. El sistema debe presentar un submenú con dos opciones: Préstamo y Devolución

**Para Préstamo:**
6. El sistema debe validar que haya ejemplares disponibles (cantidad > 0)
7. Si hay ejemplares, debe disminuir la cantidad en 1
8. Si no hay ejemplares, debe mostrar mensaje de error informativo
9. Debe mostrar la cantidad de ejemplares restantes

**Para Devolución:**
10. El sistema debe aumentar la cantidad de ejemplares en 1
11. Debe mostrar la nueva cantidad de ejemplares

**Persistencia:**
12. Los cambios deben guardarse automáticamente en el archivo CSV
13. Las listas paralelas deben mantenerse sincronizadas

#### Escenarios de Prueba

**Escenario 1: Préstamo exitoso**
- **Dado** que existe "1984" con 3 ejemplares
- **Cuando** el usuario selecciona el libro y la opción Préstamo
- **Entonces** los ejemplares deben reducirse a 2
- **Y** debe mostrar "Préstamo registrado. Ejemplares restantes: 2"

**Escenario 2: Préstamo sin ejemplares disponibles**
- **Dado** que existe "El Hobbit" con 0 ejemplares
- **Cuando** el usuario selecciona el libro y la opción Préstamo
- **Entonces** el sistema debe mostrar "Error: No hay ejemplares disponibles para préstamo"
- **Y** la cantidad debe permanecer en 0

**Escenario 3: Devolución exitosa**
- **Dado** que existe "Orgullo y Prejuicio" con 2 ejemplares
- **Cuando** el usuario selecciona el libro y la opción Devolución
- **Entonces** los ejemplares deben aumentar a 3
- **Y** debe mostrar "Devolución registrada. Ejemplares actuales: 3"

**Escenario 4: Catálogo vacío**
- **Dado** que no hay títulos registrados
- **Cuando** el usuario selecciona actualizar ejemplares
- **Entonces** el sistema debe mostrar "El catálogo está vacío"

**Escenario 5: Opción inválida en submenú**
- **Dado** que el usuario seleccionó un libro válido
- **Cuando** ingresa "5" en el submenú de préstamo/devolución
- **Entonces** el sistema debe mostrar "Opción inválida"
- **Y** debe regresar al menú principal sin realizar cambios

#### Prioridad
**Crítica** - Funcionalidad principal del sistema para operación diaria

---

### HU-008: Salir del Sistema

**Como** usuario del sistema
**Quiero** poder salir de la aplicación de forma controlada
**Para** cerrar el programa correctamente después de completar mis tareas

#### Criterios de Aceptación

1. El sistema debe terminar el bucle principal del menú
2. Debe mostrar un mensaje de despedida amigable
3. El programa debe finalizar su ejecución limpiamente
4. Todos los datos deben estar guardados antes de salir (se guardan automáticamente en cada operación)

#### Escenarios de Prueba

**Escenario 1: Salida normal**
- **Dado** que el usuario está en el menú principal
- **Cuando** selecciona la opción 8 (Salir)
- **Entonces** el sistema debe mostrar "Gracias por usar el sistema. ¡Hasta luego!"
- **Y** el programa debe finalizar

#### Prioridad
**Media** - Necesaria para buena experiencia de usuario

---

## Historias Técnicas

### HT-001: Persistencia en CSV

**Como** desarrollador
**Quiero** implementar la carga y guardado de datos en formato CSV
**Para** mantener la información persistente entre sesiones del programa

#### Criterios Técnicos

1. Utilizar módulo `csv` de Python
2. Formato de archivo: `titulo,cantidad_ejemplares`
3. Codificación UTF-8 para soportar caracteres especiales
4. Carga automática al iniciar el programa
5. Guardado automático después de cada operación de escritura
6. Manejo de archivo inexistente (primera ejecución)

---

### HT-002: Sincronización de Listas Paralelas

**Como** desarrollador
**Quiero** mantener sincronizadas las listas `titulos[]` y `ejemplares[]`
**Para** garantizar la integridad de los datos del catálogo

#### Criterios Técnicos

1. Ambas listas deben tener siempre la misma longitud
2. El índice `i` en `titulos[i]` debe corresponder a `ejemplares[i]`
3. Toda operación de inserción debe actualizar ambas listas
4. Toda operación de modificación debe preservar la sincronización
5. No se permiten operaciones que rompan la correspondencia índice-a-índice

---

## Restricciones Técnicas del Proyecto

### Estructuras Permitidas
- ✅ Bucle `while` para navegación del menú
- ✅ Estructura `match` para el menú
- ✅ Estructuras condicionales (`if`, `elif`, `else`)
- ✅ Funciones para modularización
- ✅ Listas y diccionarios
- ✅ Funciones de validación: `lower()`, `upper()`, `isdigit()`, `strip()`

### Estructuras Prohibidas
- ❌ Excepciones (`try`/`except`)
- ❌ Clases (POO)
- ❌ Funciones lambda
- ❌ Type hints del módulo `typing`

### Tecnologías
- **Lenguaje:** Python 3.10+ (requerido para `match`/`case`)
- **Persistencia:** Archivos CSV
- **Módulos:** Solo biblioteca estándar de Python

---

## Definición de "Hecho" (Definition of Done)

Una historia de usuario se considera completada cuando:

1. ✅ Todo el código cumple con las restricciones técnicas del proyecto
2. ✅ Todos los criterios de aceptación han sido implementados
3. ✅ Todos los escenarios de prueba pasan exitosamente
4. ✅ El código está modularizado en funciones con nombres descriptivos
5. ✅ Las listas paralelas se mantienen sincronizadas correctamente
6. ✅ Los datos se persisten correctamente en el archivo CSV
7. ✅ Los mensajes al usuario son claros y en español
8. ✅ Se validan todas las entradas del usuario
9. ✅ No se utilizan estructuras prohibidas (excepciones, clases, lambdas)

---

## Glosario

**Listas Paralelas:** Dos o más listas que mantienen información relacionada usando el mismo índice para acceder a elementos correspondientes.

**Sincronización de Listas:** Garantía de que las listas paralelas tienen la misma longitud y que los elementos en el mismo índice corresponden al mismo registro lógico.

**Persistencia:** Capacidad de guardar datos de forma que sobrevivan al cierre del programa.

**Validación de Entrada:** Proceso de verificar que los datos ingresados por el usuario cumplen con el formato y restricciones esperados.

---

## Priorización de Desarrollo

### Sprint 1 (Funcionalidad Base)
1. HU-001: Ingresar Títulos Iniciales
2. HU-002: Ingresar Ejemplares
3. HU-003: Mostrar Catálogo
4. HT-001: Persistencia en CSV
5. HT-002: Sincronización de Listas Paralelas

### Sprint 2 (Funcionalidad Operativa)
6. HU-006: Agregar Nuevo Título
7. HU-007: Actualizar Ejemplares (Préstamo/Devolución)
8. HU-004: Consultar Disponibilidad

### Sprint 3 (Funcionalidad Complementaria)
9. HU-005: Listar Libros Agotados
10. HU-008: Salir del Sistema

---

**Documento preparado para:** Proyecto SegPar - Sistema de Gestión de Biblioteca Escolar
**Última actualización:** Octubre 2025
**Estado:** Aprobado e Implementado