/* This is a skeleton code for two-pass multi-way sorting, you can make modifications as long as you meet 
   all question requirements*/  
//Currently this program will just load the records in the buffers (main memory) and print them when filled up.
//And continue this process untill the full Emp.csv is read. 

#include "stdc++.h"
#define buffer_size 22 //defines how many buffers are available in the Main Memory 
using namespace std;

struct EmpRecord {
    int eid;
    string ename;
    int age;
    double salary;
};
EmpRecord buffers[buffer_size]; // this structure contains 22 buffers; available as your main memory.

// Grab a single block from the Emp.csv file, in theory if a block was larger than
// one tuple, this function would return an array of EmpRecords and the entire if
// and else statement would be wrapped in a loop for x times based on block size
EmpRecord Grab_Emp_Record(fstream &empin) {
    string line, word;
    EmpRecord  emp;
    // grab entire line
    if (getline(empin, line, '\n')) {
        // turn line into a stream
        stringstream s(line);
        // gets everything in stream up to comma
        getline(s, word,',');
        emp.eid = stoi(word);
        getline(s, word, ',');
        emp.ename = word;
        getline(s, word, ',');
        emp.age = stoi(word);
        getline(s, word, ',');
        emp.salary = stod(word);
        return emp;
    } else {
        emp.eid = -1;
        return emp;
    }
}

//Printing whatever is stored in the buffers of Main Memory 
//Can come in handy to see if you've sorted the records in your main memory properly.
void Print_Buffers(int cur_size) {
    for (int i = 0; i < cur_size; i++)
    {
        cout << i << " " << buffers[i].eid << " " << buffers[i].ename << " " << buffers[i].age << " " << buffers[i].salary << endl;
    }
}

    //This was just to test and see we are really writing to disk or not
void Read_From_Disk(FILE * pFile)
{
    if (!pFile)
    {
    fprintf(stderr, "The temporary file does not exist on the disk, to read from!\n");
    }
    rewind (pFile);
    fread (buffers,sizeof(buffers[0]),buffer_size,pFile);
    //Print_Buffers(buffer_size);
}

//Sorting the buffers in main_memory based on 'eid' and storing the sorted records into a temporary file 
void Han_Yun_Sort_in_Main_Memory(EmpRecord * buf)  // You can use this sorting algorithm instead of Sort_in_Main_Memory if you want to. 
{
    EmpRecord tmp;
    for(int i = 0; i < buffer_size; ++i)
    {
        for(int j = i+1; j < buffer_size; ++j)
        {
            if(buf[i].eid > buf[j].eid)
            {
                tmp= buf[i];
                buf[i] = buf[j];
                buf[j] = tmp;
            }
        }
    }
}
void merge(EmpRecord * buf, int const start, int const mid, int const end)
{
    int const l_size= mid-start+1;
    int const r_size= end-mid;

    EmpRecord * left_array;   // declare  sub-arrays in merge-sort
    EmpRecord * right_array;
    
    left_array=new EmpRecord [l_size]; //allocate memory for sub-arrays 
    right_array=new EmpRecord [r_size];

    for (int i = 0; i < l_size; i++)   // fill allocated sub-arrays 
    {
        left_array[i]=*(buf+start+i);
    }
    for (int j = 0; j < r_size; j++)
    {
        right_array[j]=*(buf+mid+1+j);
    }

    int i=0,j=0,k=start; //initialize indicies & compare sub-arrays
    while (i<l_size && j<r_size)
    {
        if (left_array[i].eid<right_array[j].eid)
        {
        buf[k]=left_array[i];
        i++;
        }
        else
        {
        buf[k]=right_array[j];
        j++;
        }
    k++;
    }
    
    while (i<l_size) //copy the remaining values to the super array
    {
        buf[k]=left_array[i];
        i++;k++;
    }
    while (j<r_size)
    {
        buf[k]=right_array[j];
        j++;k++;
    }

}
void Sort_in_Main_Memory(EmpRecord * buf, int const start, int const end)
{
    if (start>=end)
        return;
    int mid=start+(end-start)/2;
    Sort_in_Main_Memory(buf,start,mid);
    Sort_in_Main_Memory(buf,mid+1,end);
    merge(buf,start, mid, end);
}

//You can use this function to merge your M-1 runs using the buffers in main memory and storing them in sorted file 'EmpSorted.csv'(Final Output File) 
//You can change return type and arguments as you want. 
void write_sorted_tmpfile_toDisk(EmpRecord * buf, int run_index, int size)
{
    ofstream sorted_blocks_file;
    string sorted_filename="run_" + to_string(run_index) + ".csv";
    sorted_blocks_file.open (sorted_filename);
    for(int i = 0; i < size; ++i)
    {
        sorted_blocks_file << fixed<< buf[i].eid << "," << buf[i].ename << "," << buf[i].age << "," << buf[i].salary <<"\n"<<"";
    }
    sorted_blocks_file.close();

}

FILE* openFile(char* fileName, char* mode)
{
    FILE* fp = fopen(fileName, mode);
    if (fp == NULL) {
        perror("Error while opening the file.\n");
        exit(EXIT_FAILURE);
    }
    return fp;
}

void Merge_Runs_in_Main_Memory(){
    int num_of_runs=19;
    EmpRecord read_in_Emp;
    fstream Disk_Runs, EmpSorted;
    bool flag_2 = true;
    int index_min = 0;
    while(flag_2)
    {
        EmpRecord min_records;
        int file_record_index = 0;
        string sorted_run;
        min_records.eid = INT_MAX;
        file_record_index = 0;
        for(int i = 0; i <= num_of_runs; i++)
        {
            sorted_run = "run_" + to_string(i) + ".csv";
            Disk_Runs.open(sorted_run, ios::in);
            read_in_Emp = Grab_Emp_Record(Disk_Runs);
            cout << read_in_Emp.eid << endl;
            if(read_in_Emp.eid != -1)
            {
                if(read_in_Emp.eid < min_records.eid)
                {
                    min_records = read_in_Emp;
                    index_min = i;
                }
            }
            else
            {
                file_record_index++;
            }
            Disk_Runs.close();            
        }
        
        if(file_record_index > num_of_runs)
        {
            for(int i = 0; i <= num_of_runs; i++)
            {
                sorted_run = "run_" + to_string(i) + ".csv";
                remove(sorted_run.c_str()); 
            }
            flag_2 = false;
            break;
        }
        EmpSorted.open("EmpSorted.csv", ios::out | ios::app);
        EmpSorted << fixed << min_records.eid << "," << min_records.ename << ","
        << min_records.age << "," << min_records.salary << endl;
        EmpSorted.close();

        fstream final_sorted_file_on_disk;
        string s = "";
        string data = "";
        int check = 0;
        final_sorted_file_on_disk.open("final_sorted_file_on_disk.csv", ios::out);
        sorted_run = "run_" + to_string(index_min) + ".csv";
        Disk_Runs.open(sorted_run, ios::in);
        while(getline(Disk_Runs, s))
        {
            if(check != 0)
            {
                if(check == 1)
                    data += s;
                else
                    data += ("\n" + s);
            }
            check++;
        }
        final_sorted_file_on_disk << data;
        Disk_Runs.close();
        final_sorted_file_on_disk.close();
        remove(sorted_run.c_str());
        rename("final_sorted_file_on_disk.csv", sorted_run.c_str());
    }

}


int main() 
{
    fstream input_file;  // open file streams to read and write
    input_file.open("Emp.csv", ios::in);

    bool flag = true;  // flags check when relations are done being read
    int cur_size = 0;
    int run_index=0;
    /*First Pass: The following loop will read each block put it into main_memory 
    and sort them then will put them into a temporary file for 2nd pass */
    while (flag) // FOR BLOCK IN RELATION EMP
    {
      EmpRecord  single_EmpRecord  = Grab_Emp_Record(input_file); // grabs a block
        if (single_EmpRecord.eid == -1)  // checks if filestream is empty
        {
            flag = false;
            //Sort_in_Main_Memory(buffers,0,cur_size-1);
            Han_Yun_Sort_in_Main_Memory(buffers);
            write_sorted_tmpfile_toDisk(buffers, run_index, cur_size);
            //Print_Buffers(cur_size); // The main_memory is not filled up but there are some leftover data that needs to be sorted.
        }
        if(cur_size + 1 <= buffer_size) //Memory is not full store current record into buffers.
        {
            buffers[cur_size] = single_EmpRecord ;
            cur_size += 1;
        }
        else
        {
        //Sort_in_Main_Memory(buffers,0,buffer_size-1); //memory full. Sort the blocks in Main Memory and Store it in a temporary file (runs)
        //Print_Buffers(buffer_size);
        Han_Yun_Sort_in_Main_Memory(buffers);
        write_sorted_tmpfile_toDisk(buffers, run_index,buffer_size);
        run_index+=1;
        cur_size = 0;  //After sorting start again. Clearing memory and putting the current one into main memory
        buffers[cur_size] = single_EmpRecord;
        cur_size += 1;
        }
    }     
  input_file.close();
  


  //Uncomment when you are ready to store the sorted relation
  //fstream sorted_file;  
  //sorted_file.open("EmpSorted.csv", ios::out | ios::app);

  //Pseudocode

  bool flag_sorting_done = false;
  while(!flag_sorting_done){
     Merge_Runs_in_Main_Memory();
      break;
  }
  
  //You can delete the temporary sorted files (runs) after you're done if you want. It's okay if you don't.

  return 0;
}
