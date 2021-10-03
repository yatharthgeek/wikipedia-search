import wikipedia

bash= input("Ask Question ==>>> ")

result = wikipedia.summary(bash, sentences = 2)

# printing the result

print(result)
