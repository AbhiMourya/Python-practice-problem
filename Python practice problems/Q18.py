def direction(lst):
    n_count=lst.count("NORTH")
    s_count=lst.count("SOUTH")
    e_count=lst.count("EAST")
    w_count=lst.count("WEST")
    while 1 :
        if n_count>=1 and s_count>=1:
            lst.remove('NORTH')
            lst.remove('SOUTH')
            n_count = lst.count("NORTH")
            s_count = lst.count("SOUTH")
        elif e_count>=1 and w_count>=1:
            lst.remove('EAST')
            lst.remove("WEST")
            e_count = lst.count("EAST")
            w_count = lst.count("WEST")
        else:
           return(lst)



print(direction(["NORTH","SOUTH","SOUTH","EAST","WEST","NORTH","WEST"]))