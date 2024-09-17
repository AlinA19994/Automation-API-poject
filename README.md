# Automation API Project

## This Project will fetch the current Bitcoin Price Index (BPI) from a public API and send an email to the user

## 1. Installation

### 01.

Install Python & Pip on your workstation

### 02.

Install the following packages with pip, with the following command:

```
pip install pytest  matplotlib
```

### 03.

Generate an App password from your Gmail Account and copy it

### 04.

Edit the Workflows\Email_flows.py file and Replace Line 16 with the email address you wish to receive the message."

## 2. Running the Tests

### 01.

Open a Powershell Terminal or a linux Terminal and run the following commands:
(Make sure to paste the Gmail Account & Password in the command below)

For Windows(Powershell):

```
cd Test_cases
$env:MY_EMAIL="YOUR_EMAIL"; $env:MY_PASSWORD="YOUR_PASSWORD"; pytest test_api.py --no-header --no-summary -q
```

For Linux:

```
cd Test_cases
export MY_EMAIL="YOUR_EMAIL" MY_PASSWORD="YOUR_PASSWORD" && pytest test_api.py --no-header --no-summary -q
```
