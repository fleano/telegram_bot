from random import randint
import Constants as keys
from telegram.ext import *
import Responses as R

# import necessary functions

print('Bot started...')


# create the blackjack class, which will hold all game methods and attributes


class Blackjack():
    def __init__(self):
        self.deck = []    # set to an empty list
        self.suits = ("♠️", "❤️", "♦️", "♣️")
        self.values = (2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A')

    # create a method that creates a deck of 52 cards, each card should be a tuple with a value and suit
    def makeDeck(self):
        for suit in self.suits:
            for value in self.values:
                self.deck.append((value, suit))   # ex: (7, "Hearts")

    # method to pop a card from deck using a random index value
    def pullCard(self):
        return self.deck.pop(randint(0, len(self.deck) - 1))

# create a class for the dealer and player objects


class Player():
    def __init__(self, name):
        self.name = name
        self.hand = []

    # take in a tuple and append it to the hand
    def addCard(self, card):
        self.hand.append(card)

    # if not dealer's turn, then only show one of his cards, otherwise show all cards
    def showHand(self):

        intro = "\n{}\n===========".format(self.name)
        cards = []
        for i in range(len(self.hand)):

            card = self.hand[i]
            card_list_item = "{} of {}".format(card[0], card[1])
            cards.append(card_list_item)

        return intro, cards


def play_game(name):
    game = Blackjack()

    game.makeDeck()

    player = Player(name)

    # add two cards to the dealer and player hand
    for i in range(5):
        player.addCard(game.pullCard())

    # show both hands using method
    return player.showHand()


def start_command(update, context):
    update.message.reply_text(
        "Hello! I am Justin's first bot. I was created to play poker with you!")


def help_command(update, context):
    update.message.reply_text(
        'If you need help, just play poker!\nCheat sheet url: https://texasholdemquestions.com/poker-cheat-sheet-for-2020/')
    update.message.reply_photo('')


def say_command(update, context):
    text = str(update.message.text)
    text = text.replace('/say', '')
    update.message.reply_text(text)


def play_command(update, context):
    name = str(update.message.text)
    name = name.replace('/play', '')
    intro, cards = play_game(name)
    text = intro

    for i in cards:
        text += '\n' + i
    update.message.reply_text(text)


def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)

    update.message.reply_text(response)


def error(update, context):
    print(f"Update {update} caused error {context.error}")


def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler('say', say_command))
    dp.add_handler(CommandHandler('play', play_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


main()
