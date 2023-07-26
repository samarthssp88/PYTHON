'''Write a program to visualize the data using
various charts like: Bar Graph, Scatter Plot, Bubble Chart, Pie chart, Histogram, Box plot'''

##################################

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Sample data for visualization
data = {
    'Bar Graph': {'Student Names': ['Jay', 'Samarth', 'Rahul', 'Siya'], 'Marks': [60, 85, 35, 58]},
    'Scatter Plot': {'X': [1, 2, 3, 4, 5], 'Y': [5, 7, 8, 2, 9]},
    'Bubble Chart': {'X': [3, 5, 2, 6], 'Y': [5, 9, 2, 8], 'Size': [50, 100, 30, 80]},
    'Pie Chart': {'Car Names': ['Suzuki', 'Mahindra', 'Toyota'], 'Efficiency': [50,65,85]},
    'Histogram': {'Data': np.random.randn(100)},
    'Box Plot': {'Data': np.random.randn(100)},
    'Heat Map': np.random.rand(10, 10),
}

# Function to create a bar graph
def create_bar_graph(data):
    plt.bar(data['Student Names'], data['Marks'])
    plt.xlabel('Student Names')
    plt.ylabel('Marks')
    plt.title('Bar Graph')
    plt.show()

# Function to create a scatter plot
def create_scatter_plot(data):
    plt.scatter(data['X'], data['Y'])
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Scatter Plot')
    plt.show()

# Function to create a bubble chart
def create_bubble_chart(data):
    plt.scatter(data['X'], data['Y'], s=data['Size'])
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Bubble Chart')
    plt.show()

# Function to create a pie chart
def create_pie_chart(data):
    plt.pie(data['Efficiency'], labels=data['Car Names'], autopct='%1.1f%%', startangle=90)
    plt.title('Pie Chart')
    plt.show()

# Function to create a histogram
def create_histogram(data):
    plt.hist(data['Data'], bins=10, edgecolor='black')
    plt.xlabel('Values')
    plt.ylabel('Frequency')
    plt.title('Histogram')
    plt.show()

# Function to create a box plot
def create_box_plot(data):
    plt.boxplot(data['Data'])
    plt.ylabel('Values')
    plt.title('Box Plot')
    plt.show()

# Main function to call visualization functions
def main():
    create_bar_graph(data['Bar Graph'])
    create_scatter_plot(data['Scatter Plot'])
    create_bubble_chart(data['Bubble Chart'])
    create_pie_chart(data['Pie Chart'])
    create_histogram(data['Histogram'])
    create_box_plot(data['Box Plot'])
    create_heat_map(data['Heat Map'])

if __name__ == "__main__":
    main()
