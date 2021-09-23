from src import lottery

if __name__ == '__main__':
    print('Hello World')
    tickets = lottery.generate_lottery_tickets(10)
    pulled_number = lottery.generate_lottery_ticket()
    print(f'{pulled_number}')
    for ticket in tickets:
        print(f'{ticket}')

    print(f'{lottery.check_winner_tickets(tickets,pulled_number)}')
