import pyautogui
import time

def auto_click(duration):
    """Função para clicar repetidamente por uma duração específica"""
    end_time = time.time() + duration
    while time.time() < end_time:
    pyautogui.click()
    time.sleep(0.5) #tempo de espera entre os cliques (ajustavel)

    def main()
        click_duartion = 5 * 60 #5 minutos em segundos
        wait_duration = 3 * 60 * 60 # 3 horas em segundos

        while True:
            print("iniciando o ciclo de cliques por 5 minutos")
            auto_click(click_duartion)
            print("ciclo de cliques concluido. Aguardando 3 horas.")
            time.sleep(wait_duration)

            if __name__ == "__main__":
                main()
