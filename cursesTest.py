import curses 
import curses.wrapper
import time


def main(stdscr):
   curses.curs_set(0)
   for i in range(25):
      #stdscr.clear()
      stdscr.insertln()
      stdscr.insstr(1,1,"Test %d"%(i))
      stdscr.border()
      stdscr.refresh()
      time.sleep(.5)
curses.wrapper(main)