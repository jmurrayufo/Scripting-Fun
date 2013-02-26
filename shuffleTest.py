import random
import time

def SimpleShuffle(deck, runs):
   # Init
   newDeck=list(deck)
   # Loops
   for x in range(runs):
      tmpDeck = list(newDeck)
      newDeck = list()
      topDeck=tmpDeck[:len(tmpDeck)/2]
      botDeck=tmpDeck[len(tmpDeck)/2:]

      while(len(topDeck) and len(botDeck)):
         # Select units from top deck
         numTop = random.randint(1,min(len(topDeck),5))

         # Select units from bot deck
         numBot = random.randint(1,min(len(botDeck),5))

         if random.random() < 0.5:
            for i in range(numTop):
               newDeck.append(topDeck.pop(0))
            for i in range(numBot):
               newDeck.append(botDeck.pop(0))
         else:
            for i in range(numBot):
               newDeck.append(botDeck.pop(0))
            for i in range(numTop):
               newDeck.append(topDeck.pop(0))
      # Append the remaining elements
      if random.random() < 0.5:
         newDeck+=topDeck
         newDeck+=botDeck
      else:
         newDeck+=topDeck
         newDeck+=botDeck

   return newDeck

def StacksShuffle(deck,stacks,runs):
   newDeck=list(deck)
   for null in range(runs):
      tmpDeck = list(newDeck)

      # Split deck into piles
      piles = list()
      for i in range(stacks):
         piles.append(list())
      for idx,val in enumerate(tmpDeck):
         piles[idx%len(piles)].append(val)

      # Grab piles randomly and restack the deck
      random.shuffle(piles)
      newDeck = list()
      for i in piles:
         newDeck+=i
   return newDeck

def TestForGoodHand(deck,minMana,maxMana):
   mCount = 0
   for i in range(8):
      if deck[i]=='m':
         mCount+=1
   if minMana > mCount or mCount > maxMana:
      return False
   else:
      return True

def NewDeck(cards,pMana=33,pCards=66):
   pTotal = float(pMana+pCards)
   pMana = pMana/pTotal
   pCards = pCards/pTotal
   tmp = list()
   for i in range(int(cards*pMana)):
      tmp.append("m")
   for i in range(int(cards*pCards)):
      tmp.append("c")
   if len(tmp) < cards:
      tmp.append("c")
   return tmp



results = list()
for i in range(500):
   deck = NewDeck(40,2,3)
   deck = StacksShuffle(deck,5,3)
   results.append( TestForGoodHand(deck,3,5) )
print results.count(True)/float(len(results))*100
print results.count(False)/float(len(results))*100
