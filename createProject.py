import os

name = input('Digite o nome do seu projeto: ')

def changeRow(path, indexLine, newLine):
    with open(path,'r') as f:
        text = f.readlines()
    with open(path,'w') as f:
        for i in text:
            if text.index(i) == indexLine:
                f.write(f'{ newLine } \n')
            else:
                f.write(i)

def findString(path, string):
    with open(path,'r') as f:
        texto = f.readlines()
    for i in texto:
        if string in i:
            return texto.index(i)

    return False

def writeArchive(path, string):
   a = open(path, 'a')
   a.write(string)
   a.close()

settings = [
    ['LANGUAGE_CODE',           "LANGUAGE_CODE = 'pt-br'"],
    ["'DIRS':" ,                "        'DIRS': [os.path.join(BASE_DIR, 'templates')],"],
    ['TIME_ZONE',               "TIME_ZONE = 'America/Sao_Paulo'"],
    ['MEDIA_URL',               "\n\nMEDIA_URL = '/media/'"],
    ['LOGIN_REDIRECT_URL',      "\n\nLOGIN_REDIRECT_URL = '/'"],
    ['LOGOUT_REDIRECT_URL',     "\n\nLOGOUT_REDIRECT_URL = '/accounts/login/'"],
    ['STATICFILES_DIRS',        f"\n\nSTATICFILES_DIRS = [ os.path.join(BASE_DIR, '{ name }/static'), ]"],
    # [14,                        'import os'],
]

for setting in settings:
    print(f'{ name }/{ name }/settings.py')
    print(setting[0])
    print(setting[1])
    print('-'*80)
    line = findString(f'{ name }/{ name }/settings.py', setting[0])
    
    if line:
        changeRow(f'{ name }/{ name }/settings.py', line, setting[1])

    else:
        # num_lines = sum(1 for line in open('te/te/settings.py'))
        writeArchive(f'{ name }/{ name }/settings.py', setting[1])

        # changeRow(f'{ name }/{ name }/settings.py', num_lines + 1, setting[1])


# def startProject(name):
#     result = os.system(f'python "C:\Python38\Scripts\django-admin.py" startproject { name }')

#     if (result == 0):
#         print('Projeto criado com sucesso!')
#         print('Iniciando configurações...')
#     else:
#         print('Erro! Tente novamente.')
#         startProject(input('Digite o nome do seu projeto: '))

# startProject(name)