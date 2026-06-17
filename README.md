# Book_Price_Finder
# Desktop Book Price Finder Application

A desktop Graphical User Interface (GUI) tool engineered using **Python 3**, **PyQt5**, and **SQLite3**. This application serves as a dynamic inventory search engine, allowing users to cross-reference a book title against a relational local database to instantaneously fetch live unit prices and handle localized bulk-order cost modeling.

---

## 🚀 Key Functional Features

- **Decoupled Form Architecture:** Separation of concerns by utilizing a native Qt Designer XML schema (`book_form.ui`) compiled downstream into clean Python layout wrappers (`book_form.py`).
- **Data Validation Safeguards:** Employs a restrictive `QIntValidator` input mask directly onto runtime line edits to prevent alphabetical string noise or fractional values from breaking the application when computing bulk quantities.
- **Relational Integrity Mapping:** Uses parametrized SQL statement queries (`SELECT price FROM books WHERE...`) targeting an efficient SQLite container to block external SQL injection vulnerability paths.

---

## 📊 Architectural Flow

The program adheres to a classic **Model-View-Controller (MVC)** software topology:

```text
   ┌───────────────────────┐
   │       VIEW LAYER      │ <--- User inputs text query into line edit field
   │ (PyQt5 / book_form.py)│
   └───────────┬───────────┘
               │ Triggers Click Signal
               ▼
   ┌───────────────────────┐
   │    CONTROLLER LAYER   │ <--- Evaluates validation parameters and dispatches safe
   │       (main.py)       │      SQL string configurations
   └───────────┬───────────┘
               │ Establishes DB Connection
               ▼
   ┌───────────────────────┐
   │      MODEL LAYER      │ <--- Queries records matching selection rules inside table 
   │      (books.db)       │      structures and returns unit parameters
   └───────────────────────┘

System Prerequisites
Your environment must have Python 3.x installed along with the PyQt5 library module. Download the missing dependencies using pip:

pip install PyQt5

💻 How to Run the Program
1.Clone the Repository:
git clone [https://github.com/YOUR_USERNAME/Book-Price-Finder.git](https://github.com/YOUR_USERNAME/Book-Price-Finder.git)
cd Book-Price-Finder

2.Run the Application Execution Script:
python main.py
