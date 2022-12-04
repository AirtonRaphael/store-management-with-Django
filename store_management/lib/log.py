def log(erro):
    arq = f'/home/ceto/Estudos/Projetos/Djang/Controle_de_estoque/store_management/error.log'
    with open(arq, 'a', encoding='utf=8') as f:
        f.write(f"\n{erro}")