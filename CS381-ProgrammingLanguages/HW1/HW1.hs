import HW1types

--Main Program:

--Excersize 1:Programming with Lists
--a) Ins function inserts the element x one time to the begining of the multiset >>>>> exmaple: ins 3 [(2,1),(3,1),(8,6)]
ins :: Eq a => a -> Bag a -> Bag a
ins x []=[(x,1)]
ins x ((a,n):xs)
  |x==a =((a,n+1):xs)
  |otherwise =((a,n):ins x xs)

--b) Del function removes the element x from the multiset >>>>>> Example : del 3 [(2,1),(3,1),(8,6)]
del :: Eq a => a -> Bag a -> Bag a 
del x []=[]
del x ((a,n):xs)
  |x==a && n>1 =((a,n-1):xs)
  |x==a && n==1 =xs
  |otherwise =((a,n):del x xs) 

--c)bag produces a multiset representation
bag :: Eq a => [a] -> Bag a
bag[]=[]
bag (a:xs)=ins a (bag(xs)) 

--d)Subbag determines whether or not its first argument bag is contained in the second
subbag :: Eq a => Bag a -> Bag a -> Bool
subbag [] a =True
subbag a [] =False
subbag [(a,n)] ((b,m):xs)
     |a==b &&m>=n = True
     |otherwise =False
--e)  isSet tests whether a bag is actually a set
isSet :: Eq a => Bag a -> Bool
isSet[]=True
isSet ((a,n):xs)
     |n>1 =False
     |otherwise =True
--f)  function size computes the number of elements contained in a bag
size :: Bag a -> Int
size []=0
size ((a,n):xs)= n+size(xs)

---------------Excersise 2:
--a) compute the list of nodes contained in a given graph
nodes :: Graph -> [Node] 
nodes []=[]
nodes ((a,b):c) = norm(a:b:nodes(c))

--b)computes the list of successors for a node in a given graph
suc :: Node -> Graph -> [Node]
suc x []=[]
suc x ((a,b):c) 
   |x==a = (b:suc x c)
   |otherwise=suc x c
   
--c) removes a node together with all of its incident edges from a graph
detach :: Node -> Graph -> Graph
detach x []=[]
detach x ((a,b):xs)
      |x==a || x==b = detach x xs
      |otherwise =((a,b):detach x xs)
--d) creates a cycle of any given number
aya ::Int-> Int -> Graph
aya a b = [(a,b)]

byb :: Int -> Int -> Graph
byb a b   
    |a >1        = (aya b (b+1)) ++ (byb (a-1) (b+1)) 
    |otherwise   = aya b a    

cyc :: Int -> Graph
cyc n =  byb n 1

   
--Exercise 3. Programming with Data Types
--a) 
width :: Shape -> Length
width (Pt (x,y)) =0
width (Circle(x,y) r) =2*r
width (Rect (x,y) a b) 
     | a>b=a
     |otherwise=b

--b) bbox computes the bounding box of a shape.
bbox :: Shape -> BBox
bbox (Pt (x,y))= ((x,y),(x,y))
bbox (Circle(x,y) r)=((x-r,y-r),(x+r,y+r))
bbox (Rect (x,y) a b)=((x,y),(x+a,y+b))

--c) minX  computes the minimum x coordinate of a shape.

minX :: Shape -> Number
minX (Pt (x,y)) =x
minX (Circle (x,y) r)=x-r
minX (Rect (x,y) a b)=x

--d) moves the position of a shape by a vector given by a point as its second argument
addPt :: Point -> Point -> Point
addPt (x,y) (a,b) =(x+a,y+b)

move :: Shape -> Point -> Shape
move (Pt(x,y)) (a,b)= Pt(addPt (x,y) (a,b))
move (Circle (x,y) r) (a,b)= Circle (addPt (x,y) (a,b)) r
move (Rect(x,y) l1 l2) (a,b)= Rect(addPt(x,y) (a,b)) l1 l2




