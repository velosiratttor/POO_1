#Simular un `ChatBot` básico que use clases para 
# representar usuarios, respuestas y comandos.
class chatbot:
    def responder(self, mensaje):
        if "hola" in mensaje.lower():
            return "¡Hola! ¿Cómo puedo ayudarte?"
        return "No entendí tu mensaje."


bot = chatbot()
print(bot.responder("Hola, bot"))  
