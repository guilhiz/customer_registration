from fastapi import HTTPException

def calculate_digit(cpf, end, weight):
    total = 0
    for i in range(end):
        total += int(cpf[i]) * (weight - i)

    remainder = total % 11
    return 0 if remainder < 2 else 11 - remainder

def validate_cpf(cpf):
    if not cpf.replace('.', '').replace('-', '').isdigit():
        raise HTTPException(status_code=400, detail="CPF must contain only numbers.")

    cleaned_cpf = ''.join(filter(str.isdigit, cpf))
    if len(cleaned_cpf) != 11:
        raise HTTPException(status_code=400, detail="Please check and enter a valid 11-digit CPF.")

    digit1 = calculate_digit(cleaned_cpf, 9, 10)
    digit2 = calculate_digit(cleaned_cpf, 10, 11)

    if digit1 != int(cleaned_cpf[9]) or digit2 != int(cleaned_cpf[10]):
        raise HTTPException(status_code=422, detail="Invalid CPF")

    return cleaned_cpf
