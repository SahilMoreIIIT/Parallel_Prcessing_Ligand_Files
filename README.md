For example, we have 94_Part_ZincDB_.csv (~500MB SMILE File)
Steps Followed
Download the Entire pipeline from GitHub: Parallel_Prcessing_Ligand_Files.git or Drive Final Pipeline
Now copy your smile.csv into this directory (ex: 94_Part_ZincDB_.csv).
Server copy this directory on the server. (ex: Server allotted to me)
scp -r * sahil23079@192.168.3.19:/home/ip_arul/sahil23079

Run Script _Split_Single_File.sh on this file, which takes CPU Core Counts and breaks the single file into counts Line by Line (So no data is corrupted)
chmod 777 _Split_Single_File.sh
./_Split_Single_File.sh

Run script multiprocessing.py (already present in the directory) to parallelly convert those separately .smi files into separate .sdf formats.
python3 multiprocessing.py
nohup python3 multiprocessing.py &	//TO RUN BackGround

Finally, merge the separate .sdf files_Merge_Multiple_Files. In the same order.
chmod 777 _Merge_Multiple_Files
./_Merge_Multiple_Files
Output: 94_Part_ZincDB_.sdf (30GB)The Output File can be downloaded from Serve

Server Download cmd (password required): 
scp -r sahil23079@192.168.3.19:/home/ip_arul/sahil23079/94_Part_ZincDB_.sdf
