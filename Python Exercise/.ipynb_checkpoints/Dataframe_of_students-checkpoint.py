#3.DataFrame of students and marks, filter >80
import pandas as pd

data = {
    "Student": ["Animesh", "Preeti", "Amulya", "Shri", "Lavanya"],
    "Marks": [75, 88, 92, 67, 81]
}
df_students = pd.DataFrame(data)
high_scorers = df_students[df_students["Marks"] > 80]
print("\nStudents scoring more than 80:\n", high_scorers)