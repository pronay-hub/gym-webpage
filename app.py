from flask import Flask, render_template, request, flash, redirect, url_for

# Initialize the Flask application
app = Flask(__name__)

# A secret key is required to use Flask's 'flash' messages (security feature)
app.secret_key = "fitzone_super_secret_key" 

# Route 1: Serve the main landing page
@app.route("/")
def home():
    return render_template("index.html")

# Route 2: Handle the contact form submission
@app.route("/submit_contact", methods=["POST"])
def submit_contact():
    # Extract the data submitted in the HTML form
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    # In a real app, you would save this to a database or send an email.
    # For now, we will just print it to the server console.
    print("-" * 30)
    print(f"NEW INQUIRY FROM: {name}")
    print(f"EMAIL: {email}")
    print(f"MESSAGE: {message}")
    print("-" * 30)

    # Send a success message back to the frontend
    flash(f"Thanks {name}! Your message was sent successfully. We'll be in touch soon.")
    
    # Redirect the user back to the contact section of the homepage
    return redirect(url_for('home') + '#contact')

if __name__ == "__main__":
    # Run the server in debug mode (auto-reloads when you make changes)
    app.run(debug=True)

