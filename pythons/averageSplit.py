def split_array(array:list, parts:int) -> list[list]:
    if array == []:
        return []
    if parts == 0:
        return [array]

    length = len(array)
    parts = min(parts, length)

    res_lst = []

    # if length%parts == 0:
    #     part_length = length//parts
    #     lst = []
    #     for i in range(0, parts):
    #         lst = array[i * part_length: i * part_length + part_length]
    #         res_lst.append(lst)

    # else:
    part_length = length // parts
    len_lst = []
    remain = length % parts
    for i in range(parts):
        if i < remain:
            len_lst.append(part_length + 1)
        else:
            len_lst.append(part_length)

    left,right = 0, 0
    for i in range(parts):
        right += len_lst[i]
        res_lst.append(array[left:right])
        left = right
    return res_lst