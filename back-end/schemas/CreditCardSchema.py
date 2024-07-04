from datetime import datetime
from pydantic import BaseModel
from pydantic import field_validator


class CreditCardSchema(BaseModel):
    titular_name: str
    number: str
    cvc: str
    user_id: int
    expiry_date: str
    
    '''
    Verifica que el nombre solo contenga letras y punto
    '''

    @field_validator("titular_name")
    def validateName(cls, titular_name):
        if not all(c.isalpha() or c.isspace() or c == '.' for c in titular_name):
            raise ValueError("El nombre solo debe contener letras, espacios y puntos")
        return titular_name

    '''
    VALIDA SI EL NÚMERO DE LA TARJETA ES UN NÚMERO VÁLIDO POR MEDIO DEL ALGORITMO
    DE LUHN QUE CONSISTE EN QUE OBTENIENDO LA REVERSA DE UN NÚMERO  Y LA SUMA DE 
    SUS DIGITOS DEBE SER MÚLTIPLO DE 0

    EJEMPLO:
    Número de ejemplo: 49927398716
    Se multiplica por 2 los dígitos que ocupan las posiciones pares empezando por el final: 
    (1*2) = 2, (8*2) = 16, (3*2) = 6, (2*2) = 4, (9*2) = 18
    Se suman los dígitos que ocupan las posiciones impares con los dígitos de los productos 
    obtenidos: 6 + (2) + 7 + (1+6) + 9 + (6) + 7 + (4) + 9 + (1+8) + 4 = 70. (1+6) es por 
    la multiplicación de 8x2 y (1+8) es por la multiplicación de 9x2 del primer punto
    Si el resto de dividir el total entre 10 es igual a cero, el número es correcto: 
    70 mod 10 = 0

    Número para probar: 4539 1488 0343 6467 ----> Valido
    Numero para probar: 4539 1488 0343 6466 ----> Invalido
    '''
    @field_validator("number")
    def verificateNumberCard(cls, number):
        # Eliminar espacios en blanco
        number = number.replace(" ", "")
        
        # Convertir cada dígito a un entero
        digitos = [int(d) for d in number]

        # Aplicar el algoritmo de Luhn
        for i in range(len(digitos)-2, -1, -2):
            digitos[i] *= 2
            if digitos[i] > 9:
                digitos[i] -= 9
        
        suma = sum(digitos)

        # Verificar que la suma sea divisible por 10 y que el número tenga 16 dígitos
        if suma % 10 != 0 or len(digitos) != 16:
            raise ValueError("Número de tarjeta inválido")
        
        return number
    
    '''
    Verifica que la fecha de la tarjeta sea posterior a la fecha actual y que sea en el formato
    MM/YY
    '''
    @field_validator("expiry_date")
    def validate_date(cls, expiry_date):
        try:
            exp_date = datetime.strptime(expiry_date, "%m/%y")
        except ValueError:
            raise ValueError("La fecha debe tener el formato MM/YY")
        
        if exp_date < datetime.now():
            raise ValueError("La fecha de expiración debe ser posterior a la fecha actual")
        
        return expiry_date

    '''
    Verifica que el CVC sea solo números de 3 o 4 cifras
    Ejemplo:
    123 : retorna 123
    1: retorna Error
    '''
    @field_validator("cvc")
    def validate_cvc(cls, cvc):
        if not cvc.isdigit() or len(cvc) not in (3, 4):
            raise ValueError("El CVC debe ser un número de 3 o 4 dígitos")
        return cvc

