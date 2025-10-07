# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Sistema de gestión de biblioteca escolar (SegPar) - A simple library management system for cataloging books and tracking available copies. This is an educational project that implements a menu-based interface using parallel lists.

## Architecture

The project uses **parallel lists** as the core data structure:
- `titulos[]`: List of book titles
- `ejemplares[]`: List of copy counts for each title

**Critical constraint**: Both lists must remain synchronized - the title at index `i` in `titulos[]` must correspond to the number of copies at index `i` in `ejemplares[]`.

Example:
```python
titulos = ["El Señor de los Anillos", "Orgullo y Prejuicio", "Matar un Ruiseñor"]
ejemplares = [5, 3, 7]
```

## Technical Requirements and Restrictions

**Required structures:**
- `while` loop for menu navigation
- `match` statement for menu options
- Functions for code modularization
- Lists and dictionaries
- CSV files for data persistence

**Strictly prohibited** (will result in maximum 10% grade):
- Exception handling (try/except)
- Classes (OOP)
- Lambda functions
- Type hints from `typing` module

**Allowed**:
- String validation functions: `lower()`, `upper()`, `isdigit()`, `strip()`
- Conditional and sequential structures
- Dictionaries for configuration

## Menu Functionality

1. **Ingresar títulos**: Add initial book titles (user specifies initial quantity)
2. **Ingresar ejemplares**: Add copy counts for each title
3. **Mostrar catálogo**: Display all books with current stock
4. **Consultar disponibilidad**: Search for a specific title and show available copies
5. **Listar agotados**: Show titles with 0 copies
6. **Agregar título**: Add new book with its copies to catalog (maintain list synchronization)
7. **Actualizar ejemplares**: Modify stock for loans/returns
   - **Préstamo** (Loan): Decrease copies by 1 (if sufficient stock)
   - **Devolución** (Return): Increase copies by 1
8. **Salir**: Exit program

## Running the Application

```bash
# Activate virtual environment (if using one)
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate

# Run the application
python main.py
```

No external dependencies required - uses only Python standard library.

## Data Persistence

**File:** `catalogo.csv`
**Format:** `titulo,cantidad_ejemplares`
**Encoding:** UTF-8

The CSV file is automatically:
- Created on first write operation
- Loaded when the program starts (in `main()` via `cargar_datos()`)
- Saved after every modification (via `guardar_datos()`)

Example CSV content:
```csv
El Señor de los Anillos,5
Orgullo y Prejuicio,3
Matar un Ruiseñor,7
```

## Code Structure

**Main file:** `main.py` (265 lines)

**Global variables:**
- `titulos[]`: List of book titles
- `ejemplares[]`: List of copy counts (parallel to titulos)
- `ARCHIVO_CSV`: Constant for CSV filename

**Key functions:**
- `cargar_datos()`: Loads CSV into parallel lists at startup
- `guardar_datos()`: Saves parallel lists to CSV
- `main()`: Entry point with while loop and match statement
- 8 menu functions (one per menu option)

**Important implementation details:**
- All arithmetic operations use explicit syntax (e.g., `ejemplares[i] = ejemplares[i] + cantidad` instead of `+=`)
- Case-insensitive search uses `.lower()` method
- Input validation uses `.isdigit()` and `.strip()`
- No exception handling - validation is done before operations

## When Modifying Code

**Always remember:**
1. Maintain parallel list synchronization at ALL times
2. Never use try/except, classes, lambda, or type hints
3. Always call `guardar_datos()` after modifying data
4. Use `match` statement for menu options (not if/elif chains)
5. Validate user input before processing
6. Keep messages in Spanish

**Common pitfalls to avoid:**
- Adding to one list but forgetting the parallel list
- Using `+=` operator (use explicit addition instead)
- Using list comprehensions with lambdas
- Adding exception handling "just in case"
- Using augmented assignment operators (`+=`, `-=`, `*=`, etc.)
- Importing modules not in standard library

## Project Files

```
SegPar/
├── main.py                    # Main application (265 lines)
├── catalogo.csv               # Data persistence (auto-generated)
├── info                       # Original requirements (Spanish)
├── HISTORIAS_USUARIO.md       # User stories with acceptance criteria
├── CLAUDE.md                  # This file
└── .venv/                     # Virtual environment (optional)
```

## Documentation

- `info`: Original project requirements (Spanish)
- `HISTORIAS_USUARIO.md`: Complete user stories with acceptance criteria and test scenarios
- `CLAUDE.md`: This file - architecture and development guidance

## Python Version

Requires **Python 3.10+** for `match`/`case` syntax support.