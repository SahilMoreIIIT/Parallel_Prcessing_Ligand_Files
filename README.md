# Parallel_Processing_Ligand_Files

A complete pipeline to convert Ligand files in SMILES format to SDF format.

## Steps to Process SMILES File

1. **Download the Pipeline**

   Clone the repository from GitHub or download it from the provided link:
   ```
   git clone https://github.com/yourusername/Parallel_Processing_Ligand_Files.git
   ```
2. **Copy the SMILES File to the Pipeline Directory**
  Place your SMILES file (e.g., 94_Part_ZincDB_.csv) into the cloned directory.

3. **Copy the Directory to the Server**
   Transfer the directory to the allocated server using scp:
   ```
   scp -r * sahil23079@192.168.3.19:/home/ip_arul/sahil23079
   ```
4. **Run the Splitting Script**
   The script _Split_Single_File.sh will split the single SMILES file into multiple smaller files based on the number of CPU cores available. Ensure the script has executable permissions and then run it:
   ```
   chmod 777 _Split_Single_File.sh
    ./_Split_Single_File.sh
   ```

5. **Run the Parallel Conversion Script**
   Use the multiprocessing.py script to parallelly convert the separate .smi files into separate .sdf formats:
   ```
   python3 multiprocessing.py
   ```
   To run the script in the background, use:
   ```
   nohup python3 multiprocessing.py &
   ```

6. **Merge the Converted SDF Files**
   Merge the separate .sdf files back into a single .sdf file using the _Merge_Multiple_Files script. Make the script executable and then run it:
   ```
   chmod 777 _Merge_Multiple_Files
   ./_Merge_Multiple_Files
   ```
The output will be a merged file, e.g., 94_Part_ZincDB_.sdf (approximately 30GB).

7. **Download the Merged SDF File from the Server**
   Use the following scp command to download the merged .sdf file from the server:
   ```
   scp -r sahil23079@192.168.3.19:/home/ip_arul/sahil23079/94_Part_ZincDB_.sdf .
   ```
