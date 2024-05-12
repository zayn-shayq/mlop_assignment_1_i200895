
import csv
import subprocess

def save_data(articles, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Description'])  # Writing headers
        for article in articles:
            writer.writerow([article['title'], article['description']])
    
    # Track with DVC
    subprocess.run(['dvc', 'add', filename], check=True)
    subprocess.run(['git', 'add', filename + '.dvc'], check=True)
    subprocess.run(['git', 'commit', '-m', f'Add updated data {filename}'], check=True)
    subprocess.run(['dvc', 'push'], check=True)

def main():
    # Example data (normally you would pass real data here)
    example_data = [{'title': 'Example Title', 'description': 'Example Description'}]
    save_data(example_data, 'example_data.csv')

if __name__ == '__main__':
    main()
