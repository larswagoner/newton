#The input should be structured as follows:
#In the first line enter the polynomial
#The polynomial x^3 - 4*x + 5 is 1 3 -4 1 5 0.
#The second line should contain the number of iterations for Newton's Method
#The third line should contain an initial approximation of the root.
#Save to a .txt file in the same directory as this .py


#obtains coefficients and exponents of the polynomial
def deconstruct_polynomial(polynomial):
    polynomial = polynomial.split()
    coefficients = [int(coefficient) for coefficient in polynomial[0::2]]
    exponents = [int(exponent) for exponent in polynomial[1::2]]

    return coefficients, exponents


def differentiate_polynomial(coefficients, exponents):
    new_coefficients = []

    for coefficient, exponent in zip(coefficients, exponents):
        new_coefficients += [coefficient * exponent]

    exponents = [number - 1 if number != 0 else 0 for number in exponents]

    return new_coefficients, exponents


def evaluate_polynomial(coefficients, exponents, variable):
    result = 0
    for coefficient, exponent in zip(coefficients, exponents):
        result += coefficient * (variable ** exponent)

    return result


def approximate_root(polynomial, repetitions, approximation):
    coefficients, exponents = deconstruct_polynomial(polynomial)
    deriv_coeffs, deriv_exponents = differentiate_polynomial(coefficients, exponents)

    if repetitions == 0:
        return approximation

    evaluated_polynomial = evaluate_polynomial(coefficients, exponents, approximation)
    evaluated_derivative = evaluate_polynomial(deriv_coeffs, deriv_exponents, approximation)
    approximation -= (evaluated_polynomial / evaluated_derivative)

    return approximate_root(polynomial, repetitions - 1, approximation)


def start_approx(file_name):
    lines = open(file_name).read().splitlines()
    polynomial = lines[0]
    repetitions = int(lines[1])
    approximation = float(lines[2])
    approximation = approximate_root(polynomial, repetitions, approximation)

    print('After using Newton\'s method %d times, the approximated root is x = %.1f.' % (repetitions, approximation))


#start
file_name = input('Enter the file name to use Newton\'s method: ')
start_approx(file_name)
