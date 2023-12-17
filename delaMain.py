from gpt4all import GPT4All
import json
import os
import subprocess
import pyttsx3
engine = pyttsx3.init() # FIXME aplay error?

face_process = None
tts = False
face = True

model = GPT4All(model_name='mistral-7b-openorca.Q4_0.gguf')
with open("config.json", "r") as f:
    config = json.load(f)
    print("Loaded configuration:")
    for key, value in config.items():
        print(key, value)

def chat_session():
    global tts
    print(".:: Delamain is starting ::.")
    with model.chat_session():
        # Endless chat session with ctrl-c interrupt
        try:
            # Being polite is important
            output = model.generate(prompt='Hello!')
            print("Delamain > " + output)
            while True:
                text = input('> ')
                # Custom modules
                is_done = view_modules(text)
                if is_done:
                    continue
                # SECTION Built in modules are defined here
                # Also 'exit' can be used to exit the chat session
                if text == 'exit':
                    print('Exiting...')
                    do_exit()
                elif text.startswith("complete the following: "):
                    to_complete = text.split("complete the following: ")[1]
                    print("Completing message: " + to_complete)
                    output = complete(to_complete)
                else:
                    # Here delamain generates its own message if nothing has been requested above
                    tokens = []
                    output = model.generate(text, max_tokens=1024)
                # Is reply time!
                print("Delamain >" + output)
                if tts:
                    engine.say(output)
                    engine.runAndWait()
        except KeyboardInterrupt:
            print('Exiting...')
            do_exit()

# INFO Simple completion module
def complete(text):
    tokens = []
    for token in model.generate(text, max_tokens=20, streaming=True):
        tokens.append(token)
    output = tokens.join(" ")
    return output

# INFO Priority to custom modules
def view_modules(text):
    # SECTION Modules are defined here
    is_done = False
    for key, value in config.items():
        if text.startswith(key):
            is_done = True
            arguments = text.split(key)[1]
            if arguments == "":
                print("Warning: no arguments given for module: " + key)
            script = value['script']
            typeOf = value['type']
            description = value['description']
            print("Executing script: " + description)
            dispatcher(script, typeOf, arguments)
    return is_done

# INFO Heavy work is done here
def dispatcher(script, typeOf, arguments):
    global tts
    cmd = ""
    # NOTE We avoid defining types that have the same syntax as the invocation module
    if typeOf == "javascript":
        cmd = "node "
    else:
        cmd = typeOf + " "
    # Finding the script
    path = os.path.dirname(os.path.realpath(__file__)) + "/scripts/" + script
    if not os.path.isfile(path):
        print("Script not found: " + script)
        return
    # Executing the script
    print("Executing script: " + cmd + path + " " + arguments)
    proc = subprocess.run(cmd + path + " " + arguments, shell=True,stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    out = proc.stdout.decode("utf-8")
    print(out)
    if tts:
        engine.say(out)
        engine.runAndWait()

# Terminating gracefully
def do_exit():
    global face_process
    if face_process:
        face_process.terminate()
    exit()

if __name__ == '__main__':
    # Starting face in background
    if face:
        face_process = subprocess.Popen(["python3", "face.py"])
    # Chatting session
    chat_session()