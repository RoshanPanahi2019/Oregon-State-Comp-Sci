module HW2types where

import Data.List (nub,sort)

--Exercise 1

--(a)



data Cmd = Pen Mode
     | Moveto Pos Pos
     | Def String Pars Cmd
     | Call String Vals
     | Cd Cmd Cmd



data Mode = Up | Down
data Pos = Pnum Int | Pname String
type Pars = [String]
type Vals = [Int]


--(b)

vector = Def "vector" ["x1","y1","x2","y2"] (Cd (Moveto (Pname "x1") (Pname "y1")) (Cd (Pen Down) (Cd (Moveto (Pname "x2") (Pname "y2")) (Pen Up))))

--(c)

steps :: Int -> Cmd
steps 0 = Pen Up
steps n = Cd (Cd (Cd (Cd (Cd (Moveto(Pnum n, Pnum n)) Pen Down) Moveto(Pnum n, Pnum (n-1))) Moveto(Pnum n,Pnum n)) Pen Up) (steps(n-1))



--Exercise 2

--(a)

--data Regex = Empty 
--           | String String 
--           | Match Regex

--(b)

--accept :: RegEx -> String -> Bool

--(c)





