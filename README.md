# Subdomain-Finder

Subdomain-Finder is a Python tool designed to help penetration testers and bug bounty hunters enumerate subdomains of target domains. By using lists of common or high-probability subdomains, it automates the discovery process and simplifies reconnaissance for security assessments.

## Features

- **Subdomain Enumeration**: Brute-force discovery of subdomains using customizable wordlists.
- **Domain Information Gathering**: Fetch registration and metadata details about domains.
- **Flexible Wordlists**: Supports additional or custom subdomain dictionaries.
- **Easy Integration**: Python-based and designed for simple usage.

## Installation

1. Clone the repository:

    git clone https://github.com/TRISHUL-1/Subdomain-Finder.git
    cd Subdomain-Finder


2. Install dependencies:

    pip install -r requirements.txt


## Usage

### Subdomain Enumeration

Run the subdomain finder script to enumerate subdomains for a given domain

You may edit or provide your own wordlist by modifying `subdomains.txt`, `subdomains1.txt`, or `subdomains-top1million-110000.txt` as needed.

## Wordlists

The repository includes several wordlists (`subdomains.txt`, `subdomains1.txt`, and `subdomains-top1million-110000.txt`) that can be used or customized to improve the coverage of the enumeration process.

## Dependencies

This project requires Python 3 and the following packages (see `requirements.txt`):

- `requests`
- `dnspython`

Ensure you have Python 3 installed before running the tool.

## Disclaimer

This tool is intended for educational purposes and authorized security testing only. The user is solely responsible for any misuse.