def add():
    titulo = input("Qual o titulo da tarefa: ")
    descricao = input("Descreva sua tarefa: ")

    with open ('tarefas.json', 'a') as f:
        f.write(titulo + "|" + descricao + "|False\n")

def view():
    try:
        with open('tarefas.json' , 'r') as r:
            for line in r.readlines():
                tarefas = line.rstrip()
                titulo, descricao, concluida = tarefas.split("|")
                if concluida == "True":
                    status = "[X]"
                else:
                    status = "[]"
                print(f"{status} Título:, {titulo}, Descriçao:  {descricao}")
                print()
                
    except FileNotFoundError:
        print("Nenhuma tarefa encontrada. Adicione uma nova tarefa.")

def concluir():
    view()
    tarefa_conclusao = input("Qual tarefa deseja concluir?: ")

    with open ('tarefas.json' , 'r') as f:
        linhas = f.readlines()
    with open ('tarefas.json' , 'w') as f:
        for line in linhas:
            tarefas = line.rstrip()
            titulo, descricao, concluida  = tarefas.split("|")
            if tarefa_conclusao == titulo:
                f.write(titulo + "|"+ descricao + "|True\n")
            else:
                f.write(line)

def remover():
    view()
    remoçao = input("Qual tarefa deseja remover?: ")
    
    with open('tarefas.json', 'r') as f:
        linhas = f.readlines()

    with open('tarefas.json', 'w') as f:
        for line in linhas:
            tarefas = line.rstrip()
            titulo, descricao, concluida = tarefas.split("|")
            if remoçao != titulo:
                f.write(line)

while True:
    print("1. Adicionar nova tarefa \n 2. Listar tarefas \n 3. Marcar tarefa como concluída \n 4. Remover tarefa \n 5. Sair")
    escolha = int(input("Escolha uma opção: "))

    match escolha:
        case 1:
            add()
        case 2:
            view()
        case 3:
            concluir()
        case 4:
            remover()
        case 5:
            quit()