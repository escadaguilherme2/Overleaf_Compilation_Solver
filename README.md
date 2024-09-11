# Overleaf Compilation Solver

This repository was created to assist in setting up a portable LaTeX editor, allowing you to carry your work on a USB drive and use it on any computer without requiring installations or configurations. It also provides a solution to the compilation limitations of the free version of Overleaf. Simply download your project as a compressed folder (ZIP) from Overleaf, extract its contents, open it with this editor, and compile it. This way, you can obtain a fully compiled PDF for free, although the process may be slower than upgrading your Overleaf subscription.

Additionally, this repository includes an optional folder to convert multiple images to PDF, speeding up the compilation process.

## How to Set Up

1. **Create a folder** named **LaTeX**.

2. Download the portable version of **Texmaker** [here](https://www.xm1math.net/texmaker/download.html "Texmaker download page").

   ![1](https://github.com/user-attachments/assets/6d7c30d6-9de2-41f8-8689-4d8b78157c93)

   2.1. **Extract** the contents of the downloaded folder.  
   
   2.2. **Rename** the folder to **Texmaker**.

   ![2](https://github.com/user-attachments/assets/98ebc038-80dd-4c04-96b2-f260c99ee479)

   2.3. **Move** the folder to the **LaTeX** folder created earlier.

   ![3](https://github.com/user-attachments/assets/3917ade8-2a5f-4e50-8d63-358224b53609)

   You can now delete both the original downloaded file and the extracted folder.

3. In the **LaTeX** folder, **create another folder** named **MiKTeX**.

   ![4](https://github.com/user-attachments/assets/3b4ba5ce-6a22-464f-9c3d-c5187172b089)

4. Download the portable version of **MiKTeX** [here](https://miktex.org/download "MiKTeX download page").

   **Note:** The file you need is in the "Installer" section.

   ![5](https://github.com/user-attachments/assets/b8691310-2b15-4245-a799-7c1f99cd2a63)

   4.1. **Rename** the downloaded file to `miktex-portable` and run it.

   ![6](https://github.com/user-attachments/assets/9c2433a7-d1b5-4c16-a429-c44c9f70117c)

   4.2. When asked, select the **MiKTeX** folder as the destination folder.

   ![7](https://github.com/user-attachments/assets/31d2829c-4049-4d30-a3b4-60a69a2f8e76)

   4.3. During setup, it is recommended to choose `Yes` for the option `Install missing packages on-the-fly`.

   ![8](https://github.com/user-attachments/assets/500afc98-73bc-4c89-b03b-4ddfa08f4fd9)

   After installation, you may delete the `miktex-portable.exe` installer.

5. Download the files from [this repository](https://github.com/escadaguilherme2/Overleaf_Compilation_Solver/releases).

   ![9](https://github.com/user-attachments/assets/c2442baa-a075-4398-b1cf-a5b11e5dd840)

   5.1. **Extract** the downloaded files.  
   
   5.2. **Move** the file `README (MiKTeX).txt` to the **MiKTeX** folder, as it contains useful tips and instructions for using MiKTeX.  
   
   5.3. **Move** the file `RUNME.bat` to the **LaTeX** folder.  
   
   5.4. Optionally, **move** the **Image2pdf** folder to the **LaTeX** folder if you'd like to use the image conversion tool.

   Your folder structure should look something like this:

   ![10](https://github.com/user-attachments/assets/31da48c8-1600-48ee-9781-646d1fb0e807)

   You can now delete both the downloaded file and the extracted folder.

7. **Final Steps:**
   - It is recommended to read the `README (MiKTeX).txt` file and follow its instructions to ensure MiKTeX is up-to-date.
   - To start using the portable LaTeX editor, simply run the `RUNME.bat` file located in the **LaTeX** folder.

   ⚠️ **Important:** The `RUNME.bat` file may be flagged by your antivirus software. This is a false positive, and the file is safe. You can view its contents on GitHub for reassurance.

## Optional Image2pdf Tool for Faster Compilation

The **Image2pdf** tool is an optional utility to convert images to PDF format, which can help accelerate the LaTeX compilation process.

### Option 1: Python Script (`Image2pdf.py`)

If you have Python installed:

1. Copy the `Image2pdf.py` script to the folder where your images are located.  
2. Run the script to convert your images to PDF format.  
3. A PDF version of each image will be created with the `.pdf` extension.  
4. Update the image references in your LaTeX project.

If Python is not installed, you can download it [here](https://www.python.org/downloads/ "Python download page").

### Option 2: Executable (`Image2pdf.exe`)

If you prefer not to use Python or do not have it installed, follow these steps to use the executable version of **Image2pdf**:

The executable is provided as a split 7-Zip archive due to GitHub's file size limitations.

1. Ensure both parts of the archive (`Image2pdf.7z.001` and `Image2pdf.7z.002`) are in the same directory.  
2. Right-click on `Image2pdf.7z.001` and select **7-Zip > Extract Here**.  
3. After extraction, copy `Image2pdf.exe` to the folder where your images are located.  
4. Run the executable to convert your images to PDF format.  
5. Update the image references in your LaTeX project.

You may delete the executable after use if desired.

## About

This project is developed by [**escadaguilherme2**](https://github.com/escadaguilherme2), and the repository for this project can be found [here](https://github.com/escadaguilherme2/Overleaf_Compilation_Solver).

Contributions are welcome! If you have suggestions or improvements, feel free to open an issue or submit a pull request on the repository.
