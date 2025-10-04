import pandas as pd
from datetime import datetime
import pathlib
from expense_tracker.models import Expense

class ExpenseManager:
    def __init__(self, file_path="data/expenses.csv"):
        self.file_path = pathlib.Path(file_path)
        if not self.file_path.exists():
            self.file_path.parent.mkdir(parents=True, exist_ok=True)
            df = pd.DataFrame(columns=["Name","Amount","Category","Date"])
            df.to_csv(self.file_path, index=False)
    
    def add_expense(self, expense: Expense) -> None:
        df = pd.read_csv(self.file_path)
        new_expense = {
            "Name": expense.name,
            "Amount": expense.amount,
            "Category": expense.category,
            "Date": expense.date.strftime("%Y-%m-%d")
        }
        df = df.append(new_expense, ignore_index=True) # type: ignore
        df.to_csv(self.file_path, index=False)
        
        