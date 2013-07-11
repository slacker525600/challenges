#10! permutations
#3628800
#each starting digit is 1/10 so, 
#362880 0s 1s 2s
#1000000 - 362880*2 = 274240
#362880/9 for next dig = 40320
def find_mil():
  nAtLevel = 3628800 #10!
  nTheNumber = 0
  nDigOn = 10 # ten choices
  nElim = 0
  anDigLeft = [0,1,2,3,4,5,6,7,8,9]
  anSet = []
  nDigRank = 0
  while nDigOn != 1:
    if nElim + nAtLevel/nDigOn > 999999:
      #do not go higher at this level.
      nAtLevel/=nDigOn
      nDigOn -= 1
      anSet.append(nDigRank)
      nTheNumber = nTheNumber*10 + anDigLeft[nDigRank]
      print(nTheNumber, nElim)
      anDigLeft.remove(anDigLeft[nDigRank])
      nDigRank =0
    else:
      nElim += nAtLevel/nDigOn # eliminating
      nDigRank += 1
  return anSet
print(find_mil())
#[2, 6, 6, 2, 5, 1, 2, 2, 0]
#0123456789
#2783915604
#exclusion counting up from start... ... wrong, 
#trying one larger and one smaller ... >1000000 vs ==?
