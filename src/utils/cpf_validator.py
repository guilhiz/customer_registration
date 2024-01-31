from fastapi import HTTPException

def validate_cpf(cpf):
    # Remove caracteres não numéricos do CPF
    if not cpf.replace('.', '').replace('-', '').isdigit():
        raise HTTPException(status_code=400, detail="CPF deve conter apenas números.")
    print(cpf)
    cleaned_cpf = ''.join(filter(str.isdigit, cpf))
    print(cpf)
    # Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        raise HTTPException(status_code=400, detail="Verifique e insira um CPF válido com 11 números.")

    # Cálculo do primeiro dígito verificador
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = soma % 11
    digito1 = 0 if resto < 2 else 11 - resto

    # Cálculo do segundo dígito verificador
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    resto = soma % 11
    digito2 = 0 if resto < 2 else 11 - resto

    # Verifica se os dígitos calculados são iguais aos dígitos informados no CPF
    if digito1 != int(cpf[9]) or digito2 != int(cpf[10]):
        raise HTTPException(status_code=400, detail="CPF inválido")

    return cleaned_cpf
