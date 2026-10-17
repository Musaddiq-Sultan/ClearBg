# ClearBg

A command-line interface (CLI) tool written in Python that downloads an image from a URL and automatically removes its background using the `backgroundremover` utility.

## Features

* Image Downloading: Automatically downloads target images directly from a provided URL using `curl`.
* Automatic Background Removal: Integrates with `backgroundremover` to isolate the primary subject of an image and strip out the background.
* Custom Output Naming: Allows users to specify the exact output filename and format for the processed image.

## Prerequisites

Before running the tool, ensure you have the following installed on your system:

* Python 3.x
* curl (Command-line tool for transferring data with URLs)
* backgroundremover: Can be installed via pip:

  ```bash
  pip install backgroundremover
  ```

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/musaddiq-sultan/ClearBg.git
   cd ClearBg
   ```

2. Ensure all external system dependencies (`curl` and `backgroundremover`) are installed and accessible in your system's PATH.

## How to Use

Run the main script from your terminal:

```bash
python main.py
```

### Steps to Remove Image Background

1. **Input Image Link:** Enter the full direct URL of the image you want to process when prompted.
2. **Specify Output File Name:** Enter the desired filename for the output file (e.g., `output.png`).
3. **Processing:** The tool will download the source image and apply background removal.
4. **Result:** The processed image without the background will be saved with your specified file name in the current directory.