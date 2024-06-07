# 📝 book sales management

This program allows you to manage book sales in a store.

## 📄Features

-  Customer registration: You can add, modify, and remove customers.
-  Book registration: You can add, modify, and remove books, including their ISBN, title, author, price, and available quantity.

- Sales: You can record sales by associating a customer with one or more books, specifying the quantity sold of each. The program automatically updates the quantity of books available in the inventory.

##  Instructions
- Run the program: Download the source code and run it in your Python environment.

- Manage customers and books: Use the available functions to add, modify, and remove customers and books.

- Make sales: Enter the customer code and select the books you want to sell. Specify the quantity sold of each. The program will show you the total of the sale and update the inventory.


##🔧 Main Functions
- read(tasks): Prints all tasks.

- create(tasks, identifier, newTask): Adds a new task to the dictionary..

- update(tasks, identifier, updatedTask): Updates an existing task in the dictionary.
- delete(tasks, identifier): Removes a task from the dictionary.

## 🛠️Usage example

 - 1.Registering a new customer:
 
 -Enter the customer name: "Juan Pérez"
 -Enter the customer's phone number: "312 555 1234"
 
 - 2.Registering a new book:
 
 -Enter the book ISBN: "978-84-206-7242-6"
 -Enter the book title: "One Hundred Years of Solitude"
 -Enter the book author: "Gabriel García Márquez"
 -Enter the book price: 25000
 -Enter the available quantity: 10
 
 - 3.Making a sale:
-Enter the customer code: 1
-Enter the book code: "978-84-206-7242-6"
-Enter the quantity sold: 2
.-The total sale is: 50000
-The available quantity of the book is updated to 8

###Customization
You can modify the source code to adapt it to your specific needs, such as adding new features or changing the interface design.

Enjoy selling books!


###➕Notes
- This is a basic example of a sales management program. You can expand it to include more features, such as sales history, reports, etc.

- **Database:** The program uses an SQLite database to store customer, book and sales information. The database is created automatically when you run the program for the first time. You don't need to configure anything additional.

- **Ejecución:** Asegúrate de tener instalado Python y las bibliotecas necesarias para ejecutar el código.

- **Adaptation:** You can modify the source code to adapt it to your operating system and development environment. ⚙️



### 🤝 Contribuciones
Contributions are welcome. Feel free to fork the repository, make improvements, and submit a pull request.
