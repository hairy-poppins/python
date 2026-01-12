from currency_converter import CurrencyConverter
import customtkinter as ctk

class CurrencyConversion(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Currency Converter")
        self.geometry("700x400")
        self.c = CurrencyConverter()

        # Get list of available currencies
        self.currencies = ['USD', 'EUR', 'GBP', 'JPY', 'CAD', 'AUD', 'CHF', 'CNY', 'INR', 'MXN', 'CHF']

        # Title
        self.label = ctk.CTkLabel(self, text="Currency Converter", font=("Arial", 24, "bold"))
        self.label.pack(pady=20)    

        # Amount Entry Frame
        self.amount_frame = ctk.CTkFrame(self)
        self.amount_frame.pack(pady=10)
        
        self.amount_label = ctk.CTkLabel(self.amount_frame, text="Amount:", font=("Arial", 14))
        self.amount_label.pack(side="left", padx=5)
        
        self.amount_entry = ctk.CTkEntry(self.amount_frame, width=200, placeholder_text="Enter amount")
        self.amount_entry.pack(side="left", padx=5)

        # From Currency Frame
        self.from_frame = ctk.CTkFrame(self)
        self.from_frame.pack(pady=10)
        
        self.from_label = ctk.CTkLabel(self.from_frame, text="From:", font=("Arial", 14))
        self.from_label.pack(side="left", padx=5)
        
        self.from_currency = ctk.CTkComboBox(self.from_frame, values=self.currencies, width=200)
        self.from_currency.set("USD")
        self.from_currency.pack(side="left", padx=5)

        # To Currency Frame
        self.to_frame = ctk.CTkFrame(self)
        self.to_frame.pack(pady=10)
        
        self.to_label = ctk.CTkLabel(self.to_frame, text="To:", font=("Arial", 14))
        self.to_label.pack(side="left", padx=5)
        
        self.to_currency = ctk.CTkComboBox(self.to_frame, values=self.currencies, width=200)
        self.to_currency.set("EUR")
        self.to_currency.pack(side="left", padx=5)

        # Convert Button
        self.convert_button = ctk.CTkButton(self, text="Convert", command=self.perform_conversion, 
                                           font=("Arial", 16, "bold"), width=200, height=40)
        self.convert_button.pack(pady=20)

        # Result Label
        self.result_label = ctk.CTkLabel(self, text="", font=("Arial", 18, "bold"))
        self.result_label.pack(pady=10)

    def perform_conversion(self):
        try:
            amount = float(self.amount_entry.get())
            from_curr = self.from_currency.get()
            to_curr = self.to_currency.get()
            
            result = self.convert(amount, from_curr, to_curr)
            
            if isinstance(result, str) and result.startswith("Error"):
                self.result_label.configure(text=result, text_color="red")
            else:
                self.result_label.configure(
                    text=f"{amount:.2f} {from_curr} = {result:.2f} {to_curr}",
                    text_color="green"
                )
        except ValueError:
            self.result_label.configure(text="Error: Please enter a valid number", text_color="red")
        except Exception as e:
            self.result_label.configure(text=f"Error: {str(e)}", text_color="red")

    def convert(self, amount, from_currency, to_currency):
        try:
            converted_amount = self.c.convert(amount, from_currency, to_currency)
            return converted_amount
        except Exception as e:
            return f"Error: {str(e)}"
        
app = CurrencyConversion()
app.mainloop()