--Team Member
--Rohan Ballapragada, Chih-Hao Feng, Roshan Panah, Ming Wei, Zhangyao Zhou.hs

module HW3 where















--Exercise 2

data Cmd = Pen Mode
     | Moveto Int Int 
     | Seq Cmd Cmd
     deriving Show



data Mode = Up | Down
  deriving Show
type State = (Mode,Int,Int)
type Line = (Int,Int,Int,Int)
type Lines = [Line]


semS :: Cmd -> State -> (State,Lines)
semS (Pen n) (n1,s1,s2) = ((n,s1,s2),[(s1,s2,s1,s2)])
semS (Moveto t1 t2) (n1,s1,s2) = ((n1,t1,t2),[(s1,s2,t1,t2)])
semS (Seq c1 c2) st = (so, lo) where
  (s1, l1) = semS c1 st
  (s2, l2) = semS c2 s1
  so = s2
  lo = l1 ++ l2 



sem' :: Cmd -> Lines
sem' a = n2 where
  (_,n2) = semS a (Up, 0, 0)
  
  
  