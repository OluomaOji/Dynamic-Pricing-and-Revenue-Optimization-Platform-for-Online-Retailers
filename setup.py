from setuptools import find_packages,setup

# Function to read the requirements.txt file
def parse_requirements(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file if line and not line.startswith('#')]

setup(
    name = "Dynamic-Pricing-and-Revenue-Optimization-Platform-for-Online-Retailers",
    author= "Oluoma Oji",
    version= "0.0.1",
    author_email= "oluomaoji@gmail.com",
    packages= find_packages(include=['src','src*']),
    python_requires='>=3.8',
    install_requires = parse_requirements('requirements.txt'),
    description= "An automated machine learning system that dynamically optimizes product prices for an online retailer based on real-time demand forecasts, competitor analysis, and customer behavior insights."
)