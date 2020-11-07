from flask import Flask, request, render_template
import random

app = Flask(__name__)

def sort_letters(message):
    """A helper method to sort the characters of a string in alphabetical order
    and return the new string."""
    return ''.join(sorted(list(message)))


@app.route('/')
def homepage():
    """A homepage with handy links for your convenience."""
    return render_template('home.html')

@app.route('/froyo')
def choose_froyo():
    """Shows a form to collect the user's Fro-Yo order."""
    return """
    <form action="/froyo_results" method="GET">
        What is your favorite Fro-Yo flavor? <br/>
        <input type="text" name="flavor"><br/>

        What is your favorite Topping?<br/>
        <input type="text" name="toppings"><br/>

        <input type="submit" value="Submit!">
    </form>
    """

@app.route('/froyo_results')
def show_froyo_results():
    # users_froyo_flavor = request.args.get('flavor')
    # users_froyo_toppings = request.args.get('toppings')
    # return f'You ordered {users_froyo_flavor} flavored Fro-Yo with toppings {users_froyo_toppings}!'

        # Refactor the froyo and froyo_results routes to render a template.......
    context = {
        'user_flavor' : request.args.get('flavor'),
        'user_topping' : request.args.get('toppings')
    }
    return render_template('froyo_results.html', context = context)

# ---------------------------------------------------------------------------------------------
@app.route('/favorites')
def favorites():
    """Shows the user a form to choose their favorite color, animal, and city."""
    return """
    <form action="/favorites_results" method="GET">
        What is your favorite color? <br/>
        <input type="text" name="color"><br/>

        What is your favorite animal?<br/>
        <input type="text" name="animal"><br/>

        What is your favorite city?<br/>
        <input type="text" name="city"><br/>

        <input type="submit" value="Submit!">
    </form>
    """

@app.route('/favorites_results')
def favorites_results():
    users_fav_color = request.args.get('color')
    users_fav_animal = request.args.get('animal')
    users_fav_city = request.args.get('city')
    return f"Wow, I didn't know {users_fav_color} {users_fav_animal} lived in {users_fav_city}!"

# ------------------------------------------------------------------------------------------------
@app.route('/secret_message')
def secret_message():
    """Shows the user a form to collect a secret message. Sends the result via
    the POST method to keep it a secret!"""
    return """
    <form action="/message_results" method="POST">
        Please type in your message!<br/>
        <input type="text" name="message"><br/>
        <input type="submit" value="Send">
    </form>
    """

@app.route('/message_results', methods=['POST'])
def message_results():
    users_secret_message = sort_letters(request.form.get('message'))
    return f"Here's your secret message! <br/><br/> {users_secret_message}"

# ------------------------------------------------------------------------------------------------
@app.route('/calculator')
def calculator():
    """Shows the user a form to enter 2 numbers and an operation."""
    return """
    <form action="/calculator_results" method="GET">
        Please enter 2 numbers and select an operator.<br/><br/>
        <input type="number" name="operand1">

        <select name="operation">
            <option value="add">+</option>
            <option value="subtract">-</option>
            <option value="multiply">*</option>
            <option value="divide">/</option>
        </select>
        <input type="number" name="operand2">

        <input type="submit" value="Submit!">
    </form>
    """

@app.route('/calculator_results')
def calculator_results():
    context = {
        'input1' : int(request.args.get('operand1')),
        'calculation' : request.args.get('operation'),
        'input2' : int(request.args.get('operand2'))
    }
    print(context)
    # result = 
    return  render_template('calculator_results.html', context = context)
    # f"You chose to {operation} {users_input1} and {users_input2} and your result is

# ------------------------------------------------------------------------------------------


# List of compliments to be used in the `compliments_results` route (feel free 
# to add your own!) 
# https://systemagicmotives.com/positive-adjectives.htm
list_of_compliments = [
    'awesome',
    'beatific',
    'blithesome',
    'conscientious',
    'coruscant',
    'erudite',
    'exquisite',
    'fabulous',
    'fantastic',
    'gorgeous',
    'indubitable',
    'ineffable',
    'magnificent',
    'outstanding',
    'propitioius',
    'remarkable',
    'spectacular',
    'splendiferous',
    'stupendous',
    'super',
    'upbeat',
    'wondrous',
    'zoetic'
]

@app.route('/compliments')
def compliments():
    """Shows the user a form to get compliments."""
    return render_template('compliments_form.html')

@app.route('/compliments_results')
def compliments_results():
    """Show the user some compliments."""
    context = {
        # TODO: Enter your context variables here.
    }

    return render_template('compliments_results.html', **context)


if __name__ == '__main__':
    app.run()
