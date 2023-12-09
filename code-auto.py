#Guide for product registration auto
  

import pyautogui
import time 


pyautogui.PAUSE = 0.5

# Open browser

pyautogui.press("win")
pyautogui.write("browser name")
pyautogui.press("enter")


# Entrar no link

link = "Paste the link to log in to your company website"
pyautogui.write(link)
pyautogui.press("enter")

# wait 

time.sleep(2)




#  2: Log in to your company's Website  

pyautogui.click(x=648, y=360)
pyautogui.write("e-mail here")
pyautogui.press("tab")
pyautogui.write("password here")
pyautogui.press("enter")
time.sleep(2)

#  3: Import data base
# pip install pandas numpy openpyxl

import pandas 

tabela = pandas.read_csv("produtos.csv")

for linha in tabela.index:

     # 4: register product
     # Change (marca, tipo, categoria, preco_unitario e custo) according to your needs

     codigo = tabela.loc[linha, "codigo"]
     
     pyautogui.click(x=603, y=250)
     pyautogui.write(str(codigo))
     pyautogui.press("tab")
     pyautogui.write(str(tabela.loc[linha, "marca"])) 
     pyautogui.press("tab")
     pyautogui.write(str(tabela.loc[linha, "tipo"]))
     pyautogui.press("tab")
     pyautogui.write(str(tabela.loc[linha, "categoria"]))
     pyautogui.press("tab")
     pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
     pyautogui.press("tab") 
     pyautogui.write(str(tabela.loc[linha, "custo"]))
     pyautogui.press("tab")

     obs = tabela.loc[linha, "obs"]
     if not pandas.isna(obs):
          pyautogui.write(str(obs))

    
    


     pyautogui.press("tab")
     pyautogui.press("enter")
     
     pyautogui.scroll(500)


# 5: register all your products