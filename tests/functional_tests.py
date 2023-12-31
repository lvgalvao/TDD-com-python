from selenium import webdriver
import unittest

class NovoVisitanteTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()
    
    def test_iniciar_uma_lista_e_acessar_depois(self):
        # Acessar a homepage
        self.browser.get('http:localhost:8000')

        # Percebe que o título da página e o cabeçalho mrnciam lista de tarefas

        self.assertIn('To-Do', self.browser.title)
        self.fail('O título do browser foi: ' + self.browser.title)

        # Insere um liitem de tarefa

        # Ela digita 'Comprar penas de pavão' em uma caixa de texto

        # Quando digita enter, a página é atualizada, e agora a pagina lista
        # '1: Comprar penas de pavão' como um interm da lista de tarefas

        # Ela digita 'Usar a penas de pavão para pescar

        # Aperta enter, e a página é atualizada novamente, agora exibindo os 2 itens

        # Ela anota uma URL único com a lista de tarefa

        # Ela testa a URL única

        # Ela anota e saí da aplicação

if __name__ == '__main__':
    unittest.main(warnings='ignore')