def exists_word(word, instance):
    for i in range(len(instance)):
        if word not in instance.search(i):
            return []


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
