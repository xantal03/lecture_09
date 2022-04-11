import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name) # z os ziskal cwd, do neho ulozil aktualny pracovny adresar

    if field not in {"unordered_numbers","ordered_numbers","dna_sequence"}:
        return None

    with open(file_path, 'r') as subor:
        slovnicek = json.load(subor)

    return slovnicek[field]


def linear_search(seq, number):
    pom = list()
    count = 0
    for i in range(len(seq)):
        if seq[i] == number:
            pom.append(i)
            count += 1

    return {
        'positions': pom,
        'count': count
    }




def main():
    file_name = 'sequential.json'
    sequential_data = read_data(file_name, 'unordered_numbers')
    print(sequential_data)
    print(linear_search(sequential_data, number=5))
    pass


if __name__ == '__main__':
    main()