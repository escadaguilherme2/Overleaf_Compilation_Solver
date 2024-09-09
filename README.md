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

9. Download [this](https://github.com/escadaguilherme2/Overleaf_Compilation_Solver) repository's files.

10. **Extract the contents of the folder.**
    - Move the file `README (MiKTeX).txt` to the **MiKTeX** folder. This file provides tips and instructions for using MiKTeX.
    - Move the file `RUNME.bat` to the `LaTeX` folder.

## Optional: Image2pdf Tool for Faster Compilation

If you wish to speed up the LaTeX compilation process, consider converting all images to PDF format using the **optional Image2pdf tool**. You have two options depending on your setup:

### Option 1: Python Script (`image2pdf.py`)

If you have Python installed, you can use the Python script:

1. Copy the `image2pdf.py` script to the folder where your images are located.
2. Run the script to convert your images to PDF format.
3. A copy of each image will be created with a `.pdf` extension.
4. Afterward, update the image references in your LaTeX project.

### Option 2: Recombining and Running the Executable (`Image2pdf.exe`)

If you prefer using an executable or don't have Python installed, follow these steps to recombine and run the `Image2pdf.exe`:

1. **Recombine the Executable**:
    - The `Image2pdf.exe` file has been split into multiple parts due to GitHub's file size limitations.
    - To reassemble it:
      1. Run the `combine_file.bat` script.
     
      3. The original executable will be recreated as `Image2pdf.exe`.

    **Important:** If you encounter a security error while running the script, you may need to adjust your PowerShell execution policy. Open PowerShell as an administrator and run:
    ```powershell
    Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
    ```

2. **Running the Executable**:
    - Once recombined, copy `Image2pdf.exe` to the folder containing your images.
    - Run the executable to convert the images to PDF format.
    - Each image will have a `.pdf` copy created in the same folder.
    - After the conversion, update the image references in your LaTeX project.

    You may delete the executable after use.

Your folder structure should now look similar to this:

![9](https://github.com/user-attachments/assets/5a0fae36-0694-48a2-9bd6-f4b97c354a12)

12. **Final Steps:**
    - It is recommended to read the `README (MiKTeX).txt` file and follow its instructions to ensure MiKTeX is up to date for future use.
    - Once done, you are ready to start using your portable LaTeX editor!
