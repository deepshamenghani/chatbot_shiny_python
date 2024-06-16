from shiny import App, ui, render, reactive 
import conversationchatbot  

# Define the UI for the application
app_ui = ui.page_fillable(
    ui.page_auto(
        # Title of the application with styling
        ui.h1("Shiny Web Application Chatbot", style="font-family: Arial, sans-serif; color: #0078B8; text-shadow: 2px 2px 4px #000000; font-size: 2.7em; text-align: center; padding: 20px;"),
        # Description of the application
        ui.markdown("This application allows you to ask questions and get answers using a conversational AI model."),
        # Click the button to add the API key
        ui.card(ui.input_action_button("apikey", "Enter OpenAI API Key to get started", class_="btn-warning")), 
        # Text input for user to enter their question
        ui.input_text("question_input", "Please enter your question and press 'Send':", width="100%"),
        # Button to send the question
        ui.input_action_button("send_button", "Send", class_="btn-primary"),
        # Card to display the answer
        ui.card(
            ui.output_text("answer_output", inline=True),
            style="white-space: pre-wrap; width: 100%; margin: 3; padding: 10px;"
        )
    )
)

def server(input, output, session):
    # Display a modal for API key input when the 'apikey' input is triggered
    @reactive.effect
    @reactive.event(input.apikey)
    def _():
        m = ui.modal(  
            # Input field for the OpenAI API key
            ui.input_password("password", "OpenAI API key:"),
            # Button to connect to OpenAI
            ui.input_action_button("connect", "Connect to OpenAI"),
            easy_close=True,  
            footer=None,  
        )  
        ui.modal_show(m)  # Show the modal

    # Remove the modal when the 'connect' button is pressed
    @reactive.effect  
    @reactive.event(input.connect)  
    def __():  
        ui.modal_remove()  # Hide the modal

    # Define the output for the answer
    @output
    @render.text
    @reactive.event(input.send_button, ignore_none=False)
    def answer_output():
        # Get the user's question from the input
        question = input.question_input()
        if question:
            # Check if the API key has been provided
            if not input.apikey(): 
                return "Please input your OpenAI API key"
            else: 
                # Get the response from the conversational AI model using the provided API key
                response = conversationchatbot.ask_question(question, api_key=input.password())
                return response
        else:
            # Return placeholder text if no question is entered
            return "....."
        
# Create the Shiny app
app = App(app_ui, server)