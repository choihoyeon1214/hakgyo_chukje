import tkinter as tk
from tkinter import messagebox

class ScoreboardApp:
    def __init__(self, parent, frame_num):
        self.frame = tk.Frame(parent, borderwidth=2, relief="groove")
        self.frame.grid(row=0, column=frame_num, padx=10, pady=10)

        self.id_label = tk.Label(self.frame, text="학번:")
        self.id_label.grid(row=1, column=0, padx=5, pady=5)
        self.id_entry = tk.Entry(self.frame)
        self.id_entry.grid(row=1, column=1)

        self.name_label = tk.Label(self.frame, text="이름:")
        self.name_label.grid(row=2, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(self.frame)
        self.name_entry.grid(row=2, column=1)

        self.score_label = tk.Label(self.frame, text="점수:")
        self.score_label.grid(row=3, column=0, padx=5, pady=5)
        self.score_entry = tk.Entry(self.frame)
        self.score_entry.grid(row=3, column=1)

        self.add_button = tk.Button(self.frame, text="추가", command=self.add_score)
        self.add_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.output_text = tk.Text(self.frame, height=15, width=40)
        self.output_text.grid(row=5, column=0, columnspan=2)

        self.add_title = tk.Label(self.frame, text="(              ) 순위표")
        self.add_title.grid(row=0, column=0, padx=5, pady=5)

        self.scores = []


    def add_score(self):
        try:
            학번 = self.id_entry.get()
            이름 = self.name_entry.get()
            점수 = int(self.score_entry.get())

            if not 학번 or not 이름:
                raise ValueError("학번과 이름은 필수 입력 값입니다.")

            self.scores.append((학번, 이름, 점수))
            self.scores.sort(key=lambda x: x[2], reverse=True)

            self.display_scores()
            self.clear_entries()
        except ValueError as e:
            messagebox.showerror("입력 오류", str(e))

    def display_scores(self):
        self.output_text.delete(1.0, tk.END)  # 텍스트 박스 초기화
        self.output_text.insert(tk.END, "학번\t이름\t점수\n")
        for score in self.scores:
            self.output_text.insert(tk.END, f"{score[0]}\t{score[1]}\t{score[2]}\n")

    def clear_entries(self):
        self.id_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.score_entry.delete(0, tk.END)

#=================================================================================================교사용 점수판판
class ScoreboardApp_teacher:
    def __init__(self, teacher,frame_num_teacher):
        self.new_method(teacher)
        self.frame_teacher = tk.Frame(teacher, borderwidth=2, relief="groove")
        self.frame_teacher.grid(row=8, column=frame_num_teacher, padx=10, pady=10)

        self.id_label_teacher = tk.Label(self.frame_teacher, text="교무실실:")
        self.id_label_teacher.grid(row=9, column=0, padx=5, pady=5)
        self.id_entry_teacher = tk.Entry(self.frame_teacher)
        self.id_entry_teacher.grid(row=9, column=1)

        self.name_label_teacher = tk.Label(self.frame_teacher, text="이름:")
        self.name_label_teacher.grid(row=10, column=0, padx=5, pady=5)
        self.name_entry_teacher = tk.Entry(self.frame_teacher)
        self.name_entry_teacher.grid(row=10, column=1)

        self.score_label_teacher = tk.Label(self.frame_teacher, text="점수:")
        self.score_label_teacher.grid(row=11, column=0, padx=5, pady=5)
        self.score_entry_teacher = tk.Entry(self.frame_teacher)
        self.score_entry_teacher.grid(row=11, column=1)

        self.add_button_teacher = tk.Button(self.frame_teacher, text="추가", command=self.add_score_teacher)
        self.add_button_teacher.grid(row=12, column=1, columnspan=2, pady=10)

        self.output_text_teacher = tk.Text(self.frame_teacher, height=15, width=40)
        self.output_text_teacher.grid(row=13, column=0, columnspan=2)

        self.add_title_teacher = tk.Label(self.frame_teacher, text="교사용 순위표 (             )")
        self.add_title_teacher.grid(row=7, column=0, padx=5, pady=5)

        self.scores_teacher = []

    def new_method(self, teacher):
        self.teacher=teacher

    def add_score_teacher(self):
        try:
            학번 = self.id_entry_teacher.get()
            이름 = self.name_entry_teacher.get()
            점수 = int(self.score_entry_teacher.get())

            if not 학번 or not 이름:
                raise ValueError("학번과 이름은 필수 입력 값입니다.")

            self.scores_teacher.append((학번, 이름, 점수))
            self.scores_teacher.sort(key=lambda x: x[2], reverse=True)

            self.display_scores_teacher()
            self.clear_entries_teacher()
        except ValueError as e:
            messagebox.showerror("입력 오류", str(e))

    def display_scores_teacher(self):
        self.output_text_teacher.delete(1.0, tk.END)  # 텍스트 박스 초기화
        self.output_text_teacher.insert(tk.END, "학번\t이름\t점수\n")
        for score in self.scores_teacher:
            self.output_text_teacher.insert(tk.END, f"{score[0]}\t{score[1]}\t{score[2]}\n")

    def clear_entries_teacher(self):
        self.id_entry_teacher.delete(0, tk.END)
        self.name_entry_teacher.delete(0, tk.END)
        self.score_entry_teacher.delete(0, tk.END)

class MainApplication:
    def __init__(self, master):
        self.master = master
        self.master.title("점수 순위표")
        
        # 여러 개의 ScoreboardApp을 생성
        for i in range(5):
            ScoreboardApp(master, i)
        for k in range(3):
            ScoreboardApp_teacher(master, k)
        


if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root)
    root.mainloop()