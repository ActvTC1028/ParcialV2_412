# List of tuples
# Each tuple contains a test: the first element are the inputs, the second are the output, and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    # Test case 1
    (
        # Inputs
        ["4","25", "134", "110", "-20"],
        # Outputs
        ["Cantidad de números: ", "Número 1: ","Número 2: ", "Número 3: ","Número 4: ", "La suma de números entre -100 y 100 es: 5"],
        # Message in case of failure
        "Revisa que estes identificando y sumando sólo los que están entre -100 y 100"
    ),
    # Test case 2
    (
       # Inputs
        ["3", "12", "34", "-100"],
        # Outputs
        ["Cantidad de números: ", "Número 1: ","Número 2: ", "Número 3: ", "La suma de números entre -100 y 100 es: -54"],
        # Message in case of failure
        "Revisa que estes identificando y sumando sólo los que están entre -100 y 100"
    ),
    # Test case 3
    (
        # Inputs
        ["0"],
        # Outputs
        ["Cantidad de números: ", "La cantidad de números debe ser mayor a 0"],
        # Message in case of failure
        "Revisa que estes identificando y sumando sólo los que están entre -100 y 100"
    ),
    # Test case 4
    (
        # Inputs
        ["1","-3"],
        # Outputs
        ["Cantidad de números: ", "Número 1: ", "La suma de números entre -100 y 100 es: -3"],
        # Message in case of failure
        "Revisa que estes identificando y sumando sólo los que están entre -100 y 100"
    )
]