"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
  #if part of SPARC
    if x <= 1:
      return x
  #else part of SPARC
    else:
      ra,rb = (foo(x-1)),(foo(x-2))
    #the "in ra+rb"
      return ra + rb
    pass





def longest_run(mylist, key):
  length = 0
  my_set = set()
  for i, key1 in enumerate(mylist):
    if key1 == key: 
        length += 1
    else:
        print('else',i,length)
        my_set.update([length])
        length=0   
  my_set.update([length])
  return max(my_set)
  pass


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    
def  combine (r1:Result,r2:Result):
  r=Result(0,0,0,'F')
  
  if r1.is_entire_range == 'T' and r2.is_entire_range == 'T':
    r.is_entire_range ='T'
    r.longest_size=r1.longest_size+r2.longest_size
    r.left_size=r1.left_size+r2.left_size
    r.right_size= r1.right_size+r2.right_size

  if (r1.is_entire_range == 'T' and r2.is_entire_range == 'F') :
    r.is_entire_range ='F'
    r.longest_size=r1.longest_size+r2.left_size
    r.left_size=r1.left_size+r2.left_size
    r.right_size= r1.right_size+r2.right_size

      
  if (r1.is_entire_range == 'F' and r2.is_entire_range == 'T') :
    r.is_entire_range ='F'
    r.longest_size=max(r2.longest_size,r1.longest_size)
    r.left_size=r1.left_size+r2.left_size
    r.right_size= r1.right_size+r2.right_size


  if (r1.is_entire_range == 'F' and r2.is_entire_range == 'F'):  
    r.is_entire_range ='F'
    r.longest_size=max(r1.longest_size,r2.longest_size)
    r.left_size=r1.left_size+r2.left_size
    r.right_size=max(r1.right_size,r2.right_size)
      
  return(r)
  pass
def longest_run_recursive(mylist, key):
    ### TODO.
  mid = 0
  
  if len(mylist) ==1:
    if mylist[0] == key:
      r=Result(1,1,1,'T')
      return r
    else:
      r=Result(0,0,0,'F')
      return r
  else:
    #l=len(mylist)
    mid = len(mylist)//2
    left = mylist[:mid]
    right = mylist[mid:]
    r1=longest_run_recursive(left, key)
    r2=longest_run_recursive(right, key)
    return (combine( r1,r2 ))
  pass


## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3

