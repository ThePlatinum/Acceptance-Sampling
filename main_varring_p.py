c1 = int(input("C1: "))
c2 = int(input("C2: "))
n1 = int(input("Sample size 1: "))
n2 = int(input("Sample size 2: "))


for i in range(1, 10):
    p = i/100
    q = 1 - p
    def permutation(n, x):
        final = 0
        for j in range(0, x + 1):
            n_fac = 1
            x_fac = 1
            n_x_fac = 1
            for i in range(1, n + 1):
                n_fac = n_fac * i
            for i in range(1, j + 1):
                x_fac = x_fac * i
            for i in range(1, n - j + 1):
                n_x_fac = n_x_fac * i
            p_x = p ** int(j)
            q_x = q ** int(n - j)

            the_fac = n_fac / (x_fac * n_x_fac)
            final = final + (the_fac * p_x * q_x)

        return final


    def permutation_fixed(n, j):
        n_fac = 1
        x_fac = 1
        n_x_fac = 1
        for i in range(1, n + 1):
            n_fac = n_fac * i
        for i in range(1, j + 1):
            x_fac = x_fac * i
        for i in range(1, n - j + 1):
            n_x_fac = n_x_fac * i
        p_x = p ** int(j)
        q_x = q ** int(n - j)

        the_fac = n_fac / (x_fac * n_x_fac)
        fac = (the_fac * p_x * q_x)
        return fac


    partial = 0
    for i in range(1, c2):
        d1 = c1 + i
        for_d1 = permutation_fixed(n1, d1)

        d2 = c2 - (c1 + i)
        for_d2 = permutation(n2, d2)

        partial = partial + for_d1 * for_d2


    for1 = permutation_fixed(n1, c2)
    for2 = permutation(n2, 0)
    cons = for1 * for2 + partial

    pa1 = permutation(n1, c1)

    print("Using p = ", p)
    print("The Pa1 is: ", format(pa1,'.4f'))
    print("The Pa2 is: ", format(cons,'.4f'))
    pa = cons + pa1
    print("Thus the Probablity of acceptance 'Pa' is:", format(pa,'.4f'))
    print("")
    
