from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NovoVisitanteTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()
    
    def test_iniciar_uma_lista_e_acessar_depois(self):
        # Acessar a homepage
        self.browser.get('http:localhost:8000')

        # Percebe que o título da página e o cabeçalho mencionam lista de tarefas

        self.assertIn('To-Do lists', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # Insere um item de tarefa
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # Ela digita 'Comprar penas de pavão' em uma caixa de texto
        inputbox.send_keys('Comprar penas de pavão')

        # Quando digita enter, a página é atualizada, e agora a pagina lista
        # '1: Comprar penas de pavão' como um interm da lista de tarefas
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_id('tr')
        self.assertTrue(
            any(row.text == '1: Comprar penas de pavão' for row in rows)
        )

        # Ela digita 'Usar a penas de pavão para pescar

        self.fail('Finalizar o testes')

        # Aperta enter, e a página é atualizada novamente, agora exibindo os 2 itens

        # Ela anota uma URL único com a lista de tarefa

        # Ela testa a URL única

        # Ela anota e saí da aplicação

if __name__ == '__main__':
    unittest.main(warnings='ignore')