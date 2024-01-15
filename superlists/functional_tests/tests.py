from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from django.test import LiveServerTestCase
from selenium.common.exceptions import WebDriverException

MAX_WAIT = 10
class NovoVisitanteTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def wait_for_row_in_list_table(self, row_text):
        """ 
        Objetivo desse teste é trabalhar com o princípio de DRY (Don't Repeat Yourself)
        Háviamos 2 testes semelhantes para testar itens em uma lista
        Com esse teste removemos essa lógica duplicada e simpliciamos nossa lógica
        """
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep


    
    def test_iniciar_uma_lista_e_acessar_depois(self):
        # Acessar a homepage
        self.browser.get(self.live_server_url)

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
        self.wait_for_row_in_list_table('1: Comprar penas de pavão')

        # Ela digita 'Usar a penas de pavão para pescar

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Usar penas de pavão para fazer uma isca')
        inputbox.send_keys(Keys.ENTER)

        self.wait_for_row_in_list_table('1: Comprar penas de pavão')
        self.wait_for_row_in_list_table('2: Usar penas de pavão para fazer uma isca')
        
    def test_multiplos_usuarios_podem_iniciar_novas_listas_em_diferentes_urls(self):
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Comprar penas de pavão')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Comprar penas de pavão')

        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')

        self.browser.quit()
        self.browser = webdriver.Firefox()
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Comprar penas de pavão', page_text)
        self.assertNotIn('Usar penas de pavão para fazer uma isca', page_text)

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Comprar leite')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Comprar leite')

        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Comprar penas de pavão', page_text)
        self.assertIn("Comprar leite", page_text)
