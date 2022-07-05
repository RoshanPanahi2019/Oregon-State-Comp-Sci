module HW2types where

--import Data.List (nub,sort)

--Exercise 1

--(a)



data Cmd = Pen Mode
     | Moveto Pos Pos
     | Def String Pars Cmd
     | Call String Vals
     | CmdC Cmd Cmd
--deriving Show



data Mode = Up | Down
data Pos = Pnum Int | Pname String
type Pars = [String]
type Vals = [Int]


--(b)

vector = Def "vector"  ["x1","y1","x2","y2"] (CmdC(CmdC(CmdC(CmdC (Pen Up) (Moveto (Pname ("x1")) (Pname ("y1")))) (Pen Down)) (Moveto (Pname "x2") (Pname "y2"))) (Pen Up))
                          

--(c)

steps :: Int -> Cmd
steps 0 = Pen Up
steps n = CmdC
            (CmdC
                (CmdC
                    (CmdC
                        (CmdC
                            (CmdC (Pen Up)(Moveto (Pnum (n)) (Pnum (n)))) (Pen Down))
                            (Moveto (Pnum (n-1)) (Pnum (n))))
                            (Moveto (Pnum (n-1)) (Pnum (n-1))))
                            (Pen Up))
                            (steps (n-1))



--Exercise 2


--(a)
data Regex= Epsilon
           |Dot[Char]
           |Ch [Char] 
           |Ques [Char]
           |Star Regex
           |Plus Regex
           |Seq Regex Regex
           |Or Regex Regex


--(b)
accept ::Regex -> String ->Bool
accept Epsilon s = (s == [])
accept (Dot c) s = True
accept (Ch c) s = (c == s)
accept (Ques c) s = ((s == []) || (c == s))
accept (Star c) s | s == [] = True
                  | otherwise = or [accept c v && accept (Star c) w | (v,w) <- splits s]
accept (Plus c) s | s == [] = False
                  | otherwise = or [accept c v && accept (Star c) w | (v,w) <- splits s]
accept (Seq e1 e2) s = or [accept e1 v && accept e2 w | (v,w) <- splits s]
accept (Or e1 e2) s = accept e1 s || accept e2 s 




--test function
--accept (Epsilon) ""
--accept (Ch "ab") "ab"
--accept (Dot "ab") "sudvfs"
--accept (Ques "ab") ""
--accept(Star (Ch "def")) "defdefdefdef" Or  accept(Star (Ch "def")) ""
--accept(Plus (Ch "def")) "def"    Or  accept(Plus (Ch "def")) ""
--accept(Seq (Ch "ab") (Ch "cd")) "abcd"
--accept(Or (Ch "abc") (Ch "def")) "def"


splits::[a]->[([a],[a])]
splits []=[]
splits [x]=[([],[x]),([x],[])]
splits(x:xs)=([],x:xs):[(x:s,t)|(s,t)<-splits xs]



--(c)

classify :: Regex -> [String] -> Bool
classify e ws = putStrLn ("ACCEPT:\n"++show acc++"\nREJECT:\n"++show rej)
                where acc = filter (accept e) ws
                      rej = filter (not.(accept e)) ws

--commaSepTest = ["cat","cat,bat","cat,cat","bat","",",","dog",
--                 ",cat","cat,","catcat","cat,,bat","cat,bat,"]

commaSep :: Regex
commaSep=accept(Or (Ch "c") (Ch "c"))  




















