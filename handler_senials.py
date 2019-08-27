from senial import Senial

class HandlerSenials():

    def __init__(self):
        self.list_senials = list()

    def load_senials(self):

        with open("senials_running.txt", "r") as file_read:
            rows = file_read.readlines()
            for row in rows:
                new_senial = Senial()
                new_senial.set_from_file(row)

                self.list_senials.append(new_senial)

        file_read.close()
        
        file_delete = open("senials_running.txt", "w")
        file_delete.close()


    def save_senials(self):
        list_senial_running = list()

        for senial in self.list_senials:
            if senial.running is True:
                list_senial_running.append(senial)

        file = open("senials_running.txt", "w")
        file.writelines(list_senial_running)

        list_senial_running.clear()