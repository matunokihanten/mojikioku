import random
import tkinter as tk
from tkinter import messagebox

# Kanji characters used in the game
kanji_characters = [
    '一', '二', '三', '四', '五', '六', '七', '八', '九', '十', '百', '千', '万',
    '上', '下', '左', '右', '中', '大', '小', '日', '月', '火', '水', '木', '金', '土',
    '山', '川', '空', '田', '虫', '犬', '猫', '鳥', '魚', '馬', '牛', '花', '草', '木', '林', '森',
    '人', '父', '母', '兄', '姉', '弟', '妹', '子', '友', '学', '校', '本', '文', '字', '生', '先', '名',
    '年', '時', '分', '秒', '早', '立', '出', '入', '前', '後', '外', '内', '男', '女', '円', '音',
    '車', '電', '駅', '白', '黒', '赤', '青', '黄', '緑', '大', '中', '小', '明', '暗', '新', '古'
]

class KanjiMemoryGame:
    def __init__(self, root):
        self.root = root
        self.root.title("漢字記憶ゲーム")

        self.current_level = 1
        self.current_kanji_sequence = ''
        self.previous_kanji_sequence = ''

        self.level_label = tk.Label(root, text="問題番号: 1", font=("Arial", 20))
        self.level_label.pack()

        self.kanji_label = tk.Label(root, font=("Arial", 40))
        self.kanji_label.pack()

        self.input_field = tk.Entry(root, font=("Arial", 20))
        self.input_field.pack()
        self.input_field.bind('<Return>', self.check_answer)

        self.result_label = tk.Label(root, font=("Arial", 20), fg="red")
        self.result_label.pack()

        self.start_button = tk.Button(root, text="開始", font=("Arial", 20), command=self.start_game)
        self.start_button.pack()

        self.delete_button = tk.Button(root, text="1文字消す", font=("Arial", 20), command=self.delete_last_character)
        self.delete_button.pack()

        self.submit_button = tk.Button(root, text="完了", font=("Arial", 20), command=self.check_answer)
        self.submit_button.pack()

        self.kanji_container = tk.Frame(root)
        self.kanji_container.pack()

        self.display_kanji_buttons()

    def start_game(self):
        self.current_level = 1
        self.current_kanji_sequence = ''
        self.previous_kanji_sequence = ''
        self.next_level()

    def next_level(self):
        random_kanji = self.generate_random_kanji(1)
        self.current_kanji_sequence += random_kanji
        self.display_kanji_sequence()

    def display_kanji_sequence(self):
        self.level_label.config(text=f"問題番号: {self.current_level}")
        self.kanji_label.config(text=self.current_kanji_sequence)
        self.input_field.delete(0, tk.END)
        self.result_label.config(text='')

        self.root.after(3000, self.hide_kanji_sequence)

    def hide_kanji_sequence(self):
        self.kanji_label.config(text='')
        self.input_field.focus()

    def check_answer(self, event=None):
        user_input = self.input_field.get()
        if user_input == self.current_kanji_sequence:
            self.result_label.config(text='正解です！次のレベルへ進みます。')
            self.previous_kanji_sequence = self.current_kanji_sequence
            self.current_level += 1
            self.root.after(2000, self.next_level)
        else:
            self.result_label.config(text=f'不正解です。正解は「{self.current_kanji_sequence}」でした。')
            self.input_field.delete(0, tk.END)

    def delete_last_character(self):
        self.input_field.delete(len(self.input_field.get())-1, tk.END)

    def generate_random_kanji(self, level):
        return ''.join(random.choice(kanji_characters) for _ in range(level))

    def display_kanji_buttons(self):
        for index, kanji in enumerate(kanji_characters):
            button = tk.Button(self.kanji_container, text=kanji, font=("Arial", 15),
                               command=lambda k=kanji: self.input_field.insert(tk.END, k))
            button.grid(row=index // 10, column=index % 10)

if __name__ == "__main__":
    root = tk.Tk()
    game = KanjiMemoryGame(root)
    root.mainloop()
