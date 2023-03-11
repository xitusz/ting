import sys
from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue


def process(path_file, instance):
    for i in range(len(instance)):
        if instance.search(i)["nome_do_arquivo"] == path_file:
            return

    result = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(txt_importer(path_file)),
        "linhas_do_arquivo": txt_importer(path_file)
    }

    instance.enqueue(result)

    print(result)


queue = Queue()
process("statics/arquivo_teste.txt", queue)
print()

def remove(instance):
    if not instance:
        return print('Não há elementos')

    path_file = instance.dequeue()

    print(f'Arquivo {path_file["nome_do_arquivo"]} removido com sucesso')

remove(queue)
print()

def file_metadata(instance, position):
    try:
        print(instance.search(position))
    except Exception:
        return sys.stderr.write('Posição inválida')


process("statics/nome_pedro.txt", queue)
print()
file_metadata(queue, 0)