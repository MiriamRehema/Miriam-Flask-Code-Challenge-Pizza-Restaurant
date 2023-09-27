# Miriam-Flask-Code-Challenge-Pizza-Restaurant

## Table of Content
1. Description 
2. Installation Requirement
3. Technology Used 
4. Conclusion 
5. Licence 
6. Authors Info

## Description

#  Flask Code Challenge - Pizza Restaurants

For this assessment, i will be working with a Pizza Restaurant domain.
I will build out the Flask API to add the functionality described in the deliverables below.
Test you endpoints as stated below

    1. Running the Flask server and using Postman to make requests

# Models
You need to create the following relationships:

    A Restaurant has many Pizzas through RestaurantPizza
    A Pizza has many Restaurants through RestaurantPizza
    A RestaurantPizza belongs to a Restaurant and belongs to a Pizza

# Validations
Add validations to the RestaurantPizza model:

    must have a price between 1 and 30

Add validations to Restaurant Model:

    must have a name less than 50 words in length
    must have a unique name

# Routes:
GET /restaurants

GET /restaurants/:id

DELETE /restaurants/:id

GET /pizzas

POST /restaurant_pizzas


# Frontend

Git clone the repository git clone `git@github.com:MiriamRehema/Miriam-Flask-Code-Challenge-Pizza-Restaurant``
Navigate to the project directory with the command cd Miriam-Flask-Code-Challenge-Pizza-Restaurant

# Technology used

The challenge was mainly based on Python, so I used the following technologies:
Python(your version)

Flask

# Conclusion

Completing this challenge was a great opportunity for me to use my knowledge of Python. I had a nice experience working on the different tasks and I look forward to building more projects using Python.
Migration



Create database tables and initial data using migrations and the seeds.py file. Implement methods and test them in the console using sample data. Follow the suggested order of tasks, but feel free to adapt based on your preference. Ensure methods work as expected and test thoroughly before proceeding. Refactor code for clean and maintainable organization.

This project does include automated tests.

# License

This project is open-source and available under the MIT License. MIT License Copyright (c) 2023 MiriamRehema

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.