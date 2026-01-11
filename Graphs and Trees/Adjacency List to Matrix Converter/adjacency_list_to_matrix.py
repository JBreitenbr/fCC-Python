def adjacency_list_to_matrix(dict):
    mat=[]
    l=len(dict.keys())
    for i in range(l):
        mat.append([])
        for j in range(l):
           mat[i].append(0)
    for i in dict.keys():
        for j in range(len(dict[i])):
            mat[i][dict[i][j]]=1
    print(mat)
    return mat
adjacency_list_to_matrix({0: [1, 2], 1: [2], 2: [0, 3],3:[2]})
