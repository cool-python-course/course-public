import controller
import persist
import config
from person import Person

if __name__ == '__main__':
    while True:
        controller.print_options()
        selected_option = controller.read_option()
        if selected_option == 'Q':
            exit(0)
        if selected_option == 'L':
            controller.print_all_people()
        if selected_option == 'R':
            controller.record_person()
