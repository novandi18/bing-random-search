# Bing Random Search Tool

An automated tool for earning Microsoft Rewards points through random Bing searches with configurable delay timing.

## Description

This tool opens Microsoft Edge browser and automatically performs random searches on Bing with adjustable time intervals. The purpose is to help users earn daily Microsoft Rewards points without having to manually perform repeated searches.

## Prerequisites

- Python 3.6 or newer (tested on Python 3.13.2)
- Microsoft Edge browser
- Microsoft account logged in to Edge browser
- Selenium library for Python

## Installation

1. Clone this repository:

   ```
   git clone https://github.com/novandi18/bing-random-search.git
   cd bing-random-search
   ```

2. Install required library:
   ```
   pip install selenium
   ```

## Usage

### Basic Command

```
python random_search.py
```

With the basic command, the program will:

- Open Edge browser
- Perform random searches with 8-second delays
- Run indefinitely until manually stopped with Ctrl+C

### Configuration Options

The program accepts several command line arguments to customize its behavior:

| Argument  | Description                                            | Default Value |
| --------- | ------------------------------------------------------ | ------------- |
| `--delay` | Delay time in seconds between searches                 | 8             |
| `--count` | Maximum number of searches (infinite if not specified) | infinite      |
| `--form`  | Form parameter used in the Bing URL                    | QBRE          |

### Usage Examples

```bash
# Run with 5-second delay
python random_search.py --delay=5

# Run only 20 searches then stop
python random_search.py --count=20

# Set custom form parameter
python random_search.py --form=QBLH

# Combine all options
python random_search.py --delay=3 --count=30 --form=QBLH
```

## Important Notes

1. **Microsoft Edge is required** to be installed on your system.
2. You **must be logged in** with your Microsoft account in Edge browser before running this tool.
3. This tool is **tested on Windows 11**. While it might theoretically work on Linux and macOS, it hasn't been officially tested on those platforms.
4. If **points are not increasing** even though you still have daily quota available:
   - Perform one manual search on Bing
   - Look at the URL and extract the value of the `form` parameter
   - Run this tool with the `--form=value_from_the_url` argument

## Troubleshooting

**Points not increasing:**

1. Make sure you're logged in with your Microsoft account in Edge
2. Verify you still have daily points quota available
3. Try performing one manual search and observe the URL
4. Find the `form=` parameter and copy its value
5. Run the program with that parameter, for example:
   ```
   python random_search.py --form=QBLH
   ```

**Browser not opening:**

1. Make sure Microsoft Edge is properly installed
2. Ensure Selenium is installed correctly (`pip install selenium`)
3. Try restarting your computer if the issue persists

## Security and Ethics

This tool is designed to be used with your own Microsoft account and to facilitate earning Microsoft Rewards points in a more automated way. Responsible usage is strongly recommended.

## Legal Disclaimer

This tool is provided "as is" without warranty of any kind. **Use at your own risk**. Usage of this tool may be against Microsoft Rewards Terms of Service. Be sure to check Microsoft's policies regarding automated scripts.

## Contributing

Contributions and suggestions are always welcome. Please feel free to create a pull request or issue for improvements or feature additions.
