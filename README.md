
# PortSwigger_Labs: Automated Web Security Exploitation Tools

This repository houses a collection of Python scripts designed to automate the execution of various web security attacks, primarily targeting vulnerabilities encountered in the PortSwigger Web Security Academy. The project aims to provide a programmatic approach to identifying and exploiting common web application weaknesses, facilitating learning and practice in web penetration testing.

## Badges

[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview

The `PortSwigger_Labs` repository is structured to provide specialized tools for different categories of web vulnerabilities. While currently focusing on SQL Injection and Authentication, the architecture is designed for extensibility to include other attack vectors such as Server-Side Request Forgery (SSRF), Cross-Site Scripting (XSS), and more as development progresses. Each attack category is organized into its own directory, promoting clarity and maintainability.

## Features

*   **Automated Blind SQL Injection:** Scripts designed to automate the detection and exploitation of blind SQL injection vulnerabilities, including time-based and error-based techniques.
*   **Authentication Bypass:** Tools to assist in testing and potentially bypassing authentication mechanisms.
*   **Modular Design:** The repository is organized into directories based on attack types, allowing for easy navigation and the addition of new attack modules.
*   **Extensible Architecture:** Designed to accommodate future additions of other web vulnerability classes (e.g., SSRF, XSS, CSRF, Access Control).
*   **Utility Functions:** Includes helper scripts for common tasks such as ASCII art rendering and flag extraction, valuable in Capture The Flag (CTF) scenarios.

## Installation

To get started with the `PortSwigger_Labs` tools, please follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/NSS0x03/PortSwigger_Labs.git
    cd PortSwigger_Labs
    ```

2.  **Ensure Python 3 is installed:**
    This project requires Python 3.9 or higher. You can download it from [python.org](https://www.python.org/downloads/).

3.  **Install dependencies (if any):**
    Currently, the project has no external Python dependencies beyond the standard library. If future modules require specific libraries, a `requirements.txt` file will be added.

## Usage

The tools are designed to be run from the command line. Each subdirectory contains specific scripts for particular attack types.

### SQL Injection Examples

The `SQLi` directory contains scripts for automating SQL injection attacks.

#### Blind SQL Injection (Time-Based)

This script can be used to brute-force data using time-based blind SQL injection.

```bash
python SQLi/Time_Brute.py <target_url> <parameter_name> <payload_template> <injection_point>


*   `<target_url>`: The URL of the vulnerable application.
*   `<parameter_name>`: The name of the parameter to inject into.
*   `<payload_template>`: A template for the SQLi payload (e.g., `UNION SELECT null, @@version -- `).
*   `<injection_point>`: The position within the query where the injection should occur.
```

#### Error-Based SQL Injection

Scripts like `Error_Brute.py` and `Error_Brute2.py` are designed to leverage error messages returned by the database to extract information.

```bash
python SQLi/Error_Brute.py <target_url> <parameter_name> <error_based_payload>
```

*   `<target_url>`: The URL of the vulnerable application.
*   `<parameter_name>`: The name of the parameter to inject into.
*   `<error_based_payload>`: A payload designed to trigger specific database errors for information disclosure.

### Authentication Examples

The `Authentication` directory may contain scripts or notes related to bypassing or testing authentication mechanisms. Please refer to individual files within this directory for specific usage instructions.

### CTF Utilities

The `CTF_Utils` directory contains helper scripts.

#### Flag Extractor

This script can assist in extracting flags from output.

```bash
python CTF_Utils/Flag_Extractor.py <input_file>
```

*   `<input_file>`: The file containing the output from which to extract flags.

## Directory Structure

```
.
├── Authentication/
│   └── auth.txt              # Notes or scripts related to authentication
├── CTF_Utils/
│   ├── ASCII_reader.py       # Utility for rendering ASCII art
│   ├── Flag_Extractor.py     # Script to extract flags from text
│   └── README.md             # README for CTF Utilities
├── SQLi/
│   ├── Blind_Brute2.py       # Advanced blind SQLi brute-forcing script
│   ├── Error_Brute.py        # Error-based SQLi brute-forcing script
│   ├── Error_Brute2.py       # Alternative error-based SQLi script
│   └── Time_Brute.py         # Time-based blind SQLi brute-forcing script
├── README.md                 # Main README for the repository
└── ...                       # Other potential attack modules and utilities
```

## Future Development

The project is under active development, with plans to incorporate tools for a wider range of web vulnerabilities, including:

*   Server-Side Request Forgery (SSRF)
*   Cross-Site Scripting (XSS)
*   Cross-Site Request Forgery (CSRF)
*   Access Control vulnerabilities
*   And more...

Each new attack vector will likely have its own dedicated directory and associated README for detailed documentation.

