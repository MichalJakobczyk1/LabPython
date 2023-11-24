import os
import shutil


def copy_and_report(base_folder):
    file_counter = 0

    # Open the report file in write mode
    report_path = os.path.join(base_folder, "report.txt")
    with open(report_path, "w") as report_file:

        # Get a list of folders in the base directory
        folder_list = [f for f in os.listdir(base_folder) if os.path.isdir(os.path.join(base_folder, f))]
        print(folder_list)

        # Create the "copies" folder
        copies_folder = os.path.join(base_folder, "copies")
        if not os.path.exists(copies_folder):
            os.makedirs(copies_folder)

        for folder in folder_list:
            folder_path = os.path.join(base_folder, folder)

            # Check if the folder contains image files
            image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.jpg', '.png'))]

            # Save information to the report
            report_file.write(f"Folder: {folder_path}\n")
            report_file.write("Old file names:\n")
            for file in image_files:
                report_file.write(f"- {file}\n")
            report_file.write("\n")

            # Copy files to the "copies" folder and assign new names
            for file in image_files:
                new_name = f"{folder}_{file_counter}.{file.split('.')[-1].upper()}"
                source_path = os.path.join(folder_path, file)
                destination_path = os.path.join(copies_folder, new_name)
                shutil.copy(source_path, destination_path)
                file_counter += 1

    print("Operation completed successfully. See the report in the file:", report_path)


copy_and_report("BaseFolder")
