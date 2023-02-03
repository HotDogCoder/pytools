from appscript import app, mactypes

# Connect to the Illustrator application
ai = app('Adobe Illustrator')

# Select the first layer in the document
ai.documents[0].layers[0].visible.set(False)
