import sys


def txt_importer(path_file):
    if not path_file.endswith(".txt"):
        return sys.stderr.write("Formato inválido\n")

    try:
        with open(path_file, mode="r") as file:
            return file.read().split("\n")
    except Exception:
        return sys.stderr.write(f"Arquivo {path_file} não encontrado\n")


print(txt_importer("statics/arquivo_teste.txt"))
print()
print(txt_importer("statics/nome_pedro.txt"))