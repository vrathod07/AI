
# move n-1 disc to aux rod
# move last disc to final rod
# move n-1 disc to base rod
# move n-2 disc to aux rod
# move last disc to final rod
#repeat till everything is over


n = int(input("Enter the number of disc: "))

# creating the source rod

def solve(n,source_rod,aux_rod,dest_rod):

    if n == 1:
        print("Move disk: 1 from source rod to destination rod")
        return
    solve(n-1,source_rod,aux_rod,dest_rod)
    print("Move disc",n," from aux rod to source rod")
    solve(n-1, aux_rod,dest_rod,source_rod)


#after  function call
solve(n,"A","C","B")


