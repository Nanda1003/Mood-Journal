import csv
import datetime
import matplotlib.pyplot as plt
from collections import Counter

class MoodJournal:
    def __init__(self, filename="mood_data.csv"):
        self.filename = filename
        self.moods = ["Happy", "Sad", "Neutral", "Excited", "Angry"]
        self.load_data()

    def load_data(self):
        try:
            with open(self.filename, mode="r") as file:
                self.data = list(csv.reader(file))
        except FileNotFoundError:
            self.data = []
            with open(self.filename, mode="w") as file:
                writer = csv.writer(file)
                writer.writerow(["Date", "Mood"])

    def log_mood(self):
        today = datetime.date.today().strftime("%Y-%m-%d")
        print("Available moods:", ", ".join(self.moods))
        mood = input("Enter your mood for today: ").capitalize()

        if mood not in self.moods:
            print("Invalid mood. Please choose from the list.")
            return

        self.data.append([today, mood])
        with open(self.filename, mode="a") as file:
            writer = csv.writer(file)
            writer.writerow([today, mood])
        print(f"Mood '{mood}' logged for {today}.")

    def visualize_mood(self):
        if len(self.data) < 2:
            print("Not enough data to visualize. Log more moods!")
            return

        mood_counts = Counter([row[1] for row in self.data[1:]])
        moods, counts = zip(*mood_counts.items())

        print("\nChoose a visualization type:")
        print("1. Pie Chart")
        print("2. Bar Graph")
        choice = input("Enter your choice (1/2): ").strip()

        if choice == "1":
            plt.pie(counts, labels=moods, autopct='%1.1f%%', startangle=140)
            plt.title("Mood Distribution")
            plt.show()
        elif choice == "2":
            plt.bar(moods, counts, color="skyblue")
            plt.title("Mood Trends")
            plt.xlabel("Moods")
            plt.ylabel("Count")
            plt.show()
        else:
            print("Invalid choice. Please choose 1 or 2.")

if __name__ == "__main__":
    journal = MoodJournal()

    while True:
        print("\nOptions:")
        print("1. Log Mood")
        print("2. Visualize Moods")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            journal.log_mood()
        elif choice == "2":
            journal.visualize_mood()
        elif choice == "3":
            print("Exiting Mood Journal. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")
