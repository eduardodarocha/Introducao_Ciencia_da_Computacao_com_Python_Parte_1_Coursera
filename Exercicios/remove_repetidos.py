def remove_repetidos(lis):
    listanova = []
    for item in lis:
        if item not in listanova:
            listanova.append(item)
    return sorted(listanova)