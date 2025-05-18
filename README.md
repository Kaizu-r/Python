# How to Install Python

## For Windows

1. **Download the Python Installer:**
   Go to the official Python website and download the installer for Python 3.10 from this link:
   [Download Python 3.10](https://www.python.org/downloads/release/python-3100/)

2. **Run the Installer:**
   Locate the downloaded `.exe` file (usually in your Downloads folder) and double-click it to run the installer.

3. **Add Python to PATH:**
   Before clicking "Install Now," **make sure to check the box that says "Add Python 3.10 to PATH"**.
   This will let you run Python commands from the Command Prompt anywhere on your system.

4. **Install Python:**
   Click on **"Install Now"** to begin the installation process. The installer will copy all necessary files and set up Python on your computer.

5. **Wait for Installation to Complete:**
   This may take a few minutes. Once finished, you’ll see a success message.

6. **Close the Installer:**
   Click "Close" to exit the setup wizard.

7. **Verify Python Installation:**

   * Open the **Command Prompt**: Press `Win + R`, type `cmd`, and press Enter.
   * Type the following command and press Enter:

     ```
     python --version
     ```
   * You should see the installed Python version printed, like:

     ```
     Python 3.10.0
     ```

8. **Troubleshooting:**

   * If you get an error like `'python' is not recognized as an internal or external command`, it means Python isn’t added to your PATH.
   * You can either reinstall and ensure the "Add to PATH" box is checked, or manually add Python’s install directory to your PATH environment variable.

---

## For Linux (Ubuntu/Debian-based distros)

1. **Open the Terminal:**
   You can usually find this in your applications menu or by pressing `Ctrl + Alt + T`.

2. **Update Package Lists:**
   Run the following command to refresh your package database:

   ```
   sudo apt update
   ```

3. **Upgrade Installed Packages:**
   To make sure everything is up to date, run:

   ```
   sudo apt upgrade
   ```

4. **Install Python 3:**
   Install the latest version of Python 3 available in your distro’s repositories by running:

   ```
   sudo apt install python3
   ```

5. **Check the Installed Python Version:**
   After the installation is complete, verify the installed version with:

   ```
   python3 --version
   ```

   It should display something like:

   ```
   Python 3.12.0
   ```

6. **Optional - Install pip (Python Package Manager):**
   To install Python’s package manager pip, run:

   ```
   sudo apt install python3-pip
   ```

   Verify with:

   ```
   pip3 --version
   ```
