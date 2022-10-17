import time
import cv2
import random
from keras.models import load_model
import numpy as np
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

class Rps:
    ''' A rock, paper, scisors game that asks the user for 
        input via video capturing, then predicts the gestures
        using a model created in teachable machine and compares 
        the results of the model to the random choice made by the computer'''

    def __init__(self):
        self.options = ["rock", "paper", "scissors", "Nothing"]
        self.choice = self.options[:3]
        self.user_wins = 0
        self.computer_wins = 0
        self.winning_score = 3
        
    def get_computer_choice(self):
        pick_one = random.choice(self.choice)
        return pick_one

    def get_prediction(self):
        ''' A function that captures the images and predicts the gestures
            then prints the predicted gesture name in the frame
            '''
        end_time = time.time()+5
        while time.time() < end_time:
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            prediction = model.predict(data)
            max_prediction_index = np.argmax(prediction) 
            user_pick = self.choice[max_prediction_index]
            if user_pick == "rock":
                cv2.putText(frame, user_pick, (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
            elif user_pick == "paper":
                cv2.putText(frame, user_pick, (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
            elif user_pick == "scissors":
                cv2.putText(frame, user_pick, (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
            else:
                cv2.putText(frame, user_pick, (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
            cv2.imshow('frame', frame) 
            # Press q to close the window
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        return user_pick


    def get_winner(self, computer_choice, user_choice):

        if user_choice == computer_choice:
            print(f"Both players selected {user_choice}. It's a tie!")
        elif user_choice == "rock":
            if computer_choice == "scissors":
                print("Rock smashes scissors! You win!")
                self.user_wins += 1
            else:
                print("Paper covers rock! You lose.")
                self.computer_wins += 1
        elif user_choice == "paper":
            if computer_choice == "rock":
                print("Paper covers rock! You win!")
                self.user_wins += 1
            else:
                print("Scissors cuts paper! You lose.")
                self.computer_wins += 1
        elif user_choice == "scissors":
            if computer_choice == "paper":
                print("Scissors cuts paper! You win!")
                self.user_wins += 1
            else:
                print("Rock smashes scissors! You lose.")
                self.computer_wins += 1


def play():
    game = Rps()
    while True:
        user = game.get_prediction()
        computer = game.get_computer_choice()
        game.get_winner(computer, user)
        if game.user_wins == game.winning_score:
            print(f"Great Job!!!, you won by {game.user_wins} points")
            break
        elif game.computer_wins == game.winning_score:
             print(f"Sorry!!!, computer won by {game.computer_wins} points")
             break
    # After the loop release the cap object         
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()        

if __name__ == '__main__':
    play()