A,B,C,D =map(int,input().split())
if C<B:
    if A<D:
       if A+B<C+D:
           if A%2==0:
               print("Valores aceitos")
           else:
                print("Valores nao aceitos")
       else:
            print("Valores nao aceitos")
    else:
        print("Valores nao aceitos")
else:
    print("Valores nao aceitos")