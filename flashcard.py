from tkinter import *
from random import randint
from words import words
score = 0

def get_high_score():
    high_score_file = open("high_score.txt", "r")
    high_score = int(high_score_file.read())
    high_score_file.close()
    return high_score

best = get_high_score()
remaining = 11
root = Tk()
root.title('Groeneveld - APCSP Vocabulary')
root.geometry("650x500")
root['bg']='#666600'
# get a count of our word list
count = len(words)


def next():
    global hinter, hint_count, remaining, score, random_word
    remaining -=1
    remaining_label.config(text = 'Remaining: ' + str(remaining))
    # Clear the screen
    if remaining < 1:
        grade = (score / 50) * 100
        definition.config(text="Game over \nyour grade is " + str(score) + "/50 or " + str(grade) + "%\nClick next to continue.")
        answer_label.config(text="Summary Above")
        remaining = 11
        score = 0
        score_label.config(text = 'Score: ' + str(score))
    else:
        answer_label.config(text="")
        my_entry.delete(0, END)
        hint_label.config(text="")
        random_word = randint(0, count-1)
        # update label with Spanish Word
        definition.config(text=words[random_word][0])
    # Reset Hint stuff
    hinter = ""
    hint_count = 0
    

# Create random selection
    

def answer():
    global score
    global best
    if my_entry.get().lower() == (words[random_word][1]).lower():
        answer_label.config(text="Correct!")
        score = score + 5
        score_label.config(text = 'Score: ' + str(score))
        if score > best:
            best = score
            try:
                # Write the file to disk
                high_score_file = open("high_score.txt", "w")
                high_score_file.write(str(best))
                high_score_file.close()
                best_label.config(text = 'Best: ' + str(best))
            except IOError:
                # Hm, can't write it.
                print("Unable to save the high score.")
        
            
    else:
        answer_label.config(text="Incorrect, change answer,\ntry a hint,\n or go to next.")
        score = score - 1
        score_label.config(text = 'Score: ' + str(score))
        
# Keep Track Of the Hints
hinter = ""
hint_count = 0
def hint():
    global hint_count
    global hinter
    global score

    if hint_count < len(words[random_word][1]):
        hinter = hinter + words[random_word][1][hint_count]
        hint_label.config(text=hinter)
        hint_count +=1
        score = score - 1
        score_label.config(text = 'Score: ' + str(score))


def rules():
    global remaining
    definition.config(text="10 questions!\nCorrect = 5 points, incorrect = -1 point\nHints cost one point\n50 Points is perfect!\nClick next to continue.")
    remaining +=1

def close():
    root.destroy()
    
# Labels
definition = Label(root, text="", font=("Helvetica", 18))
definition.pack(pady=10)
definition['bg']='#F5CBA7'

answer_label = Label(root, fg='#FFF', font=("Helvetica", 20,'bold'), text="")
answer_label.pack(pady=10)
answer_label['bg']='#666600'

my_entry = Entry(root, font=("Helvetica", 18))
my_entry.pack(pady=10)


# Create Buttons
button_frame = Frame(root)
button_frame.pack(pady=15)
button_frame['bg']='#666600'
rules_frame = Frame(root)
rules_frame.pack(pady=1)
rules_frame['bg']='#666600'

answer_button = Button(button_frame, text="Answer", command=answer)
answer_button.grid(row=0, column=0, padx=10)

next_button = Button(button_frame, text="Next", command=next)
next_button.grid(row=0, column=1,padx=10)

hint_button = Button(button_frame, text="Hint", command=hint)
hint_button.grid(row=0, column=2, padx=10)

rules_button = Button(rules_frame, text="Rules",  fg='#801', command=rules)
rules_button.grid(row=0, column=0, padx=10)

# Button for closing
exit_button = Button(rules_frame, text="Exit", fg='#801', command=close)
exit_button.grid(row=0, column=1, padx=10)
   

# Create Hint Label
hint_label = Label(root, fg='#FFF', font=("Helvetica", 17,'bold'), text="")
hint_label.pack(pady=10)
hint_label['bg']='#666600'

# Create a best score label
best_label = Label(root, text = 'Best Score: ' + str(best))
best_label.pack(pady=5)
# Create Score Label
score_label = Label(root, text = 'Score: ' + str(score))
score_label.pack(pady=10)

remaining_label = Label(root, text = 'Remaining: ' + str(remaining))
remaining_label.pack(pady=0)
# Run next function when program starts
next()

root.mainloop()
