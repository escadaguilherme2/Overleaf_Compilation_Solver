# Overleaf Compilation Solver

This repository was created to assist in setting up a portable LaTeX editor, allowing you to carry your work on a USB drive and use it on any computer without the need for installations or configurations. It also serves as a solution to the compilation limitations present in the free version of Overleaf. Simply download your project as a compressed folder (ZIP) from Overleaf, extract its contents, open it with this editor, and compile it. This way, you can obtain a fully compiled PDF for free, even though the process might be slower than upgrading your Overleaf subscription.

Additionally, this repository provides an optional folder to convert multiple images to PDF, speeding up the compilation process.

## How to Set Up

1. **Create a folder named `LaTeX`.**

2. Download the portable version of Texmaker [here](https://www.xm1math.net/texmaker/download.html).

![2](https://github.com/user-attachments/assets/6d7c30d6-9de2-41f8-8689-4d8b78157c93)

3. **Extract the contents of the downloaded folder.**
    - Locate the folder containing the files and rename it to **Texmaker**.

![3](https://github.com/user-attachments/assets/16f76fdf-a839-45e0-8e18-5b6d7f803a7e)

    - Move it to the `LaTeX` folder you created earlier.

![4](https://github.com/user-attachments/assets/db98e01e-3d1e-4110-9cd7-bf0c621fc850)


4. Download the portable version of MiKTeX [here](https://miktex.org/download).

    **Note:** The file you need is located under the "Installer" section.

![5](https://github.com/user-attachments/assets/c11e487a-1c3e-405a-a2bc-2375c3be0e4a)

5. **Rename the file** to `miktex-portable.exe` and run it.

![6](https://github.com/user-attachments/assets/9c2433a7-d1b5-4c16-a429-c44c9f70117c)

6. During installation, you will be asked for the destination folder. Choose a suitable location such as the `LaTeX` folder or your desktop.  
    **Important:** If selecting a folder, you must add `\MiKTeX` to the end of the path.
    
![7](https://github.com/user-attachments/assets/2bb05192-9cf8-45e4-97c6-ab44d8edc7eb)

7. **Set preferences** during installation. It is recommended to select "Yes" for the option `Install missing packages on-the-fly`.

![8](https://github.com/user-attachments/assets/500afc98-73bc-4c89-b03b-4ddfa08f4fd9)

8. Once the installation is complete, if the MiKTeX folder is not yet in the `LaTeX` folder, move it there now.

    You can now delete the `miktex-portable.exe` installer.

9. Download [this](https://github.com/escadaguilherme2/Overleaf_Compilation_Solver/releases) repository's files.

![image](https://github.com/user-attachments/assets/cb389bae-14f5-411e-95af-66dd1bbf8b58)

10. **Extract the contents of the folder.**
    - Move the file `README (MiKTeX).txt` to the **MiKTeX** folder. This file provides tips and instructions for using MiKTeX.
    - Move the file `RUNME.bat` to the `LaTeX` folder.

## Optional: Image2pdf Tool for Faster Compilation

The **Image2pdf** tool is an optional utility that can help speed up the LaTeX compilation process by converting all images to PDF format.

### Option 1: Python Script (`Image2pdf.py`)

If you have Python installed:

1. Copy the `Image2pdf.py` script to the folder where your images are located.
2. Run the script to convert your images to PDF format.
3. A PDF version of each image will be created with the `.pdf` extension.
4. Update the image references in your LaTeX project.

### Option 2: Executable (`Image2pdf.exe`)

If you do not have Python installed or prefer using an executable, follow these steps:

#### Step 1: Extract `Image2pdf.exe`

The executable is provided as a split ZIP archive due to GitHub's file size limitations. To reassemble it:

1. Download the split archive parts (`Image2pdf.zip.001`, `Image2pdf.zip.002`, etc.).
2. Use **7-Zip** to extract the executable:
   - Right-click on `Image2pdf.zip.001` and select **7-Zip > Extract Here**.
   - Ensure all parts of the split archive are in the same directory before extracting.

#### Step 2: Run the Executable

1. Once `Image2pdf.exe` is extracted, copy it to the folder where your images are located.
2. Run the executable to convert your images to PDF format.
3. A PDF version of each image will be created with the `.pdf` extension.
4. Update the image references in your LaTeX project.

You may delete the executable after use if desired.

Your folder structure should now look similar to this:

![9](https://github.com/user-attachments/assets/5a0fae36-0694-48a2-9bd6-f4b97c354a12)

11. **Final Steps:**
    - It is recommended to read the `README (MiKTeX).txt` file and follow its instructions to ensure MiKTeX is up to date for future use.
    - Once done, you are ready to start using your portable LaTeX editor!
