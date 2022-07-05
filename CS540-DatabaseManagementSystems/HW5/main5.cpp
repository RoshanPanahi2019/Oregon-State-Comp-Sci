/* This is a skeleton code for Optimized Merge Sort, you can make modifications as long as you meet 
   all question requirements*/  

#include "stdc++.h"
#include "record_class.h"

using namespace std;

//defines how many blocks are available in the Main Memory 
#define buffer_size 22

Records buffers[buffer_size]; //use this class object of size 22 as your main memory

/***You can change return type and arguments as you want.***/

//Sorting the buffers in main_memory and storing the sorted records into a temporary file (runs) 
void Sort_Buffer_emp(int cur_size){
    //Remember: You can use only [AT MOST] 22 blocks for sorting the records / tuples and create the runs
    for (int i = 0; i < cur_size ; i++)
    {
        int min_idx = i;
        for (int j = i + 1; j < cur_size; j++)
        {
            if (buffers[j].emp_record.eid<buffers[min_idx].emp_record.eid)
            {
                buffers[21]=buffers[j];
                buffers[j]=buffers[i];
                buffers[i]=buffers[21];
            }
        }
    }
    return;
}

void Sort_Buffer_deptin(int cur_size){
    //Remember: You can use only [AT MOST] 22 blocks for sorting the records / tuples and create the runs
    for (int i = 0; i < cur_size ; i++)
    {
        int min_idx = i;
        for (int j = i + 1; j < cur_size; j++)
        {
            if (buffers[j].dept_record.managerid<buffers[min_idx].dept_record.managerid)
            {
                buffers[21]=buffers[j];
                buffers[j]=buffers[i];
                buffers[i]=buffers[21];
            }
        }
    }
    return;
}

//Prints out the attributes from empRecord and deptRecord when a join condition is met 
//and puts it in file Join.csv
void PrintJoin() 
{
    fstream joinout;
    joinout.open("Join.csv", ios::out | ios::app);

    joinout<<buffers[21].emp_record.eid<<','<<buffers[21].emp_record.ename<<','<<buffers[21].emp_record.age<<','
    <<buffers[21].emp_record.salary<<','<<buffers[1].dept_record.did<<','<<buffers[1].dept_record.dname<<','<<
    buffers[1].dept_record.budget<<','<<buffers[1].dept_record.managerid<<'\n';

    return;
}

//Use main memory to Merge and Join tuples 
//which are already sorted in 'runs' of the relations Dept and Emp 

void Merge_Join_Runs()
{
    //and store the Joined new tuples using PrintJoin() 
    int num_of_runs=2;
    //Records::EmpRecord read_in_Emp;
    fstream Disk_Runs, EmpSorted, Dept, join;
    bool flag_2 = true;
    int index_min = 0;
    Dept.open("run_deptin_0.csv",ios::in);
    buffers[1]=Grab_Dept_Record(Dept);
    while(flag_2)
    {
        //Records::EmpRecord min_records;
        int file_record_index = 0;
        string sorted_run;
        buffers[21].emp_record.eid= INT_MAX;
        file_record_index = 0;
        
        for(int i = 0; i <= num_of_runs; i++)
        {
            sorted_run = "run_emp_" + to_string(i) + ".csv";
            Disk_Runs.open(sorted_run, ios::in);
            
            buffers[0]=Grab_Emp_Record(Disk_Runs);
            if(buffers[0].no_values != -1)
            {
                if(buffers[0].emp_record.eid < buffers[21].emp_record.eid)
                {
                    
                    buffers[21].emp_record = buffers[0].emp_record;
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
                sorted_run = "run_emp_" + to_string(i) + ".csv";
                remove(sorted_run.c_str()); 
            }
            flag_2 = false;
            break;
        }
    
        while(buffers[1].dept_record.managerid == buffers[21].emp_record.eid && buffers[1].no_values!=-1)
        {
            PrintJoin();
            buffers[1]=Grab_Dept_Record(Dept);
        }

        EmpSorted.open("EmpSorted.csv", ios::out | ios::app);
        EmpSorted << fixed << buffers[21].emp_record.eid << "," << buffers[21].emp_record.ename << ","
        << buffers[21].emp_record.age << "," << buffers[21].emp_record.salary << endl;
        EmpSorted.close();

        fstream final_sorted_file_on_disk;
        string s = "";
        string data = "";
        int check = 0;
        final_sorted_file_on_disk.open("final_sorted_file_on_disk.csv", ios::out);
         sorted_run = "run_emp_" + to_string(index_min) + ".csv";
   
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
   
int main() {

    //Open file streams to read and write
    //Opening out two relations Emp.csv and Dept.csv which we want to join
    fstream empin;
    fstream deptin;
    fstream tmp;

    //1. Create runs for Dept and Emp which are sorted using Sort_Buffer()
    int cur_size=0;
    int run_idx=0;
    int i=0;
    bool flag=true;
    empin.open("Emp.csv", ios::in);

    // Reading and sorting empin
    while (flag)
    {
        Records single_EmpRecord =Grab_Emp_Record(empin);
        
        if (single_EmpRecord.no_values==-1)
        {
           
            flag=false;
            
            Sort_Buffer_emp(cur_size);
            i=0;
            // write temp
            string file="run_emp_" + to_string(run_idx) + ".csv";
            tmp.open(file,ios::out);
            while (i<cur_size)
            {
                tmp<<buffers[i].emp_record.eid<<','<<buffers[i].emp_record.ename<<','<<buffers[i].emp_record.age<<','<<buffers[i].emp_record.salary<<endl;
                i++;
            }
            tmp.close();
        }

        if (cur_size<buffer_size-1 )
        {
            buffers[cur_size] =single_EmpRecord;
            cur_size+=1;
        }
        else
        {
            Sort_Buffer_emp(cur_size);
            
             // write temp
            int i=0;
            string file="run_emp_" + to_string(run_idx) + ".csv";
            tmp.open(file,ios::out);
            while (i<buffer_size-1)
            {
                tmp<<buffers[i].emp_record.eid<<','<<buffers[i].emp_record.ename<<','<<buffers[i].emp_record.age<<','<<buffers[i].emp_record.salary<<endl;
                i++;
            }
            tmp.close();
            run_idx+=1;
            cur_size=0;
            buffers[cur_size] =single_EmpRecord;
            cur_size+=1;
            
        }
    }
    // Reading and sorting dept
    cur_size=0;
    run_idx=0;
    i=0;
    flag=true;
    deptin.open("Dept.csv",ios::in);

    while (flag)
    {
        Records single_deptinRecord =Grab_Dept_Record(deptin);
        if (single_deptinRecord.no_values==-1)
        {
            flag=false;
            Sort_Buffer_deptin(cur_size);
            i=0;
            // write temp
            string file="run_deptin_" + to_string(run_idx) + ".csv";
            tmp.open(file,ios::out);
            while (i<cur_size)
            {
                tmp<<buffers[i].dept_record.did<<','<<buffers[i].dept_record.dname<<','<<buffers[i].dept_record.budget<<','<<buffers[i].dept_record.managerid<<endl;
                i++;
            }
            tmp.close();
        }

        if (cur_size<buffer_size-1 )
        {
            buffers[cur_size] =single_deptinRecord;
            cur_size+=1;
        }
        else
        {
            Sort_Buffer_deptin(cur_size);
            
             // write temp
            int i=0;
            string file="run_deptin_" + to_string(run_idx) + ".csv";
            tmp.open(file,ios::out);
            while (i<buffer_size-1)
            {
                tmp<<buffers[i].dept_record.did<<','<<buffers[i].dept_record.dname<<','<<buffers[i].dept_record.budget<<','<<buffers[i].dept_record.managerid<<endl;
                i++;
            }
            tmp.close();
            run_idx+=1;
            cur_size=0;
            buffers[cur_size] =single_deptinRecord;
            cur_size+=1;
            
            cout<<"Done sorting Emp"<<endl;
        }
    }

    //2. Use Merge_Join_Runs() to Join the runs of Dept and Emp relations 
     Merge_Join_Runs();
    //Please delete the temporary files (runs) after you've joined both Emp.csv and Dept.csv
    remove("run_deptin_0.csv"); 
    remove("EmpSorted.csv");
    return 0;
}
