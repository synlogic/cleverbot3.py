"""Cleverbot chats with himself."""
import traceback

import cleverbot3


def main():
    # instantiate two Cleverbot objects
    cleverbot_client_one = cleverbot3.Cleverbot()
    cleverbot_client_two = cleverbot3.Cleverbot()

    print('>> Cleverbot #1: Hi.')
    answer = cleverbot_client_two.ask('Hi.')

    while True:
        print('>> Cleverbot #2: {}'.format(answer))
        answer = cleverbot_client_one.ask(answer)
        print('>> Cleverbot #1: {}'.format(answer))
        answer = cleverbot_client_two.ask(answer)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('>> Exiting...')
    except Exception as err:
        print(traceback.format_exc(err))
