# Stori Technical Challenge
### [Video demo📱](https://www.loom.com/share/f93ce3f5c75d4d42968555c2b05e1653?sid=01736d5f-bf90-4ed6-81c9-70f9b88f57e4)

## Context of the testing framework

This repository contains the technical challenge for Stori. The task involves accessing the website [Rahul Shetty Academy Automation Practice](https://rahulshettyacademy.com/AutomationPractice/) from a mobile browser, whether on a physical device or an emulator. The objective is to interact and test the elements functionalities fo the different website elements.

## Design Decision

I decided to implement a Page Object Model (POM) due to its benefits:

- **Maintainability**: It allows easy maintenance and reduces code duplication by encapsulating the page elements and actions.
- **Readability**: It improves the readability of the tests by separating the test logic from the page interaction logic.
- **Reusability**: It promotes reusability of code as the page objects can be reused across multiple tests.

In this implementation, instead of interacting with different pages, I treated each section of the webpage as a "page" because each section contained a distinct component. Therefore, I considered the components as pages.

Additionally, I used Gherkin to structure the project so that each component tested had its own `.feature` file, along with corresponding `.steps`, `.page`, and `.selectors` files.

### Tools Used

- [**pytest-bdd**](https://pytest-bdd.readthedocs.io/en/stable/#welcome-to-pytest-bdd-s-documentation): 
  - It combines the best of pytest and BDD (Behavior-Driven Development), providing a clear structure for writing and maintaining tests.
- [**Appium-Python-Client**](https://appium.io/docs/en/2.0/quickstart/test-py/):
  - It allows for cross-platform mobile testing, supports multiple programming languages, and integrates well with various test automation frameworks.
- [**selenium**](https://www.selenium.dev/documentation/):
  - It is a widely-used web automation tool that supports various browsers and platforms, making it versatile for different testing needs.

To interact with the Android browser, I used `UiAutomator2`:

- [**UiAutomator2**](https://appium.io/docs/en/2.4/quickstart/uiauto2-driver/): It is preferred because it provides robust support for Android automation, offering a rich set of APIs for interacting with the UI components of Android applications.

## Project Structure
```
Stori-QA-Automation-Challenge/
│
├── allure-results/ 
│ └── ... # Stores the results of the Allure reports
│
├── config/
│  # Configuration files for setting up Android and iOS capabilities
│ ├── init.py
│ ├── android_capabilities.py
│ └── ios_capabilities.py
│ 
│
├── helpers/
│    # Helper functions and scripts to support the main testing tasks
│ ├── init.py
│ ├── get_capabilities.py
│ └── scripts.py
│
├── tests/
│ ├── features/
│ │ # Gherkin feature files describing the behavior and scenarios to be tested
│ │ └── name_of_feature.feature
│ ├── pages/
│ │ Page Object Models representing different sections or components of the application
│ │ └── name_of_feature_page.py
│ ├── selectors/
│ │ # Selectors for the elements to be interacted with in the tests
│ │ └── name_of_feature_selectores.py
│ ├── steps/
│ │ # Step definitions linking Gherkin steps to the underlying test code
│ │ └── test_name_of_feature_steps.py
│ ├── init.py
│
├── .gitignore
│ # Specifies files and directories to be ignored by Git
│
├── init.py
│ # Initialization file for the main package
│
├── conftest.py
│ # Configuration file for pytest, including fixtures and hooks
│
└── requirements.txt
│     # Lists the dependencies required to run the project
```

## Pre-requisites

Before running the framework, ensure that you have the following installed and configured:

1. **Android Studio**: 
   - Install Android Studio and set up an Android emulator.
   - Ensure the emulator is configured and running. You can start the emulator using the command:
     ```sh
     emulator -avd <device_name>
     ```

2. **Appium Server**:
   - Ensure the Appium server is installed and running. Start the Appium server using the command:
     ```sh
     appium
     ```
    Ensure the following drivers are installed:
     - `uiautomator2`
     - `chromium`
    You can install these drivers using the following commands:
     ```sh
     appium driver install uiautomator2
     appium driver install chromium
     ```
    

3. **Environment Variables**:
   - Ensure all necessary environment variables are set in your `.zshrc` or equivalent shell configuration file. For example, you might need to add:
     ```sh
     export ANDROID_HOME=$HOME/Library/Android/sdk
     export PATH=$PATH:$ANDROID_HOME/emulator
     export PATH=$PATH:$ANDROID_HOME/tools
     export PATH=$PATH:$ANDROID_HOME/tools/bin
     export PATH=$PATH:$ANDROID_HOME/platform-tools
     ```
4. **Python Virtual Environment**:
   - Create and activate a virtual environment:
     ```sh
     python3 -m venv venv
     source venv/bin/activate
     ```

5. **Python Dependencies**:
   - Once you activated your virtual environment, install all required Python packages listed in the `requirements.txt` file. You can do this using the following command:
     ```sh
     pip install -r requirements.txt
     ```

## Instructions to Run the Tests

### Running All Tests Without Report

To run all tests without generating a report, use the following command:
```sh
pytest --env android
```

### Running just one test without Report

To run a single test, specify the feature name using the -k option:
```sh
pytest --env android -k <feature_name>
```

### Running Tests with Report
To run tests and generate a report, use the following commands:

```sh
pytest --env android --alluredir allure-results
```

After running the tests, you need to serve the Allure report to view it in an HTML format:

```sh
allure serve allure-results
```

## Observations and Limitations

The tests currently run only on an Android emulator. While the framework has the capability to set up the environment for iOS and the iOS capabilities have been configured, if you attempt to run the tests in an iOS simulator, they will fail. The tests can be launched on the device, but they do not interact with the WebView elements.

Due to the observation mentioned in [Appium's documentation](https://appium.readthedocs.io/en/latest/en/writing-running-appium/web/hybrid/) under the section "Automating hybrid iOS apps," __unfortunately, it is not currently able to handle SafariViewController elements__. Consequently, the pre-requisites for running the tests have been provided only for Android in this README.





