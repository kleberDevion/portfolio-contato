import requests
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def config():
    # Define o alvo da URL
    target_url = "https://megalink.net.br"
    
    # Configuração do Selenium Chrome Driver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    return target_url, driver

def extract_data(url, driver):
    print("Extraindo infos.......")
    try:
        driver.get(url)
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')

        # Busca pelas tags especificadas
        data = {
            "title": soup.title.string if soup.title else "",
            "footer": soup.footer.get_text() if soup.footer else "",
            "header": soup.header.get_text() if soup.header else "",
            "paragraphs": [p.get_text() for p in soup.find_all('p')]
        }

        if any(data.values()):
            print("Dados conseguidos!!")
            return data
        else:
            print("Erro ao extrair as informacoes..!!!")
            return None
    except Exception as e:
        print(f"Erro ao extrair as informacoes..!!! {e}")
        return None

def main():
    url, driver = config()
    
    try:
        result = extract_data(url, driver)
        
        if result:
            filename = "resultScraping.json"
            with open(filename, "w", encoding='utf-8') as file:
                json.dump(result, file, indent=4, ensure_ascii=False)
            print(f"Dados salvos em {filename}")
        else:
            print("Erro ao salvar as informacoes..")
            
    except Exception as e:
        print(f"Erro ao salvar as informacoes.. {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()