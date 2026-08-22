def spiral(a):
    spiral=[]
    start_row=0
    start_col=0
    end_row=len(a)-1
    end_col=len(a[0])-1
    while start_row<=end_row and start_col<=end_col:
    #top
        for i in range(start_col,end_col+1):
            spiral.append(a[start_row][i])
        start_row+=1
    #right- row changing, t to b
        for i in range(start_row,end_row+1):
            spiral.append(a[i][end_col])
        end_col-=1
    #bottom-column changing,r to l
        for i in range(end_col,start_col-1,-1):
            spiral.append(a[end_row][i])
        end_row-=1
    #left-row is changing
        for i in range(end_row,start_row-1,-1):
            spiral.append(a[i][start_col])
        start_col+=1
    print(spiral)

a= [[ 1, 2, 3, 4 ],[5, 6, 7, 8 ],[9, 10, 11, 12 ],[13, 14, 15, 16 ]]
spiral(a)
#Time-O(mxn)
#Space-O(1)