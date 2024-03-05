import base64
import pdfkit
import numpy as np
import matplotlib.pyplot as plt
from jinja2 import Environment, FileSystemLoader


def draw_chart(data ,data2):
    plt.plot(data)
    plt.plot(data2)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Chart from Data')
    plt.grid(True)
    plt.savefig('chart.png')


# Example usage
data = [1, 2, 7, 4, 5, 4, 7, 2, 1]
data2 = [12, 22, 72, 42, 52, 42, 72, 22, 12]
draw_chart(data,data2)


def render_pdf(template_path, output_path, context):
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template(template_path)
    html_out = template.render(**context)
    pdfkit.from_string(html_out, output_path)


if __name__ == "__main__":
    template_path = 'template.html'
    output_path = 'output.pdf'
    chart_path = 'chart.png'

    table_data = [
        {"name": "John", "age": 30, "city": "New York"},
        {"name": "Alice", "age": 25, "city": "Los Angeles"},
        {"name": "Bob", "age": 35, "city": "Chicago"}
    ]

    table_data2 = [
        {"product": "Laptop", "price": 1000, "stock": 20},
        {"product": "Smartphone", "price": 500, "stock": 50},
        {"product": "Tablet", "price": 300, "stock": 30}
    ]

    table_data3 = [
        {"country": "USA", "population": 331000000, "area": 9834000},
        {"country": "China", "population": 1441000000, "area": 9597000},
        {"country": "India", "population": 1380000000, "area": 3287000}
    ]

    context = {
        'title': 'Sample PDF',
        'content': 'This is a sample PDF created using Python, HTML, Jinja, and pdfkit.',
        'image_data': None, 
        'table_data' : table_data,
        'table_data2' : table_data2,
        'table_data3' : table_data3

    }


    render_pdf(template_path, output_path, context)
