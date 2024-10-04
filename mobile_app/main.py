import joblib
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.list import OneLineListItem
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder

KV = '''
BoxLayout:
    orientation: 'vertical'
    padding: dp(10)
    spacing: dp(10)

    MDTextField:
        id: person_age
        hint_text: "Age"

    MDTextField:
        id: person_income
        hint_text: "Income"

    MDTextField:
        id: person_emp_length
        hint_text: "Employment Length"

    MDTextField:
        id: loan_amnt
        hint_text: "Loan Amount"

    MDTextField:
        id: loan_int_rate
        hint_text: "Loan Interest Rate"

    MDTextField:
        id: loan_percent_income
        hint_text: "Loan Percent Income"

    MDRaisedButton:
        text: "Select Home Ownership"
        id: home_ownership_btn
        on_release: app.show_home_ownership_menu()

    MDRaisedButton:
        text: "Select Loan Intent"
        id: loan_intent_btn
        on_release: app.show_loan_intent_menu()

    MDRaisedButton:
        text: "Select Loan Grade"
        id: loan_grade_btn
        on_release: app.show_loan_grade_menu()

    MDRaisedButton:
        text: "Select Default on File"
        id: default_on_file_btn
        on_release: app.show_default_on_file_menu()

    MDRaisedButton:
        text: "Predict"
        on_release: app.predict()

    MDLabel:
        id: prediction_result
        text: ""
        halign: "center"
'''

class LoanApprovalApp(MDApp):
    def build(self):
        self.model = joblib.load('loan_approval_model.joblib')
        return Builder.load_string(KV)

    def show_home_ownership_menu(self):
        menu_items = [
            {"text": "RENT", "viewclass": "OneLineListItem", "on_release": lambda x="RENT": self.set_home_ownership(x)},
            {"text": "MORTGAGE", "viewclass": "OneLineListItem", "on_release": lambda x="MORTGAGE": self.set_home_ownership(x)},
            {"text": "OWN", "viewclass": "OneLineListItem", "on_release": lambda x="OWN": self.set_home_ownership(x)},
            {"text": "OTHER", "viewclass": "OneLineListItem", "on_release": lambda x="OTHER": self.set_home_ownership(x)},
        ]

        self.home_ownership_menu = MDDropdownMenu(
            caller=self.root.ids.home_ownership_btn,
            items=menu_items,
            width_mult=4,
            position="auto",
            anchor_rectangle=self.root.ids.home_ownership_btn
        )
        self.home_ownership_menu.open()

    def set_home_ownership(self, text):
        self.root.ids.home_ownership_btn.text = text
        self.home_ownership_menu.dismiss()

    def show_loan_intent_menu(self):
        menu_items = [
            {"text": "HOMEIMPROVEMENT", "viewclass": "OneLineListItem", "on_release": lambda x="HOMEIMPROVEMENT": self.set_loan_intent(x)},
            {"text": "PERSONAL", "viewclass": "OneLineListItem", "on_release": lambda x="PERSONAL": self.set_loan_intent(x)},
            {"text": "DEBT CONSOLIDATION", "viewclass": "OneLineListItem", "on_release": lambda x="DEBT CONSOLIDATION": self.set_loan_intent(x)},
            {"text": "EDUCATION", "viewclass": "OneLineListItem", "on_release": lambda x="EDUCATION": self.set_loan_intent(x)},
            {"text": "MEDICAL", "viewclass": "OneLineListItem", "on_release": lambda x="MEDICAL": self.set_loan_intent(x)},
        ]

        self.loan_intent_menu = MDDropdownMenu(
            caller=self.root.ids.loan_intent_btn,
            items=menu_items,
            width_mult=4,
            position="auto",
            anchor_rectangle=self.root.ids.loan_intent_btn
        )
        self.loan_intent_menu.open()

    def set_loan_intent(self, text):
        self.root.ids.loan_intent_btn.text = text
        self.loan_intent_menu.dismiss()

    def show_loan_grade_menu(self):
        menu_items = [
            {"text": "A", "viewclass": "OneLineListItem", "on_release": lambda x="A": self.set_loan_grade(x)},
            {"text": "B", "viewclass": "OneLineListItem", "on_release": lambda x="B": self.set_loan_grade(x)},
            {"text": "C", "viewclass": "OneLineListItem", "on_release": lambda x="C": self.set_loan_grade(x)},
            {"text": "D", "viewclass": "OneLineListItem", "on_release": lambda x="D": self.set_loan_grade(x)},
            {"text": "E", "viewclass": "OneLineListItem", "on_release": lambda x="E": self.set_loan_grade(x)},
            {"text": "F", "viewclass": "OneLineListItem", "on_release": lambda x="F": self.set_loan_grade(x)},
            {"text": "G", "viewclass": "OneLineListItem", "on_release": lambda x="G": self.set_loan_grade(x)},
        ]

        self.loan_grade_menu = MDDropdownMenu(
            caller=self.root.ids.loan_grade_btn,
            items=menu_items,
            width_mult=4,
            position="auto",
            anchor_rectangle=self.root.ids.loan_grade_btn
        )
        self.loan_grade_menu.open()

    def set_loan_grade(self, text):
        self.root.ids.loan_grade_btn.text = text
        self.loan_grade_menu.dismiss()

    def show_default_on_file_menu(self):
        menu_items = [
            {"text": "Yes", "viewclass": "OneLineListItem", "on_release": lambda x="Y": self.set_default_on_file(x)},
            {"text": "No", "viewclass": "OneLineListItem", "on_release": lambda x="N": self.set_default_on_file(x)},
        ]

        self.default_on_file_menu = MDDropdownMenu(
            caller=self.root.ids.default_on_file_btn,
            items=menu_items,
            width_mult=4,
            position="auto",
            anchor_rectangle=self.root.ids.default_on_file_btn
        )
        self.default_on_file_menu.open()

    def set_default_on_file(self, text):
        self.root.ids.default_on_file_btn.text = text
        self.default_on_file_menu.dismiss()

    def predict(self):
        age = int(self.root.ids.person_age.text)
        income = float(self.root.ids.person_income.text)
        emp_length = int(self.root.ids.person_emp_length.text)
        loan_amnt = float(self.root.ids.loan_amnt.text)
        loan_int_rate = float(self.root.ids.loan_int_rate.text)
        loan_percent_income = float(self.root.ids.loan_percent_income.text)
        
        home_ownership = self.root.ids.home_ownership_btn.text
        loan_intent = self.root.ids.loan_intent_btn.text
        loan_grade = self.root.ids.loan_grade_btn.text
        default_on_file = self.root.ids.default_on_file_btn.text

        input_data = [[age, income, home_ownership, emp_length, loan_intent, loan_grade, loan_amnt, loan_int_rate, loan_percent_income, default_on_file]]
        
        prediction = self.model.predict(input_data)

        self.root.ids.prediction_result.text = f"Prediction: {prediction[0]}"

if __name__ == '__main__':
    LoanApprovalApp().run()
