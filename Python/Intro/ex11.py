##Ex 11 :  écrire un programme qui retourne la somme de
##chacune des listes d’une liste.
##liste= [ [1,3,4,2] , [1,4,6,2] ,[2,7,9,1] , [1,2,0,0] ]

lst_num = [ [1,3,4,2] , [1,4,6,2] ,[2,7,9,1] , [1,2,0,0] ]

def add_lst(lst):
    sum_tot, sum_of_a_lst = 0, 0
    lst_sum = []

    for e in lst:

        for nb in e:
            sum_tot += nb

            sum_of_a_lst += nb

        lst_sum.append(sum_of_a_lst)
        sum_of_a_lst = 0

    return lst_sum, sum_tot

print( add_lst(lst_num) )
