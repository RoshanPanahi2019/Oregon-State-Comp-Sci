
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













