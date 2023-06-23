# How to install Homebrew 

## Installing Homebrew on macOS using Terminal

To install Homebrew on macOS using the terminal, follow these steps:

1. Open the Terminal application on your macOS.

2. Paste the following command into the terminal and press Enter:
`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`

3. The command will start the Homebrew installation process. Follow the on-screen instructions provided by the installer.

4. You may be prompted to enter your administrator password during the installation. Enter the password and press Enter.

5. Wait for the installation to complete. The terminal will display the progress and notify you once Homebrew is successfully installed.

6. If using OhMyZsh or Bash, run the following commands:
   ```bash 
   >> echo 'eval $(/opt/homebrew/bin/brew shellenv)' >> /Users/$USER/.zprofile

   >> eval $(/opt/homebrew/bin/brew shellenv)
   ```

7. To verify that Homebrew is installed correctly, run the following command: `brew -v`
