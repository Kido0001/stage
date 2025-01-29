# Minecraft Bedrock Command Line Interface
This project allows users to generate crafts, quests, and builds for Minecraft Bedrock using the OpenAI API. The user can interact with the program via menu options.

# Prerequisites
Before you begin, make sure you have the following installed on your machine:

* Python 3.6 or higher

* The following Python modules:

``` os ```

```openai ```

```colorama ```

You can install these modules using the following command:

``` pip install openai colorama ```

# Configuration
1. Create a ```.env``` file at the root of your project and add your OpenAI API key to it:

```OPENAI_KEY=your_openai_api_key_here```

2. Load the environment variables by adding the following line to your Python script:

```load_dotenv()```

# Usage

Run the ```main.py``` script to access the main menu. Here are the main functions:

```menu_menu()```
Displays the main menu and directs the user to the chosen options:

* Craft: Allows you to know the craft of an item by querying the OpenAI API.

* Quest: Generates a challenge with a certain difficulty level by querying the OpenAI API.

* Build: Generates instructions for building a house of a specific size and style by querying the OpenAI API.

* Help: Displays help for the different features.

```menu_craft()```
Asks the user for a craft and sends the input to OpenAI to get the crafting instructions.

```menu_quest()```
Asks the difficulty level of a challenge and sends the input to OpenAI to get an original challenge.

```menu_build()```
Queries the size and style of a house, and sends the input to OpenAI for building instructions.

```menu_help()```
Displays descriptions of the various functions in the program.

```main()```
The main function of the program that runs the main menu in a loop.

# Example

Here is an example of an interactive menu:
```
Where do you want to go?
1. Craft
2. Quest
3. Build
4. Help

Please enter a number:
```
Users can interact with these options to get information about crafting, challenges, and building in Minecraft Bedrock.
