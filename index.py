import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("==============================================================================\n")
print("SUBTASK 1")
print('Reading the dataset...')
df = pd.read_excel('2_workshop_DataSet.xlsx', index_col=0, engine='openpyxl')

print("Printing after success reading file")
print(df)

print("==============================================================================\n")
print("SUBTASK 2")
df = df.reset_index()

last_names_unique = df['Last name'].unique().tolist()
first_names_unique = df['first name'].unique().tolist()
groups_unique = df['Group'].unique().tolist()
ai_national_grades_unique = df['The national grading scale Artificial Intelligence'].unique().tolist()
oop_national_grades_unique = df['The national grading scale Object-Oriented Programming'].unique().tolist()

print("Unique last names:", last_names_unique)
print("Unique first names:", first_names_unique)
print("Unique groups:", groups_unique)
print("Unique AI national grades:", ai_national_grades_unique)
print("Unique OOP national grades:", oop_national_grades_unique)

data = {
    'Category': ['Last Names', 'First Names', 'Groups', 'AI National Grades', 'OOP National Grades'],
    'Unique Count': [
        len(last_names_unique),
        len(first_names_unique),
        len(groups_unique),
        len(ai_national_grades_unique),
        len(oop_national_grades_unique)
    ]
}

plot_df = pd.DataFrame(data)

plot_df = plot_df.sort_values(by='Unique Count', ascending=False)

sns.set_style('whitegrid')

plt.figure(figsize=(10, 6))
barplot = sns.barplot(x='Category', y='Unique Count', hue='Category', data=plot_df, palette='coolwarm', legend=False)

plt.title('Unique Values Count per Category', fontsize=18, fontweight='bold', color='navy')
plt.xlabel('Category', fontsize=14, color='black')
plt.ylabel('Unique Count', fontsize=14, color='black')

plt.grid(True, linestyle='--', linewidth=0.5)

plt.xticks(rotation=0, ha='center', fontsize=12)
plt.yticks(fontsize=12)

for p in barplot.patches:
    barplot.annotate(format(p.get_height(), '.0f'),
                     (p.get_x() + p.get_width() / 2., p.get_height()),
                     ha='center', va='center',
                     fontsize=12, color='black',
                     xytext=(0, 8),
                     textcoords='offset points')

plt.tight_layout()
plt.show()

print("==============================================================================\n")
print("SUBTASK 3")
print('Reading the dataset...')
new_df = pd.read_excel('Lab_2_DataSet.xlsx', engine='openpyxl')

print("Printing after success reading file")
print(new_df)
filtered_students = new_df[
    (new_df['The national grading scale Artificial Intelligence'].isin([4, 5])) &
    (new_df['The national grading scale Object-Oriented Programming'].isin([4, 5]))
]

total_filtered_students = filtered_students.shape[0]
total_students = df.shape[0]
other_students = total_students - total_filtered_students

print(f'The number of students with only excellent and good marks in all groups: {total_students}')

print(f'Total students: {total_students}')
print(f'Students with only excellent and good marks: {total_filtered_students}')
print(f'Other students: {other_students}')

labels = ['Excellent/Good Students', 'Other Students']
sizes = [total_filtered_students, other_students]
colors = ['#66b3ff', '#ff9999']

plt.figure(figsize=(8, 6))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140, textprops={'fontsize': 14})
plt.title('Percentage of Students with Excellent and Good Marks', fontsize=18, fontweight='bold')
plt.axis('equal')
plt.show()

plt.figure(figsize=(8, 6))
sns.barplot(x=labels, y=sizes, palette=colors)

plt.title('Count of Students with Excellent/Good Marks vs Others', fontsize=18, fontweight='bold')
plt.ylabel('Number of Students', fontsize=14)
plt.xlabel('Category', fontsize=14)
plt.grid(axis='y', linestyle='--', linewidth=0.5)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

for i, v in enumerate(sizes):
    plt.text(i, v + 0.5, str(v), ha='center', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.show()

print("==============================================================================\n")
print("SUBTASK 4")
unsatisfactory_students = new_df[
    (new_df['The national grading scale Artificial Intelligence'].isin([1, 2])) &
    (new_df['The national grading scale Object-Oriented Programming'].isin([1, 2]))
]

unsatisfactory_by_group = unsatisfactory_students.groupby('Group').size().reset_index(name='Number of Unsatisfactory Students')

print("Printing unsatisfactory mark's count by groups")
print(unsatisfactory_by_group)

plt.figure(figsize=(10, 6))
sns.barplot(
    data=unsatisfactory_by_group,
    x='Group',
    y='Number of Unsatisfactory Students',
    palette='Reds_r'
)

plt.title('Number of Unsatisfactory Students by Group', fontsize=18, fontweight='bold', color='darkred')
plt.xlabel('Group', fontsize=14)
plt.ylabel('Number of Unsatisfactory Students', fontsize=14)
plt.xticks(rotation=0, ha='right', fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis='y', linestyle='--', linewidth=0.5)

for i in range(len(unsatisfactory_by_group)):
    plt.text(
        i,
        unsatisfactory_by_group['Number of Unsatisfactory Students'][i] + 0.2,
        str(unsatisfactory_by_group['Number of Unsatisfactory Students'][i]),
        ha='center', va='bottom', fontsize=12, fontweight='bold'
    )

plt.tight_layout()
plt.show()

print("==============================================================================\n")
print("SUBTASK 5")
plt.close('all')

grade_counts_ai = new_df['The national grading scale Artificial Intelligence'].value_counts().sort_index()
grade_counts_oop = new_df['The national grading scale Object-Oriented Programming'].value_counts().sort_index()

plot_data = pd.DataFrame({
    'Artificial Intelligence': grade_counts_ai,
    'Object-Oriented Programming': grade_counts_oop
})

fig, ax = plt.subplots(figsize=(10, 6))
plot_data.plot(kind='bar', stacked=True, ax=ax, colormap='viridis')

plt.title('Grade Distribution Comparison (AI vs OOP)', fontsize=14, fontweight='bold')
plt.xlabel('Grade', fontsize=12)
plt.ylabel('Number of Students', fontsize=12)
plt.xticks(rotation=0, fontsize=10)
plt.yticks(fontsize=10)
plt.legend(title='Course', fontsize=10, title_fontsize=11)
plt.grid(axis='y', linestyle='--', alpha=0.7)

for i, grade in enumerate(plot_data.index):
    ai_count = plot_data.loc[grade, 'Artificial Intelligence']
    oop_count = plot_data.loc[grade, 'Object-Oriented Programming']

    if ai_count > 0:
        ax.text(i, ai_count / 2, str(ai_count),
                ha='center', va='center', fontsize=9, color='white')
    if oop_count > 0:
        ax.text(i, ai_count + oop_count / 2, str(oop_count),
                ha='center', va='center', fontsize=9, color='white')

plt.tight_layout()
plt.show()

print("==============================================================================\n")
print("SUBTASK 6")
plt.close('all')

task6_df = new_df.copy()

task6_df['Full Name'] = task6_df['first name'] + ' ' + task6_df['Last name']

task6_df['SameMarks'] = task6_df['The national grading scale Artificial Intelligence'] == task6_df[
    'The national grading scale Object-Oriented Programming']

result_df = task6_df.groupby('Group').agg(
    Unique_Names_Count=('Full Name', 'nunique'),
    Same_Marks_Count=('SameMarks', lambda x: sum(x == True)),
    Different_Marks_Count=('SameMarks', lambda x: sum(x == False))
).reset_index()

print("\nStudents with unique names and same marks in each group:")
print(result_df)

fig, ax = plt.subplots(figsize=(10, 6))
result_df.plot(x='Group', y=['Same_Marks_Count', 'Different_Marks_Count'],
               kind='bar', stacked=True, ax=ax,
               color=['#4CAF50', '#F44336'], edgecolor='black')

plt.title('Students: Mark Consistency by Group', fontsize=12, fontweight='bold')
plt.xlabel('Group', fontsize=10)
plt.ylabel('Number of Students', fontsize=10)
plt.xticks(rotation=0, fontsize=10)
plt.yticks(fontsize=10)
plt.legend(['Same Marks', 'Different Marks'], fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.7)

for i, row in result_df.iterrows():
    same = row['Same_Marks_Count']
    diff = row['Different_Marks_Count']

    if same > 0:
        ax.text(i, same / 2, str(same), ha='center', va='center', fontsize=9, color='white')
    if diff > 0:
        ax.text(i, same + diff / 2, str(diff), ha='center', va='center', fontsize=9, color='white')

plt.tight_layout()
plt.show()