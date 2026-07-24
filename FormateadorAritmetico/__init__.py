def arithmetic_arranger(problems, show_answers=False):
    # Regla 1: Validar el límite de problemas
    if len(problems) > 5:
        return 'Error: Too many problems.'

    linea1 = []
    linea2 = []
    lineas_guiones = []
    linea_resultados = []

    for problem in problems:
        partes = problem.split()
        op1 = partes[0]
        operador = partes[1]
        op2 = partes[2]

        # Regla 2: Validar los operadores permitidos
        if operador not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # Regla 3: Validar que solo contengan dígitos
        if not (op1.isdigit() and op2.isdigit()):
            return 'Error: Numbers must only contain digits.'

        # Regla 4: Validar longitud máxima de 4 dígitos
        if len(op1) > 4 or len(op2) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        # Calcular el ancho total de este bloque del problema
        ancho = max(len(op1), len(op2)) + 2

        # Formatear cada componente alineado a la derecha
        linea1.append(op1.rjust(ancho))
        linea2.append(operador + op2.rjust(ancho - 1))
        lineas_guiones.append('-' * ancho)

        # Calcular el resultado en caso de ser requerido
        if show_answers:
            resultado = str(int(op1) + int(op2)) if operador == '+' else str(int(op1) - int(op2))
            linea_resultados.append(resultado.rjust(ancho))

    # Unir los componentes de cada problema con exactamente 4 espacios de separación
    formato_final = (
        "    ".join(linea1) + "\n" +
        "    ".join(linea2) + "\n" +
        "    ".join(lineas_guiones)
    )

    if show_answers:
        formato_final += "\n" + "    ".join(linea_resultados)

    return formato_final
