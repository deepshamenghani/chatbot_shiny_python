from shiny import App, ui, render, reactive 
import conversationchatbot  

# Define the UI for the application
app_ui = ui.page_fillable(
    ui.page_auto(
        ui.h1("Shiny Web Application Chatbot", style="font-family: Arial, sans-serif; color: #0078B8; text-shadow: 2px 2px 4px #000000; font-size: 2.7em; text-align: center; padding: 20px;"),
        ui.markdown("This application allows you to ask questions and get answers using a conversational AI model."),
        ui.card(ui.input_action_button("apikey", "Enter OpenAI API Key to get started", class_="btn-warning")), 
        ui.input_text("question_input", "Please enter your question and press 'Send':", width="100%"),
        ui.input_action_button("send_button", "Send", class_="btn-primary"),
        ui.card(
            ui.output_text("answer_output", inline=True),
            style="white-space: pre-wrap; width: 100%; margin: 3; padding: 10px;"
        )
    )
)

def server(input, output, session):
    @reactive.effect
    @reactive.event(input.apikey)
    def _():
        m = ui.modal(  
            ui.input_password("password", "OpenAI api key:"),
            ui.input_action_button("connect", "Connect to OpenAI"),
            easy_close=True,  
            footer=None,  
        )  
        ui.modal_show(m)

    @reactive.effect  
    @reactive.event(input.connect)  
    def __():  
        ui.modal_remove()  

    @output
    @render.text
    @reactive.event(input.send_button, ignore_none=False)
    def answer_output():
        question = input.question_input()
        if question:
            if not input.apikey(): 
                return "Please input your OpenAI API key"
            else: 
                response = conversationchatbot.ask_question(question, api_key=input.password())
                return response
        else:
            return "....."
        
# Create the Shiny app
app = App(app_ui, server)

# Run the Shiny app
if __name__ == "__main__":
    app.run()