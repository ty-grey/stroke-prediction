import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def generate_graphs():
    df = pd.read_csv('data/clean_data.csv')

    # Plot comparison of stroke vs no stroke in relation to avg glucose level
    plt.figure(figsize=(7, 7))
    sns.distplot(df[df['stroke'] == 0]['avg_glucose_level'], color='black', label='No Stroke')
    sns.distplot(df[df['stroke'] == 1]['avg_glucose_level'], color='red', label='Had Stroke')

    plt.title('No Stroke vs Stroke by Average Glucose Level', fontsize=12)
    plt.legend()
    plt.xlim([50, 325])
    plt.xlabel('Average Glucose Level', fontsize=12)
    plt.ylabel('Density', fontsize=12)
    plt.savefig('static/images/glucose_level_graph.svg')

    # Distribution of the amount of strokes compared to age
    stroke_amount = df.groupby('age').sum()
    people_amount = df.groupby('age').count()
    stroke_percent = (stroke_amount['stroke'] / people_amount['stroke']) * 100

    plt.figure(figsize=(7, 7))
    plt.plot(stroke_percent.index, stroke_percent.values, color='red')
    plt.title('Distribution of Strokes by Age', fontsize=12)
    plt.xlabel('Age', fontsize=12)
    plt.ylabel('Percentage of People that have Experienced a Stroke', fontsize=12)
    plt.savefig('static/images/age_graph.svg')

    # Percentage of strokes vs no strokes separated into genders
    ax = sns.countplot(data=df, x=df['gender'], hue="stroke", palette=['grey', "red"])
    plt.title("Effect of Gender on Stroke", fontsize=12)

    for p in ax.patches:
        ax.annotate(f'{round(p.get_height() / len(df) * 100, 2)} %', xy=(p.get_x() + p.get_width() / 2,
                                                                         p.get_height()), ha='center', va='center',
                    size=6, xytext=(0, 8), textcoords='offset points')

    plt.xticks([0, 1, 2], ['Male', 'Female', 'Other'])
    ax.legend(labels=['No Stroke', 'Had Stroke'])
    plt.xlabel('Gender', fontsize=12)
    plt.ylabel('Count', fontsize=12)
    plt.savefig('static/images/gender_bar.svg')

    # Percentage of strokes vs no strokes separated into smoking status
    ax = sns.countplot(data=df, x=df['smoking_status'], hue="stroke", palette=['grey', "red"])
    plt.title("Effect of Smoking Status on Stroke", fontsize=12)

    for p in ax.patches:
        ax.annotate(f'{round(p.get_height() / len(df) * 100, 2)} %', xy=(p.get_x() + p.get_width() / 2,
                                                                         p.get_height()), ha='center', va='center',
                    size=6, xytext=(0, 8), textcoords='offset points')

    plt.xticks([0, 1, 2, 3], ['Never Smoked', 'Unknown', 'Former Smoker', 'Smoker'])
    ax.legend(labels=['No Stroke', 'Had Stroke'])
    plt.xlabel('Smoking Status', fontsize=12)
    plt.ylabel('Count', fontsize=12)
    plt.savefig('static/images/smoking_bar.svg')
