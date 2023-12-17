# Delaimain

Delaimain is an AI-Powered personal assistant that runs on your CPU (no GPU needed!) and locally (no OpenAI API keys needed!). It is designed to be flexible and extensible, allowing it to be customized for specific needs. One of the main features of Delaimain is the modular architecture: you can create modules for Delamain to run using basically any language installed on your computer.

This repository contains the source code for Delaimain. It includes the core components of the assistant, as well as example plugins and language support.

## Requirements and Models

This software with the default model has been tested against a 14GB RAM (heh, it's a laptop) Ryzen 7730U (yeah, it's a laptop) machine running Kubuntu 23.10 .
Theoretically, if you can run gpt4all client on your computer you can also run Delaimain as it uses gpt4all python bindings.

You are free to change the model in config.json using any model supported by gpt4all. As an additional tip, many external models like the ones available on huggingface work like a charm.

## Getting Started

To get started using Delaimain, follow these steps:

1. Clone this repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt` in the root directory of the repository.
3. Start the assistant by running `python delaMain.py` in the root directory of the repository.
4. Chat with the assistant or use one of the configured commands

## Language Support

Delaimain supports a wide range of programming languages.
Besides the growing officially supported languages, Delamain will fallback to a standalone binary if it detects an unsupported language.
For example, if a language named "xyz" is installed and is runnable through "xyz script.x", Delaimain is able to execute it anyway.
Other languages (like nodeJS which is officially supported) requires a proper configuration as their binary does not correspond to their names.

## Scripting

By following the examples in modules.json and the linked modules in scripts/, it is easy to create a new module for your Delaimain.
Let's say you want to execute a script that shutdown your Linux machine:

    sudo shutdown now

While being quite simple, this script is useful to show how Delaimain can be configured.
Let's save this script as shutdown.sh in scripts/ and let's open modules.json.
We now want to add our script in response to a command. Let's add:

    {
        "goBed": {
            "script": "shutdown.sh",
            "type": "sh",
            "description": "Shutting down your computer"
        }
    }

After reloading Delaimain, you will be able to write 'goBed' to see your script executed.

Of course you are encouraged to hack and change everything in Delaimain so to have your perfect assistant.

## Optional features

The following features are disabled by default and can be enabled by setting the related flag in config.json .
Please note that experimental features can lead to unexpected behaviour. Report bugs and feedback please.

### Face

By setting the parameter 'face' to 'true', Delaimain will spawn a little window representing a (work in progess) visual GIF animation of Delaimain itself. By replacing the corresponding GIF in your code you can give Delaimain any aspect you want.

### TTS

The TTS module is currently not working and is a work in progress.

## Future features

The following features are ordered by priority but they can change anytime.
Contributions to this features are welcome and prioritized: please open an issue to notify the others of your contribution.
Feedback is greatly appreciated.

- [ ] Working TTS engine (feel free to change the library used)
- [ ] Smoother face.py engine and management (now is an horrible subprocess)
- [ ] CLI Interface (using https://www.textualize.io)
- [ ] Microphone support (privacy oriented of course)
- [ ] Consequently, hotword support using or on the model of https://thalhammer.github.io/snowman/ or any other alternative that works
- [ ] face.py animations
- [ ] Better overall user experience

## Contributing

We welcome contributions from the community to help make Delaimain even better. If you would like to contribute, please follow these steps:

1. Fork this repository.
2. Create a new branch for your changes.
3. Make your changes and ensure they pass all tests.
4. Submit a pull request to merge your changes into the main repository.

## License

Delaimain is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
