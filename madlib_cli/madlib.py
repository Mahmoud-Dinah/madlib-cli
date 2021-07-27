import re 
def Hello():
  print("*********************  Welcome ****************** ")

Hello()

def read_template(path: str) -> str:
  try:
    with open(path, 'r') as file:
        output = file.read()
        return output.strip()
  except FileNotFoundError:
       print(" Pleaes make ure that you are entr the correct path")
       raise

def parse_template(output):
    regex = r'\{(.*?)\}'
    new = re.findall(regex, output)
    for i in new:
       output = output.replace(i,'')
      
    return output,tuple(new)

def user_input(q):
    inputs=[]
    for i in q:
      ask = input(f"please insert a word:  {i} ")
      inputs.append(ask)
    return inputs 


def merge(file,inputs):
    print (inputs)
    merged = file.format("dark", "stormy", "night")
    print(merged)
    return merged

