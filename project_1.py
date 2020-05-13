from selenium import webdriver
import tkinter as tk

#def openTxt(): Design

def signin (us,pw):

    driver = webdriver.Chrome()
    driver.maximize_window()
    #browsing the page
    driver.get("https://www.vagas.com.br/")
    assert "Vagas de Emprego e Oportunidades de Trabalho - Busca de Emprego | VAGAS.com.br" in driver.title
    #performing clicks and keys input on elements
    python_button = driver.find_element_by_id("loginCandidatoDesktop")
    python_button.click()
    driver.implicitly_wait(5)
    username_input = driver.find_element_by_id("login_candidatos_form_usuario")
    username_input.clear()
    username_input.send_keys(us)
    driver.implicitly_wait(5)
    username_input = driver.find_element_by_id("login_candidatos_form_senha")
    username_input.clear()
    username_input.send_keys(pw)
    signinButton = driver.find_element_by_id("submitLogin")
    signinButton.click()
    driver.implicitly_wait(5)
    #iterating the dictionary that comprises all attributes into the defined class for getting text into the tag,below 
    assert_value = [element.text for element in driver.find_elements_by_class_name("header-bar-profile-name")]
    assert "Gustavo" in str(assert_value[0]), "Failed"
    assert "No results found." not in driver.page_source
    driver.implicitly_wait(10)
    driver.close()
    return "Log in succeeded!!"

def getValues():
    #to be implemented, this will be an UI component for input data
    master = tk.Tk()
    tk.Label(master, text="Type your username: ").grid(row=0)
    tk.Label(master, text="Type your password: ").grid(row=1)

    username = tk.Entry(master, bd=5)
    password = tk.Entry(master, bd=5, show="*")

    username.grid(row=0, column=1)
    password.grid(row=1, column=1)
    alert = ""
    info = tk.Tk()
    tk.Label(info, text=alert).grid(row=0)

    master.mainloop()

def main():
   #userPath = input("Inform the path for file: ")
   #webpage = input("Let us know what webpage you would like to sign in: ")
   username = input("Username: ")
   password = input("Password: ")
   signin(username,password)

if __name__ == "__main__":
    main()
