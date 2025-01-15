# https://www.instagram.com/your_activity/interactions/likes
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

# Configurer le driver
driver = webdriver.Chrome()

# Étape 1 : Ouvrir Instagram
driver.get("https://www.instagram.com/")
time.sleep(3)  # Attendez que la page charge

# Étape 2 : Connecte-toi
username_input = driver.find_element(By.NAME, "username")
password_input = driver.find_element(By.NAME, "password")

# Remplacer par les identifiants
username_input.send_keys("METTRESONSEUDO")
password_input.send_keys("METTRESONMDP")
password_input.send_keys(Keys.RETURN)
time.sleep(5)  # Attend que la connexion s'effectue

# Étape 3 : aller sur la page des likes
driver.get("https://www.instagram.com/your_activity/interactions/likes")
time.sleep(5)

#cliquer sur le btn trier
tri_button = driver.find_element(By.XPATH, "//span[@data-bloks-name='bk.components.TextSpan']")
tri_button.click()
time.sleep(3)

#clier sur plus ancien au plus
date_button = driver.find_element(By.CSS_SELECTOR, "span[data-bloks-name='bk.components.TextSpan'][style*='color: rgb(250, 250, 250)'][style*='font-weight: 400'][style*='display: inline'][style*='font-size: 12px'][style*='white-space: pre-wrap'][style*='overflow-wrap: break-word']")
date_button.click()
time.sleep(1)

#appliquer la tri
tri_button = driver.find_element(By.CSS_SELECTOR, "span[data-bloks-name='bk.components.TextSpan'][style*='color: rgb(255, 255, 255)'][style*='font-weight: 700'][style*='display: inline'][style*='font-size: 14px'][style*='white-space: pre-wrap'][style*='overflow-wrap: break-word']")
tri_button.click()
time.sleep(5)

#activer la selection ICI CA MARCHE PAS
slect_button = driver.find_element(By.CSS_SELECTOR, "span[data-bloks-name='bk.components.Text'] [style*='color: rgb(0, 149, 246)'][style*='font-weight: 400'][style*='padding: unset'][style*='line-height: 1.3'][style*='white-space: pre-wrap'][style*='overflow-wrap: break-word']")
slect_button.click()

# Étape 5 : Fermer le navigateur
input("Appuie sur Entrée pour fermer...")
driver.quit()