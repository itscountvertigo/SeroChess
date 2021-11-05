from pieces import king, queen, rook, bishop, knight, pawn

def read_FEN(FEN_code):
    output_FEN=[]
    FENlist=list(FEN_code)
    X=0
    Y=7
    #println(FENlist)
    for i in range(len(FENlist)):
        if Y>-1 and X<9:
            if FENlist[i]=='/':
                #print("hoi")
                X=0
                Y -= 1
                #println(Y)
                #black pieces
            elif FENlist[i]=='r':
                output_FEN.append(rook.Rook(X, Y, 0))
                X+=1
            elif FENlist[i]=='n':
                output_FEN.append(knight.Knight(X, Y, 0))
                X+=1
            elif FENlist[i]=='b':
                output_FEN.append(bishop.Bishop(X, Y, 0))
                X+=1
            elif FENlist[i]=='q':
                output_FEN.append(queen.Queen(X, Y, 0))
                X+=1
            elif FENlist[i]=='k':
                output_FEN.append(king.King(X, Y, 0))
                X+=1
            elif FENlist[i]=='p':
                output_FEN.append(pawn.Pawn(X, Y, 0))
                X+=1

                #wite pieces
            elif FENlist[i]=='R':
                output_FEN.append(rook.Rook(X, Y, 1))
                X+=1
            elif FENlist[i]=='N':
                output_FEN.append(knight.Knight(X, Y, 1))
                X+=1
            elif FENlist[i]=='B':
                output_FEN.append(bishop.Bishop(X, Y, 1))
                X+=1
            elif FENlist[i]=='Q':
                output_FEN.append(queen.Queen(X, Y, 1))
                X+=1
            elif FENlist[i]=='K':
                output_FEN.append(king.King(X, Y, 1))
                X+=1
            elif FENlist[i]=='P':
                output_FEN.append(pawn.Pawn(X, Y, 1))
                X+=1
            elif FENlist[i]==' ':
                Y-=1
            else:
                for j in range(48,57):
                    if FENlist[i]==chr(j):
                        X+=j-48
        #print(X)
    return output_FEN