#STRINGS
def strings():
  print("|| STRINGS ||\n")
  
  name = "Jacob"
  print(f"String name: \n'{name}'")
  
  for i, char in enumerate(name):
    print(f"name[{i}]: {char}")
  print("")

  str1 = "   Hello Everybody"
  print(f"String with whitespace: \n{str1}")
  str1 = str1.strip()
  print(f"Remove white space with .strip(): \n{str1}")
  print("")
  
  str1 = str1.upper()
  print(f"String to uppercase with .upper(): \n{str1}")
  str1 = str1.lower()
  print(f"String to lowercase with .lower(): \n{str1}")
  print("")
  
  print(f"String .startswith('hello'): \n{str1.startswith('hello')}")
  print(f"String .endswith('everybody'): \n{str1.endswith('everybody')}")
  print("")
  
  print(f"String: \n{str1}")
  print(f"Find first index of a char with .find('o'): \n{str1.find('o')}")
  print(f"Count number of char with .count('o'): \n{str1.count('o')}")
  print("")
  
  print(f"String: \n{str1}")
  print(f"Replace o with u in string using .replace('o','u'): \n{str1.replace('o', 'u')}")
  print("")
  
  print(f"Split string into a list of words with a delimeter ' ': \n{str1.split(' ')}")
  print("")
  
  print(f"Split string into a list of characters using list(string): \n{list(str1)}")
  print("")

  def validParenthesisProblem(str):
    
    stack = []

    for i in str:
        if i in '({[':
            stack.append(i)

        else:
            if not stack or \
                (i == ')' and stack[-1] != '(') or \
                (i == '}' and stack[-1] != '{') or \
                (i == ']' and stack[-1] != '['):
                    return False
            stack.pop()

    return not stack
  
  print(f"Valid parenthesis, '({[]})[]()' ?: { validParenthesisProblem('({[]})[]()') }")