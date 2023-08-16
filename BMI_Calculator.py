from tkinter import *
window = Tk()
window.title("BMI Calculator")
window.minsize(width=250, height=250)
window.config(padx=30,pady=30)


def calculate_bmi():
    weight = my_entry.get()
    height = my_entry2.get()
    if weight == "" or height == "":
        result_label.config(text="Enter both weight and height!")
    else:
        try:
            bmi = float(weight)/((float(height) / 100) ** 2)
            result_string = write_result(bmi)
            result_label.config(text=result_string)
        except:
            result_label.config(text="Enter a valid number!")
def reset_BMI():
    my_entry.delete(0,"end")
    my_entry2.delete(0,"end")
#label
my_label = Label(text="Enter Your Weight (kg)",font=("Arial", 10 ,"normal"))
my_label.pack()
#entry
my_entry = Entry(width=10)
my_entry.pack()
#label2
my_label2 = Label(text="Enter Your Height (cm)",font=("Arial", 10, "normal"))
my_label2.pack()
#entry2
my_entry2 = Entry(width=10)
my_entry2.pack()
#Calculate button
my_button = Button(text="Calculate",command=calculate_bmi)
my_button.pack()
#Reset Button
my_reset_button = Button(text="Reset",command=reset_BMI)
my_reset_button.pack()
#result label
result_label = Label()
result_label.pack()

def write_result(bmi):
    result_string = f"Your BMI is {round(bmi,2)}. You are "
    if bmi <= 16:
        result_string += "severely thin!"
    elif 16 < bmi <= 17:
        result_string += "moderately thin!"
    elif 17 < bmi <= 18.5:
        result_string += "mild thin!"
    elif 18.5 < bmi <= 25:
        result_string += "normal weight"
    elif 25 < bmi <= 30:
        result_string += "overweight"
    elif 30 < bmi <= 35:
        result_string += "obese class 1"
    elif 35 < bmi <= 40:
        result_string += "obese class 2"
    else:
        result_string += "obese class 3"
    return result_string


window.mainloop()
