#https://programmers.co.kr/learn/courses/30/lessons/60061

class Building ():
    def __init__(self, n, build_frame):
        self.n = n
        self.frames = build_frame.copy()
        self.columns = set()
        self.bars = set()
        while len(self.frames):
            self.try_next_frame()
    
    def try_next_frame(self):
        if not self.frames: return False
        frame, self.frames = self.frames[0], self.frames[1:]
        x, y, a, b = frame
        
        if b: # add frame
            if a: # add bar
                if (x,y) in self.bars:
                    return False
                if ((x, y-1) in self.columns or (x+1, y-1) in self.columns or ((x-1, y) in self.bars and (x+1, y) in self.bars)):
                    self.bars.add((x,y))
                    return True
                else: return False
            else: # add column
                if (x,y) in self.columns:
                    return False
                if (y==0 or (x,y) in self.bars or (x-1,y) in self.bars or (x,y-1) in self.columns):
                    self.columns.add((x,y))
                    return True
                else: return False
        else: # rm frame
            if a: # rm bar
                if (x,y) not in self.bars:
                    return False
                # bars left and right
                if (x-1,y) in self.bars and (x-1,y-1) not in self.columns and (x,y-1) not in self.columns:
                    return False
                if (x+1,y) in self.bars and (x+1,y-1) not in self.columns and (x+2,y-1) not in self.columns:
                    return False
                # columns above
                if (x,y) in self.columns and (x,y-1) not in self.columns and (x-1,y) not in self.bars:
                    return False
                if (x+1, y) in self.columns and (x+1,y-1) not in self.columns and (x+1,y) not in self.bars:
                    return False
                
                self.bars.remove((x,y))
                return True
            else: # rm column
                if (x,y) not in self.columns:
                    return False
                # bars above
                if (x-1,y+1) in self.bars and (x-1,y) not in self.columns and ((x-2,y+1) not in self.bars or (x,y+1) not in self.bars):
                    return False
                if (x,y+1) in self.bars and (x+1,y) not in self.columns and ((x-1,y+1) not in self.bars or (x+1,y+1) not in self.bars):
                    return False
                # column above
                if (x,y+1) in self.columns and (x-1,y+1) not in self.bars and (x,y+1) not in self.bars:
                    return False
                
                self.columns.remove((x,y))
                return True
        
def solution(n, build_frame):
    building = Building(n, build_frame)
    ans = [(x,y,1) for x,y in building.bars] + [(x,y,0) for x,y in building.columns]
    return sorted(ans)
