🐾 PetGuide: Discord Cat & Dog Recognition Bot
Hey there! This project was created to bring some AI fun to Discord servers while helping our furry friends. Our bot can instantly tell if a photo is a cat or a dog and provides specific care tips based on the result.

🎯 What is the Goal of This Project?
We had a few key goals in mind while building this:

AI in Daily Life: To demonstrate how a model trained with Keras and TensorFlow can work seamlessly in a live environment like Discord.

Helping Pet Owners: Going beyond just "That's a cat" by sharing useful health and nutrition advice (like what they shouldn't eat or how often they should be fed).

Fast & Interactive Analysis: Allowing users to benefit from image processing technology simply by uploading a photo, without needing to touch a single line of code.

🚀 How Does It Work?
The logic is quite straightforward:

Discord Integration (bot.py): It listens for commands and photos. When you use the $analiz command with an attachment, it captures the image.

Smart Prediction Engine (model.py): It takes your photo and asks our "brain" (keras_model.h5), which then calculates the highest probability.

Information Sharing: If it's a dog, it sends a dog-specific guide; if it's a cat, it shares a dedicated care list for cats.

🛠️ What's Under the Hood?
Python & Discord.py: The backbone of the bot.

TensorFlow/Keras: The AI engine that analyzes the images.

Pillow (PIL): Used to resize photos so the bot can "see" them properly.

Pipfile: A list of all the libraries required to run this project.

📖 How to Use
Install the required dependencies (using Pipenv or Pip).

Run the bot.

Upload a cat or dog photo to your Discord channel and type $analiz in the caption.

Wait for the bot to analyze and give you its expert advice! 🐶🐱
