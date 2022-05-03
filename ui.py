from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(150, 125, text="Question goes here", fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"), width=280)

        self.score = 0
        self.score_label = Label(text=f"Score: {self.score}", font=("Arial", 12), bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, command=self.check_if_true, highlightthickness=0)
        self.true_button.grid(row=2, column=0)
        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, command=self.check_if_false, highlightthickness=0)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.score_label.config(text=f"Score: {self.score}")
        else:
            self.canvas.itemconfig(self.question_text, text="This is the end of the quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def check_if_true(self):
        correct = self.quiz.check_answer(user_answer="True")
        self.give_feedback(correct)

    def check_if_false(self):
        correct = self.quiz.check_answer(user_answer="False")
        self.give_feedback(correct)

    def give_feedback(self, correct):
        if correct:
            self.canvas.config(bg="green")
            self.score +=1
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
