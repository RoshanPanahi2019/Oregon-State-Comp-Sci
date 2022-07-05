#include <string>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <bitset>

using namespace std;

class Record {
public:
    int id, manager_id;
    std::string bio, name;

    Record(vector<std::string> fields) {
        id = stoi(fields[0]);
        name = fields[1];
        bio = fields[2];
        manager_id = stoi(fields[3]);
    }
    void print() {
        cout << "\tID: " << id << "\n";
        cout << "\tNAME: " << name << "\n";
        cout << "\tBIO: " << bio << "\n";
        cout << "\tMANAGER_ID: " << manager_id << "\n";
    }
    int size()
    {
        int size;
        size = name.size() + bio.size() + 16;
        return size;
    }
};


class LinearHashIndex {

private:
    const int PAGE_SIZE = 4096;
    const string Out_FILE="EmployeeIndex.csv";
    const string Out_tmp="tmp.csv";
    const int Capacity_Size = 2867; // Set the capacity of bucket to 70% of Page_Size

    vector<int> pageDirectory;  // Where pageDirectory[h(id)] gives page index of bucket
                                // can scan to pages using index*PAGE_SIZE as offset (using seek function)
    int numBuckets; // n
    int i;
    int ii; //last ii digits of hash value
    int numRecords; // Records in index
    int nextFreePage; // Next page to write to
    int this_BucketSize; 

    // conver to bit format and zero out the rest
    bitset<16> ibits(bitset<16> b,int i)
    {
        for (int j = i; j < 16; j++)
        {
            b.set(j,0);
        }
            return(b);
    }

    // return the last ii bits of the hash key
    int gettHash(int id, int numBuckets, bool flip)
    {
        ii=ceil(log2(numBuckets));
        int hashKey = id % (int)pow(2, 16); 
        bitset<16> bucket_index(hashKey);
        bucket_index=ibits(bucket_index,ii);
        if (flip)
        {
            bucket_index.flip(ii-1);
        }

        int dir_inx= bucket_index.to_ulong();
        return dir_inx;
    }

    // simple hash function
    int getHash(int id, int numBuckets, bool flip)
    {
        int hashKey = id % (int)pow(2, 16)% numBuckets;
        return hashKey;
    }

    Record grab_record_from_file(fstream &input_file, string file_name)
    {
        input_file.open(file_name, ios::in);
        string line, word;
        vector<std::string> fields;
        if (getline(input_file, line, '\n')) 
        {
            // turn line into a stream
            stringstream s(line);
            // gets everything in stream up to comma
            getline(s, word,',');
            fields.push_back(word);
            getline(s, word,',');
            fields.push_back(word);
            getline(s, word,',');
            fields.push_back(word);
            getline(s, word,',');
            fields.push_back(word);    
        }
        Record myRecord(fields);
        fields.clear();
        return (myRecord);
    }

    // Insert new record into index
    void insertRecord(Record record) {
        fstream out_file,tmp;
        
        // No records written to index yet
        if (numRecords == 0) 
        {
            // Initialize index with first buckets (start with 2)
            numBuckets=2;
            pageDirectory.push_back(0);
            pageDirectory.push_back(1);
        }
        out_file.open(Out_FILE, ios::in | ios::out);
        if(!out_file)
        {
            // Make and write to file, two empty buckets.
            out_file.open(Out_FILE, ios::out);
            out_file.close();
            out_file.open(Out_FILE, ios::out | ios::in);
            out_file.seekp(numBuckets * PAGE_SIZE);
            out_file << '$';
            out_file.close();
        }
        else
        {
            out_file.close();
        }
        
        // Compute hash value and go to bucket.
        i = getHash(record.id, numBuckets,false);
        this_BucketSize = 0;
        out_file.open(Out_FILE, ios::out | ios::in); 
        out_file.seekg(i * PAGE_SIZE);
    
        // Look for ampty space in the bucket.
        char c;
        out_file.get(c);
        while(c != 0)
        {
            this_BucketSize++;
            out_file.get(c);
        }
        
        // Check if bucket will pas capacity.
        if(this_BucketSize + record.size() > Capacity_Size )
        {
                
            //This bucket has reached the %70 capacity. Adding to number of buckets. Open a temporary file double the size
            // Step 1: Do a bit flip 
            int newNumBuckets = numBuckets+1;
            tmp.open(Out_tmp, ios::out);
            tmp.close();
            tmp.open(Out_tmp,ios::out | ios::in);
            tmp.seekp(newNumBuckets * PAGE_SIZE);
            tmp << '$';        

            //cout<< "copying data from the output File to a temprary File...";
            int tmpSize;
            for(int bucketIndex = 0; bucketIndex < numBuckets; bucketIndex++)
            {
                out_file.seekg(bucketIndex * PAGE_SIZE);
                string s, tmpName, tmpBio, tuple;
                int tempID, tmpManagerID;
                while(getline(out_file,tuple, '$'))
                {
                    stringstream ss(tuple);
                    getline(ss,s,',');
                    tempID = stoi(s);
                    getline(ss,s,',');
                    tmpName = s;
                    getline(ss,s,',');
                    tmpBio = s;
                    getline(ss,s, ',');
                    tmpManagerID = stoi(s);

                    i = getHash(tempID, newNumBuckets,false);

                    tmp.seekg(i * PAGE_SIZE);
                    char d;
                    tmp.get(d);
                    tmpSize=0;
                    while(d != 0)
                    {
                        tmpSize++;
                        tmp.get(d);
                    }
                    tmp.seekp(i * PAGE_SIZE + tmpSize);
                    tmp << tempID << "," << tmpName << ","
                    << tmpBio << "," << tmpManagerID << "," << '$';

                    if(out_file.peek() == 0)
                        break;
                }
            }
            numBuckets = newNumBuckets;
            //cout<< "finished copying to tmp"<<endl;
            //cout << "resume inserting..."<< endl;
            i = getHash(record.id, numBuckets,false);
            
            tmp.seekg(i * PAGE_SIZE);
            char d;
            tmp.get(d);
            tmpSize=0;
            while(d != 0)
            {
                tmpSize++;
                tmp.get(d);
            }
            tmp.seekp(i * PAGE_SIZE + tmpSize);
            tmp << record.id << "," << record.name << "," 
            << record.bio << "," << record.manager_id << '$';
            
            tmp.close();
            out_file.close();
            remove(Out_FILE.c_str());
            rename(Out_tmp.c_str(), Out_FILE.c_str());
            numRecords++;
        }
        else
        {
            cout<< "Inserting record to byte= "<< this_BucketSize << " of buckets =" << i << endl;
            out_file.seekp(i * PAGE_SIZE + this_BucketSize);
            out_file << record.id << "," << record.name << "," 
            << record.bio << "," << record.manager_id << '$';
            numRecords++;
            out_file.close();
        }
        cout<< "number of numRecords inserted = "<<numRecords << " numbr of buckets= "<<numBuckets<< endl;
    }

public:

    LinearHashIndex(string indexFileName) 
    {
        numBuckets = 0;
        i = 0;
        numRecords = 0;
    }

    // Write to index from file
    void createFromFile(string csvFName) 
    {
        fstream input_file;
        string line;
        input_file.open(csvFName, ios::in);
        while (getline(input_file, line, '\n')) 
        {
            stringstream ss(line);
            string s;
            vector<string> fields;
            getline(ss, s, ',');
            fields.push_back(s);
            getline(ss, s, ',');
            fields.push_back(s);
            getline(ss, s, ',');
            fields.push_back(s);
            getline(ss, s, ',');
            fields.push_back(s);
            
            Record employeeInfo(fields);

            insertRecord(employeeInfo);
            fields.clear();
        }
        input_file.close();
    }

    // ID Look up
    Record findRecordById(int id) 
    {
        int bucketIndex = getHash(id, numBuckets, false);
        int query;
        fstream result;
        string tuple, s;
        vector<string> fields;
        result.open(Out_FILE, ios::in);
        result.seekg(bucketIndex * PAGE_SIZE);

        while(getline(result, tuple,'$'))
        {
            stringstream ss(tuple);
            getline(ss, s, ',');
            query = stoi(s);
            //cout<<query<<endl;
            if(query == id)
            {
                fields.push_back(s);
                getline(ss, s, ',');
                fields.push_back(s);
                getline(ss, s, ',');
                fields.push_back(s);
                getline(ss, s, ',');
                fields.push_back(s);

                Record answer(fields);
                cout<<"\n>Employee ID : "<< answer.id<< "\n \n>Employee Name: " << answer.name <<"\n \n>Employee Bio:"<< answer.bio <<"\n \n>Manager ID: "<< answer.manager_id<<"\n"<<endl;
                return answer;
            }
            if(result.peek() == 0)break;
        }
        s = -1;
        for(int j = 0; j < 4; j++)
        {
            fields.push_back(s);
        }
        Record ignore(fields);
        return ignore;
    }
};
