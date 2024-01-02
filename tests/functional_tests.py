from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NovoVisitanteTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        """ 
        Objetivo desse teste é trabalhar com o princípio de DRY (Don't Repeat Yourself)
        Háviamos 2 testes semelhantes para testar itens em uma lista
        Com esse teste removemos essa lógica duplicada e simpliciamos nossa lógica
        """
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])
    
    def test_iniciar_uma_lista_e_acessar_depois(self):
        # Acessar a homepage
        self.browser.get('http:localhost:8000')

        # Percebe que o título da página e o cabeçalho mencionam lista de tarefas

        self.assertIn('To-do lists', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-do', header_text)

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

        self.check_for_row_in_list_table('1: Comprar penas de pavão')

        # Ela digita 'Usar a penas de pavão para pescar

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Usar penas de pavão para fazer uma isca')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        self.check_for_row_in_list_table('1: Comprar penas de pavão')
        self.check_for_row_in_list_table('2: Usar penas de pavão para fazer uma isca')
        
        self.fail('Finalizar o testes')

        # Aperta enter, e a página é atualizada novamente, agora exibindo os 2 itens

        # Ela anota uma URL único com a lista de tarefa

        # Ela testa a URL única

        # Ela anota e saí da aplicação

if __name__ == '__main__':
    unittest.main(warnings='ignore')