-- To test this program:
--    semCmd (LD 2) (Just [])
--    semCmd ADD (Just[2,4,5])
--    semCmd MULT (Just[2,4,5])
--    sem [LD 3,ADD] (Just [])
--    sem' (Seq (Pen Up) (Seq (Moveto 1 2) (Seq (Pen Down) (Seq (Moveto 4 5) (Moveto 6 7)))))




type Account = Int

data Activity = Deposit Int
              | Withdraw Int
              | Close
              | After Activity Activity


sem :: Activity -> Maybe Account -> Maybe Account
sem (Deposit x) (Just b) =  Just (x+b) 
sem (Withdraw x) (Just b) = if (b-x>0) then Just(b-x) else Nothing
sem (Close x) (Just b) = Just(0)
sem (After a1 a2) (Just b) = Just( sem (a2 (Just (sem a1 x ))))





 sem (a2 (Just (sem a1 x) )                 




data Cmd = LD Int
        | ADD
        | MULT
        | DUP
        deriving Show
type Stack = [Int]

count:: Stack->Int
count []=0
count(x:xs)= count(xs)+1

type D = Maybe Stack-> Maybe Stack
semCmd :: Cmd -> D
semCmd (LD a) (Just[])=Just [a]
semCmd (LD a) (Just(x:xs))=Just (a:x:xs)
semCmd (LD a) Nothing= Nothing

semCmd ADD (Just []) =Nothing
semCmd ADD (Just[a])= Nothing
semCmd ADD Nothing= Nothing
semCmd ADD (Just(x:y:xs))= Just ((x+y):xs)
                
semCmd MULT (Just []) =Just []
semCmd MULT (Just[a])= Nothing
semCmd MULT Nothing= Nothing
semCmd MULT (Just(x:y:xs))=Just ((x*y):xs)

semCmd DUP  (Just[]) =Just []
semCmd DUP Nothing= Nothing
semCmd DUP (Just(x:xs))=Just (x:x:xs)


type Prog = [Cmd]
sem :: Prog -> D
sem [] a=a 
sem (c:cs) Nothing=Nothing
sem (c:cs) (Just a) =  sem cs (semCmd c (Just a))
