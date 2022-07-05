type Prog = [Cmd]
data Cmd = LD Int | ADD | MULT | DUP | DEC | SWAP | POP Int

type Rank = Int
type CmdRank = (Int,Int)
rankC :: Cmd -> CmdRank
rankC (LD a)= (0,1)
rankC ADD=(2,1)
rankC MULT=(2,1)
rankC DUP=(1,1)
rankC DEC=(1,1)
rankC SWAP=(2,2)
rankC (POP k)=(k,0)


--rank :: Prog -> Rank -> Maybe Rank
--rank []=0
--rank (x:xs)=1+rankf (xs)

--rankf:: Stack -> Rank
--rankf []=0
--rankf (x:xs)=1+rankf (xs)



--rankP :: Prog -> Maybe Rank
--rankP (c:cs) stck = (b-a)+rankP(cs) 
--                    where (a,b) =rankC(c)



--------------------exercise 2-a:
data Shape = X
           | TD Shape Shape
           | LR Shape Shape
             deriving Show

type BBox = (Int,Int)
bbox :: Shape -> BBox
bbox X =  (1,1)
bbox (TD sh1 sh2) = (maximum[x1,x2],y1+y2)
                    where (x2,y2)=bbox(sh2)
                          (x1,y1)=(bbox sh1)

bbox (LR sh1 sh2) = (x1+x2,maximum[y1,y2])
                    where (x2,y2)=bbox sh2
                          (x1,y1)=bbox sh1

--------------------exercise 2-b :
rect :: Shape -> Maybe BBox
rect(TD sh1 sh2)  | x1==x2 = Just(maximum[x1,x2],y1+y2)
                  |otherwise=Nothing
                  where (x2,y2)=bbox(sh2)
                        (x1,y1)=(bbox sh1)
rect (LR sh1 sh2) | y1==y2 = Just(x1+x2,maximum[y1,y2])
                  |otherwise=Nothing
                  where (x2,y2)=bbox sh2
                        (x1,y1)=bbox sh1













