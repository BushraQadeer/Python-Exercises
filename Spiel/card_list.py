__author__ = "8252342, Qadeer"

import random 

#a) Mit dieser Funktion soll ein Kartendeck mit 32 Karten erstellt werden. 
#Die Karten sollen die Werte 1 bis 8 und die 4 Farben "Pik", "Kreuz", "Herz", 
#"Karo" entgegen nehmen. Es soll eine Liste von allen Karten ausgegeben werden.
def create_card_list():
#Es gibt 4 verschiedene Farben    
    color_of_card = ['Pik', 'Kreuz', 'Herz', 'Karo']
#Ich definiere die Werte 1 bis 8 für die Variable "num"    
    num = [1, 2, 3, 4, 5, 6, 7, 8]

#Ich erstelle eine leere Liste   
    card_list = []
#Ich verwende 2 Schleifen, um eine Liste mit allen möglichen Karten zu 
#erstellen.
    for colour in color_of_card:
        for value in num:
            card_list.append((value, colour))  

#Ich beende die Schleife. Die Liste der Karten widr angegeben.      
    return card_list

#b) Mit dieser Funktion soll das Kartendeck zufällig gemischt werden.
def shuffle_card_list(card_list):
#Die Liste der Karten wird zufällig neu sortiert     
    random.shuffle(card_list)

#c) Mit dieser Funktion soll der Wert zweier Karten verglichen werden. Die 
#Funktion nimmt zwei Karten entgegen. Ist der Wert der 1.Karte < 2.Karte, so 
#soll 0 ausgegeben werden. Ist der Wert der beiden Karten gleich, so soll 1 
#ausgegeben werden. Wenn der 1.Karte > 2.Karte gilt, soll 2 ausgegeben werden.     
def compare_two_cards(card_1: (int, str), card_2: (int, str)): 
#Ich verwende eine Schleife, um zu überprüfen ob der Wert der 1.Karte oder 
#der 2.Karte größer ist.    
    if card_1[0]< card_2[0]:
        return 0
    elif card_1[0] == card_2[0]:
            return 1
    else:
        return 2

#d) Diese Funktion soll eine Trumpfkarte erkennen. Eine Trumpfkarte hat einen
#höheren Wert als eine andere Karte. Nun sollen 2 Trumpfkarten verglichen werden.   
def compare_two_cards_trump(card_1: (int, str), card_2: (int, str), trump: str): 

#Ich verwende eine, die zunächst angibt, ob die 1. oder 2.Karte eine 
#Trumpfkarte ist.    
    if card_1[1] == trump :
        return 2
    elif card_2[1] == trump :
        return 0
#Nun wird der Wert der Karten, wie in c) betrachtet. Ist der Wert der 2.Karten
#> 1.Karte,
#so wird o ausgegeben.    
    elif card_1[0]< card_2[0]:
        return 0
#Ist der Wert der beiden Karten gleich, so wird 1 ausgegeben.    
    elif card_1[0] == card_2[0]:
            return 1
#Sonst wird 2 ausgegeben.    
    else:
        return 2

#e) Mit dieser Funktion sollen die Karten unter den Spielern verteilt werden. 
#Die Funktion gibt die Liste der Karten, Anzahl der Spieler und Karten, die 
#die Spieler bekommen sollen aus.   
def hand_out_cards(list_cards: [(int, str)], players: int, number_of_cards: int):  
  
#print(list_cards)
#Ich verwende eine Schleife, um anzugeben, dass nur 32 Karten zur Verfügung 
#stehen. Wenn die Anzahl der Spieler multipliziert mit der Anzahl der Karten,
#die sie bekommen sollen > 32 ist, wird eine Fehlermeldung ausgegeben.    
    if( players * number_of_cards > 32 ):
         print("Fehler!")
         return
    
    for player_number in range(players):
#Ich multipliziere die Anzahl der Spieler mit der Anzahl der Karten, die 
#sie bekommen sollen.         
         start = player_number * number_of_cards
         end = start + number_of_cards
         print(player_number + 1)
#Die Liste der Karten der einzelnen Spieler wird ausgegeben.         
         print(list_cards[start:end])
             
#Ich verwende eine main() -Funktion , um meine Funktionen zu testen
if __name__ == "__main__": 
    
#Ich teste die erste Funktion def create_card_list():.
    card_list = create_card_list()
#Ich teste die zweite Funktion: def shuffle_card_list(card_list):
    shuffle_card_list(card_list)

#Ich teste die dritte Funktion: def compare_two_cards(card_1: (int, str), card_2: (int, str)): 
#Das Progtamm soll zufällig 2 Karten auswählen 
    card_1 = card_list[random.randrange(0, 31)]
    card_2 = card_list [random.randint(0, 31)]
#Die Karten werden ausgegeben    
    print(card_1)
    print(card_2)
#Die Werte der zwei Karten werden verglichen 
    print(compare_two_cards(card_1, card_2))

#Ich teste die Funktion d): def compare_two_cards_trump(card_1: (int, str), card_2: (int, str), trump: str): 
    print(compare_two_cards_trump(card_1, card_2, 'Pik'))

#Ich teste die Funktion e) def hand_out_cards(list_cards: [(int, str)], players: int, number_of_cards: int):  
    print(card_list)
    num_of_players = 4
    num_of_cards = 8
    hand_out_cards(card_list, num_of_players, num_of_cards)
   



