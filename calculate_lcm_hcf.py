def hcf(x,y):
  if x > y:
    x,y = y,x
  if x == y:
    return x
  return hcf(x,y-x)



def lcm(x,y):
    return (x*y)//hcf(x,y)


if __name__ == '__main__':
    with open('data/questions.txt') as f:
        for line in f:
            current_line = line.rstrip('\n')
            quest,x,y = current_line.split(' ')
            x = int(x)
            y = int(y)
            if quest == 'HCF':
                print(f"HCF of {x} and {y}={hcf(x,y)}")
            if quest == 'LCM':
                print(f"LCM of {x} and {y}={lcm(x,y)}")
            if quest not in ['HCF','LCM']:
                raise ValueError(f"Invalid question {quest}")

        

            

