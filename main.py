from knowledge_base import infos, bp_info


if __name__ == "__main__":
    lst = infos()
    name = lst[0]
    age = lst[1]
    gender = lst[2]
    print(f'{name} {age} {gender}')
    bp_info(lst[0])

