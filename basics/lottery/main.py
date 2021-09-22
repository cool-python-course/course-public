from src import lottery

if __name__ == '__main__':
    print('Hello World')
    print(f'{lottery.generate_lottery_ticket()}')
    for ticket in lottery.generate_lottery_tickets(10):
        print(f'{ticket}')
