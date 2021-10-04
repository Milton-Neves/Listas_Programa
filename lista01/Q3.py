def validar_phone(phone, formatar=True):
    phone_sem_hifen = phone.replace('-', '')
    qtd_caracteres = len(phone_sem_hifen)
    phone_validado = phone_sem_hifen

    if qtd_caracteres < 8:
        print(f'Telefone possui {qtd_caracteres} dígitos.')
        caracteres_faltantes = 8 - qtd_caracteres
        phone_validado = caracteres_faltantes * '3' + phone_sem_hifen

    if formatar:
        phone_validado = phone_validado[0:4] + '-' + phone_validado[4:8]

    return phone_validado

if __name__ == '__main__':
    print('Informe o número de telefone COM 8 DÍGITOS para validação')
    print('Telefone (SEM HIFEN):')
    telefone = str(input())

    print('|-----------------------------------------------|')

    print('>>>> Telefone corrigido com formatação:', validar_phone(telefone))

    print('|--- FIM DA APLICAÇÃO ---|')