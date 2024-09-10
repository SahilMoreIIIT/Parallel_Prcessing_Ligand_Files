import os
import time
import pickle
import logging
import multiprocessing
from multiprocessing import Pool, Manager
from openbabel import openbabel
import matplotlib.pyplot as plt

# Configure logging
logging.basicConfig(filename='conversion_errors.txt', level=logging.ERROR)

# Function to convert SMILES file to SDF with 3D coordinates
def convert_smiles_to_sdf(smiles_file, output_directory, error_list=[]):
    try:
        obConversion = openbabel.OBConversion()
        obConversion.SetInAndOutFormats("smi", "mdl")

        # Initialize Open Babel options for adding hydrogens
        obOptions = openbabel.OBConversion()
        obOptions.SetOptions("K", obOptions.OUTOPTIONS)

        output_filename = os.path.splitext(os.path.basename(smiles_file))[0] + ".sdf"
        output_path = os.path.join(output_directory, output_filename)

        with open(smiles_file, 'r') as f:
            with open(output_path, 'w') as output_sdf:
                try:
                    for line in f:
                        mol = openbabel.OBMol()
                        data = (line.split(','))[0].strip()
                        if 'm' in data:
                            continue
                        obConversion.ReadString(mol, data)

                        # Generate 3D coordinates
                        mol.PerceiveBondOrders()
                        mol.SetDimension(3)
                        openbabel.OBBuilder().Build(mol)

                        # Add hydrogen atoms
                        mol.AddHydrogens()

                        # Convert the molecule to SDF format and write to the output .sdf file
                        obConversion.SetOutFormat("sdf")
                        output_sdf.write(obConversion.WriteString(mol))
                        output_sdf.write('\n')
                except ValueError as e:
                    # SMILES parse error
                    logging.error(f"SMILES Parse Error: {str(e)} for input: '{smiles}'")
                    error_list.append((smiles_file, str(e)))
                except RuntimeError as e:
                    # UFFTYPER error
                    logging.error(f"UFFTYPER Error: {str(e)}")
                    error_list.append((smiles_file, str(e)))

    except Exception as e:
        logging.error(f"Error processing file {smiles_file}: {str(e)}")
        error_list.append((smiles_file, str(e)))


#Function to convert SMILES files in a directory to SDF using multiprocessing
def convert_directory_smiles_to_sdf_parallel(input_directory, output_directory, num_cores):
    try:
        # Start time
        start_time = time.time()

        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        # List all files in the input directory with .smi extension
        files = [os.path.join(input_directory, file) for file in os.listdir(input_directory) if file.endswith(".smi")]

        # Error list to collect errors from worker processes
        manager = Manager()
        error_list = manager.list()

        # Set up multiprocessing pool with specified number of cores
        with Pool(processes=num_cores) as pool:
            pool.starmap(convert_smiles_to_sdf, [(file, output_directory, error_list) for file in files])

        # Log errors
        for error in error_list:
            logging.error(f"Error converting {error[0]}: {error[1]}")

        # End time
        end_time = time.time()

        # Calculate the time taken for the conversion
        execution_time = end_time - start_time
        
        return execution_time
    except Exception as e:
        # Log the error
        logging.error(f"Error in converting directory: {str(e)}")
        # Return None if an error occurs
        return None

if __name__ == '__main__':
    path = os.getcwd()
    input_directory =  os.path.join(path,'Input_Files')
    output_directory = os.path.join(path,'Result_Files')
    
    num_cores = max_cores = os.cpu_count()  # Adjust this according to your preference
    
    execution_time = convert_directory_smiles_to_sdf_parallel(input_directory, output_directory, num_cores)
    if execution_time is not None:
        print("Task Completed in {} time".format(execution_time))
    else:
        print("Error occurred during conversion.") 